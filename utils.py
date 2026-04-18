# utils.py
"""Вспомогательные функции для симулятора."""

import time


def slow_print(text: str, delay: float = 0.05) -> None:
    """Выводит текст с задержкой для эффекта."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def clear_console() -> None:
    """Очищает консоль."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def show_intro() -> None:
    """Показывает вступление."""
    print("=" * 60)
    print("     ДОБРО ПОЖАЛОВАТЬ В КОНСОЛЬНЫЙ СИМУЛЯТОР ЭКОСИСТЕМЫ")
    print("=" * 60)
    print("\nВ этой симуляции вы увидите:")
    print("  🌿 Растения (фотосинтезируют и служат едой)")
    print("  🐇 Травоядные (едят растения)")
    print("  🐺 Хищники (охотятся на травоядных)")
    print("\nНажмите Enter, чтобы начать симуляцию...")
    input()