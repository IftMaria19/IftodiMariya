# -- Косинусы нагрузки (Вариант 5)--
COSF_ACTIVE: float = 1.0 #активная
COSF_IND: float = 0.85 #индуктивная
COSF_SMESH: float = 0.75 #смешанная

# --  Допустимые диапазоны входных данных --
U_MIN: float = 12.0
U_MAX: float = 1000.0
I_MIN: float = 0.1
I_MAX: float = 500.0

# --- Пороговые значения для классификации напряжения ---
U_LOW_LIMIT: float = 220.0    # U < 220 — низкое
U_HIGH_LIMIT: float = 400.0    #U > 400 — высокое

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"
