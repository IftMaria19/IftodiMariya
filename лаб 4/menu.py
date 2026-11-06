"""
Меню выбора режима обработки через match-case.
"""

from __future__ import annotations

from connstans import COSF_ACTIVE, COSF_IND, COSF_SMESH

def show_menu() -> None:
    """Вывести меню режимов."""
    print("\n Выберите тип нагрузки:")
    print("  1 — активная  (cosf = 1.0 )")
    print("  2 — индуктивная (cosf = 0.85)")
    print("  3 — смешанная (cosf = 0.75)")


def select_mode() -> float | None:
    """
    Циклически запрашивать режим и возвращать косинус cosf.

    Использует match-case для маршрутизации.
    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер типа (от 0 до 3): ").strip()
        match choice:
            case "1":
                return COSF_ACTIVE
            case "2":
                return COSF_IND
            case "3":
                return COSF_SMESH
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")

def mode_name(k: float) -> str:
    """Вернуть название режима по косинусу."""
    match k:
        case 1.0:
            return "активная"
        case 0.85:
            return "индуктивная"
        case 0.75:
            return "смешанная"
        case _:
            return "неизвестный"
