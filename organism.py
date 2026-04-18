# organism.py
"""Модуль, содержащий классы организмов."""

from abc import ABC, abstractmethod


class Organism(ABC):
    """Абстрактный базовый класс для всех организмов."""

    def __init__(self, name: str, energy: float):
        """
        Инициализация организма.

        Args:
            name: Имя организма.
            energy: Начальный уровень энергии.
        """
        self.name = name
        self.energy = energy

    @abstractmethod
    def daily_action(self) -> None:
        """Действие, выполняемое организмом каждый день."""
        pass

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм."""
        return self.energy > 0

    def reduce_energy(self, amount: float) -> None:
        """Уменьшает энергию организма."""
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, energy={self.energy:.1f})"


class Herbivore(Organism):
    """Травоядное животное — ест растения."""

    def __init__(self, name: str, energy: float, eating_efficiency: float = 1.2):
        super().__init__(name, energy)
        self.eating_efficiency = eating_efficiency

    def daily_action(self) -> None:
        """Травоядное теряет энергию и ищет еду."""
        self.reduce_energy(5)
        print(f"  🐇 {self.name} ищет траву. Энергия: {self.energy:.1f}")

    def eat(self, plant_energy: float) -> None:
        """Поедание растения."""
        gained = plant_energy * self.eating_efficiency
        self.energy += gained
        print(f"  🐇 {self.name} съел растение (+{gained:.1f} энергии)")


class Carnivore(Organism):
    """Хищник — ест травоядных."""

    def __init__(self, name: str, energy: float, hunting_success: float = 0.7):
        super().__init__(name, energy)
        self.hunting_success = hunting_success

    def daily_action(self) -> None:
        """Хищник теряет энергию и охотится."""
        self.reduce_energy(8)
        print(f"  🐺 {self.name} ищет добычу. Энергия: {self.energy:.1f}")

    def hunt(self, prey_energy: float) -> float:
        """Охота на жертву. Возвращает полученную энергию."""
        gained = prey_energy * self.hunting_success
        self.energy += gained
        print(f"  🐺 {self.name} поймал добычу (+{gained:.1f} энергии)")
        return gained


class Plant(Organism):
    """Растение — восстанавливает энергию от солнца."""

    def __init__(self, name: str, energy: float, growth_rate: float = 1.1):
        super().__init__(name, energy)
        self.growth_rate = growth_rate

    def daily_action(self) -> None:
        """Растёт за счёт фотосинтеза."""
        self.energy *= self.growth_rate
        print(f"  🌿 {self.name} фотосинтезирует. Энергия: {self.energy:.1f}")