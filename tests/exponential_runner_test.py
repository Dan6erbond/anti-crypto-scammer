import random
from unittest import TestCase

from lib.exponential_runner import run_exponential


class TestExponentialRunner(TestCase):
    def test_exponential_runner(self):
        runs = 0
        max_runs = 10

        @run_exponential(min_sleep_after_exc=0.05, max_sleep_after_exc=1.0)
        def test_func():
            nonlocal runs
            runs += 1

        test_func(max_runs)

        self.assertEqual(runs, max_runs)

    def test_exponential_runner_exception(self):
        runs = 0
        max_runs = 10

        @run_exponential(min_sleep_after_exc=0.05, max_sleep_after_exc=1.0)
        def test_func():
            nonlocal runs
            if random.randint(0, 100) < 50:
                raise Exception("Test exception")
            runs += 1

        test_func(max_runs)

        self.assertEqual(runs, max_runs)
