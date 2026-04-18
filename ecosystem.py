# ecosystem.py
"""Модуль экосистемы, управляющий всеми организмами."""

from typing import List
from organism import Organism, Herbivore, Carnivore, Plant


class Ecosystem:
    """Класс, управляющий экосистемой."""

    def __init__(self, name: str = "Ecosystem"):
        """
        Инициализация экосистемы.

        Args:
            name: Название экосистемы.
        """
        self.name = name
        self.organisms: List[Organism] = []
        self.day = 0

    def add_organism(self, organism: Organism) -> None:
        """Добавляет организм в экосистему."""
        self.organisms.append(organism)
        print(f"+ Добавлен: {organism}")

    def remove_dead(self) -> None:
        """Удаляет всех мёртвых организмов."""
        dead = [org for org in self.organisms if not org.is_alive()]
        for org in dead:
            print(f"☠️  {org.name} умер.")
            self.organisms.remove(org)

    def simulate_day(self) -> None:
        """Симулирует один день в экосистеме."""
        self.day += 1
        print(f"\n{'=' * 50}")
        print(f"День {self.day} в {self.name}")
        print(f"{'=' * 50}")

        # Шаг 1: растения растут
        for org in self.organisms:
            if isinstance(org, Plant):
                org.daily_action()

        # Шаг 2: травоядные едят растения
        for org in self.organisms[:]:
            if isinstance(org, Herbivore) and org.is_alive():
                # Ищем растение
                for plant in self.organisms:
                    if isinstance(plant, Plant) and plant.is_alive() and plant.energy > 5:
                        org.eat(min(plant.energy, 15))
                        plant.reduce_energy(10)
                        break
                org.daily_action()

        # Шаг 3: хищники охотятся на травоядных
        for org in self.organisms[:]:
            if isinstance(org, Carnivore) and org.is_alive():
                for prey in self.organisms:
                    if isinstance(prey, Herbivore) and prey.is_alive():
                        org.hunt(prey.energy)
                        prey.reduce_energy(prey.energy)
                        break
                org.daily_action()

        # Шаг 4: удаляем мёртвых
        self.remove_dead()

    def get_statistics(self) -> dict:
        """Возвращает статистику экосистемы."""
        stats = {
            "day": self.day,
            "total": len(self.organisms),
            "herbivores": sum(1 for o in self.organisms if isinstance(o, Herbivore)),
            "carnivores": sum(1 for o in self.organisms if isinstance(o, Carnivore)),
            "plants": sum(1 for o in self.organisms if isinstance(o, Plant)),
        }
        return stats

    def show_statistics(self) -> None:
        """Выводит статистику в консоль."""
        stats = self.get_statistics()
        print(f"\n📊 Статистика (день {stats['day']}):")
        print(f"   Всего организмов: {stats['total']}")
        print(f"   Травоядных: {stats['herbivores']}")
        print(f"   Хищников: {stats['carnivores']}")
        print(f"   Растений: {stats['plants']}")