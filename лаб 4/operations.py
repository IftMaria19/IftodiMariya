"""
Расчёты: Косинус, мощность, класс напряжения
"""
from typing import Annotated

from connstans import U_LOW_LIMIT, U_HIGH_LIMIT

def power(u: Annotated[float, "Напряжение, В"], 
          i: Annotated[float, "Ток, А"], cosf: float) -> float:
    """ Рассчитать мощность P = U * I * cosf / 1000, кВт. """
    return (u * i * cosf) / 1000

def voltage_class(u:Annotated[float, "Напряжение, В"]) -> str:
    """ Классифицировать напряжение через if-elif-else."""
    if u < U_LOW_LIMIT:
        return 'низкое напряжение'
    elif u <= U_HIGH_LIMIT:
            return 'нормальное напряжение'
    else:
         return 'высокое напряжение'

    