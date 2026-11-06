from validation import input_current, input_voltage
from menu import show_menu, select_mode, mode_name
from operations import power, voltage_class

def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт мощности электропровода ===")

    while True:
        show_menu()
        cosf = select_mode()
        if cosf is None:
            print('Работа завершена.')
            break
        u = input_voltage()
        i = input_current()

        if u<12 or u>1000:
            print('Ошибка! Напряжение вне допустимого диапозона.')

        if i<0.1 or i>500:
            print('Ошибка! Ток вне допустимого диапозона.')

        p = power(u, i, cosf)
        u_cls = voltage_class(u)
        name = mode_name (cosf)

        print("\n Результаты ")
        print(f"Тип нагрузки: {name} (cosf = {cosf})")
        print(f"P (мощность): {p:.2f} кВт")
        print(f"Класс напаряжения: {u_cls}")
        print("\n")


if __name__ == "__main__":
    main()