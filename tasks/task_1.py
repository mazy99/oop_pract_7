#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import time

from sum_series import Series

if __name__ == "__main__":
    series = Series()

    print(series)

    start_time = time()
    s_numeric = series.calculate(num_threads=1)
    end_time = time()

    s_exact = series.ex_value()

    print("\nРезультаты вычислений:")
    print(f"Сумма ряда (численно)     = {s_numeric:.10f}")
    print(f"Контрольное значение y   = {s_exact:.10f}")
    print(f"Абсолютная погрешность   = {abs(s_numeric - s_exact):.2e}")
    print(f"Время вычисления (многопоточно) = {end_time - start_time:.6f} сек")
