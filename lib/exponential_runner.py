import time
from typing import Callable, TypeVar

RT = TypeVar("RT")  # return type


def run_exponential(sleep_time: float = 0.05,
                    min_sleep_after_exc: float = 1.0, max_sleep_after_exc: float = 16.0) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    initial_sleep_time = sleep_time

    def wrapper(func) -> Callable[..., RT]:
        def inner(runs: int = 0, *args, **kwargs) -> RT:
            i = 0
            sleep_time = initial_sleep_time
            while True:
                try:
                    func(i, *args, **kwargs)
                except Exception as e:
                    if sleep_time < min_sleep_after_exc:
                        sleep_time = min_sleep_after_exc
                    elif sleep_time < max_sleep_after_exc:
                        sleep_time *= 2
                else:
                    i += 1
                    sleep_time = initial_sleep_time
                if runs != 0 and i >= runs:
                    break
                time.sleep(sleep_time)
        return inner
    return wrapper
