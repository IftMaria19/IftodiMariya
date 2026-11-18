# validate
def check_window(window, n):
    'Проверка окна'
    try:
        is_positive_window = (int(window)>=1) and window <= n
    except (TypeError, ValueError) as err:
            raise ValueError(
                f'window должно быть положительным целым числом'
                f'(получено: {window!r}; причина: {err.args[0]})'
            ) from err
    if not is_positive_window:
        raise ValueError(f'должно быть целым числом (получено {window!r})')

def simple_moving_average(data, window):
    n=len(data)
    check_window(window, n)
    result=[]
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window])/ window)
    return result

def optimized_moving_average(data, window):
    "SMA через бегущую сумму (O(n)), работает быстрее"
    n=len(data)
    check_window(window, n)
    "считаем сумму первых 'window' эллементов"
    running = sum(data[:window])
    "среднее знач"
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data, window):
    "центрированное скользящее среднее (окно чётное)"
    if window % 2 == 0:
        raise ValueError('окно для центрированного окна должно быть нечётным')
    n=len(data)
    check_window(window, n)
    result=[]
    half_window = window//2
    for i in range ( half_window, n - half_window):
        current_slice = data[i - half_window: i + half_window + 1]
        result.append(sum(current_slice)/window)
    return result

def exponential_moving_average(data, alpha):
    """Экспоненциальное скользящее среднее."""
    if not (0 < alpha <= 1):
        raise ValueError("Параметр alpha должен быть в диапазоне (0, 1].")
    if not data:
        raise ValueError("Ряд пуст.")
        
    ema = [data[0]]  # Первое значение равно первому элементу ряда
    
    # Начинаем со второго элемента (индекс 1)
    for i in range(1, len(data)):
        # Формула из методички
        current_ema = alpha * data[i] + (1 - alpha) * ema[i-1]
        ema.append(current_ema)
        
    return ema




    