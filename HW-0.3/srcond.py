from typing import Callable


def some_func(): pass


def repeat(call_count: int,
           start_sleep_time: float,
           factor: int,
           border_sleep_time: float):

    def _repeat(func):
        for n in range(call_count):
            if t < border_sleep_time:
                t = start_sleep_time * 2**n
            else:
                t = border_sleep_time

            def wrap(*args, **kwargs):
                func_result = func(*args, **kwargs)
                print(f'Запуск номер {n + 1}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}')
                return func

            return wrap
    return _repeat


@repeat(call_count=3, start_sleep_time=0, factor=3, border_sleep_time=10)
def printer():
    return 'RRRRRRRRR'

printer()
