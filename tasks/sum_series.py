#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread


class Series:

    def __init__(self, x: float = 1.2, eps: float = 10 ** (-7)) -> None:
        self.x = x
        self.eps = eps

    def _term(self, n: int) -> float:
        return ((-1) ** n) * (self.x**n) / (2 ** (n + 1))

    def _worker(self, start: int, step: int, result_list: list, index: int) -> None:
        print(f"[Thread {index}] Старт")
        sum_local = 0.0
        n = start
        a_n = self._term(n)
        count = 0
        while abs(a_n) >= self.eps:
            sum_local += a_n
            n += step
            a_n = self._term(n)
            count += 1
        result_list[index] = sum_local
        print(f"[Thread {index}] Завершил. Посчитано членов ряда: {count}")

    def calculate(self, num_threads: int = 4) -> float:
        threads = []
        results = [0.0] * num_threads
        for i in range(num_threads):
            thread = Thread(target=self._worker, args=(i, num_threads, results, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return sum(results)

    def __str__(self) -> str:
        return (
            "Исходный ряд:\n"
            "S = Σ [(-1)^n * x^n / 2^(n+1)],  n = 0 .. ∞\n\n"
            f"Параметры:\n"
            f"x = {self.x}\n"
            f"epsilon = {self.eps}\n\n"
            "Аналитическое выражение суммы:\n"
            "S = 1 / (2 + x)"
        )

    def ex_value(self):
        return 1 / (2 + self.x)
