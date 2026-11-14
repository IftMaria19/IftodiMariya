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
         raise ValueError(
              f'должно быть целым числом (получено {window!r})')

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




    