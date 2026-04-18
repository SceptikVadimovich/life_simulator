# main.py
"""Главный модуль для запуска симуляции экосистемы."""

from config import GITHUB_REPO_URL
from ecosystem import Ecosystem
from organism import Herbivore, Carnivore, Plant
from utils import show_intro, clear_console


def main() -> None:
    """Основная функция программы."""
    clear_console()
    show_intro()

    # Создаём экосистему
    eco = Ecosystem("Лесная поляна")

    # Добавляем организмы
    eco.add_organism(Plant("Дуб", 30))
    eco.add_organism(Plant("Трава", 20))
    eco.add_organism(Plant("Куст", 15))

    eco.add_organism(Herbivore("Заяц", 40))
    eco.add_organism(Herbivore("Олень", 60))
    eco.add_organism(Herbivore("Белка", 25))

    eco.add_organism(Carnivore("Волк", 80))
    eco.add_organism(Carnivore("Лиса", 50))

    # Запускаем симуляцию на 10 дней
    for _ in range(10):
        eco.simulate_day()
        eco.show_statistics()

        # Проверка на вымирание
        if eco.get_statistics()["total"] == 0:
            print("\n💀 Экосистема полностью вымерла. 💀")
            break

    print(f"\n{'=' * 60}")
    print("Симуляция завершена.")
    print(f"\nСсылка на репозиторий: {GITHUB_REPO_URL}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()