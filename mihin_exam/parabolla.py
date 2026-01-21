import numpy as np
import matplotlib.pyplot as plt


def parabolic_regression_analysis():
    """
    Анализ параболической регрессии по 10 точкам данных - СТРОГАЯ СТРУКТУРА
    """
    print("=" * 80)
    print("АНАЛИЗ ПАРАБОЛИЧЕСКОЙ РЕГРЕССИИ - ПО МЕТОДИКЕ ИЗ ЛЕКЦИИ")
    print("=" * 80)

    # 1. Ввод данных
    print("\n1. ВХОДНЫЕ ДАННЫЕ")
    print("-" * 80)

    X = np.array([1, 2, 2, 3, 3, 4, 4, 4, 5, 6], dtype=float)
    Y = np.array([1, 1, 2, 3, 4, 3, 4, 5, 4, 4], dtype=float)

    n = len(X)
    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"n = {n} (количество экспериментальных точек)")

    # 2. Вывод системы уравнений в общем виде
    print("\n2. ВЫВОД СИСТЕМЫ УРАВНЕНИЙ В ОБЩЕМ ВИДЕ")
    print("-" * 80)

    print("\nФункция суммарной ошибки:")
    print("F(A₀, A₁, A₂) = Σ(Yᵢ - A₀ - A₁·Xᵢ - A₂·Xᵢ²)²")

    print("\nУсловия минимума (частные производные):")
    print("∂F/∂A₀ = -2 Σ(Yᵢ - A₀ - A₁·Xᵢ - A₂·Xᵢ²) = 0")
    print("∂F/∂A₁ = -2 Σ[Xᵢ·(Yᵢ - A₀ - A₁·Xᵢ - A₂·Xᵢ²)] = 0")
    print("∂F/∂A₂ = -2 Σ[Xᵢ²·(Yᵢ - A₀ - A₁·Xᵢ - A₂·Xᵢ²)] = 0")

    print("\nПосле деления на -2 и раскрытия сумм:")
    print("ΣYᵢ = n·A₀ + A₁·ΣXᵢ + A₂·ΣXᵢ²")
    print("ΣXᵢYᵢ = A₀·ΣXᵢ + A₁·ΣXᵢ² + A₂·ΣXᵢ³")
    print("ΣXᵢ²Yᵢ = A₀·ΣXᵢ² + A₁·ΣXᵢ³ + A₂·ΣXᵢ⁴")

    print("\nСистема нормальных уравнений:")
    print("⎧ n·A₀ + ΣX·A₁ + ΣX²·A₂ = ΣY")
    print("⎪ ΣX·A₀ + ΣX²·A₁ + ΣX³·A₂ = ΣXY")
    print("⎩ ΣX²·A₀ + ΣX³·A₁ + ΣX⁴·A₂ = ΣX²Y")

    # 3. Вывод определителей в общем виде (по Крамеру)
    print("\n3. РЕШЕНИЕ СИСТЕМЫ В ОБЩЕМ ВИДЕ (ОПРЕДЕЛИТЕЛИ ПО КРАМЕРУ)")
    print("-" * 80)

    print("\nМатричная форма системы:")
    print("⎡ n      ΣX     ΣX² ⎤ ⎡ A₀ ⎤   ⎡ ΣY   ⎤")
    print("⎢ ΣX     ΣX²    ΣX³ ⎥ ⎢ A₁ ⎥ = ⎢ ΣXY  ⎥")
    print("⎣ ΣX²    ΣX³    ΣX⁴ ⎦ ⎣ A₂ ⎦   ⎣ ΣX²Y ⎦")

    print("\nГлавный определитель (Δ):")
    print("Δ = det ⎡ n      ΣX     ΣX² ⎤")
    print("        ⎢ ΣX     ΣX²    ΣX³ ⎥")
    print("        ⎣ ΣX²    ΣX³    ΣX⁴ ⎦")

    print("\nРаскрытие определителя Δ:")
    print("Δ = n·(ΣX²·ΣX⁴ - (ΣX³)²)")
    print("  - ΣX·(ΣX·ΣX⁴ - ΣX²·ΣX³)")
    print("  + ΣX²·(ΣX·ΣX³ - (ΣX²)²)")

    print("\nОпределитель для A₀ (Δ₀) — замена 1-го столбца на [ΣY, ΣXY, ΣX²Y]ᵀ:")
    print("Δ₀ = ΣY·(ΣX²·ΣX⁴ - (ΣX³)²)")
    print("    - ΣX·(ΣXY·ΣX⁴ - ΣX²Y·ΣX³)")
    print("    + ΣX²·(ΣXY·ΣX³ - ΣX²Y·ΣX²)")

    print("\nОпределитель для A₁ (Δ₁) — замена 2-го столбца:")
    print("Δ₁ = n·(ΣXY·ΣX⁴ - ΣX²Y·ΣX³)")
    print("    - ΣY·(ΣX·ΣX⁴ - ΣX²·ΣX³)")
    print("    + ΣX²·(ΣX·ΣX²Y - ΣX²·ΣXY)")

    print("\nОпределитель для A₂ (Δ₂) — замена 3-го столбца:")
    print("Δ₂ = n·(ΣX²·ΣX²Y - ΣX³·ΣXY)")
    print("    - ΣX·(ΣX·ΣX²Y - ΣX²·ΣXY)")
    print("    + ΣY·(ΣX·ΣX³ - (ΣX²)²)")

    print("\nФормулы коэффициентов:")
    print("A₀ = Δ₀ / Δ")
    print("A₁ = Δ₁ / Δ")
    print("A₂ = Δ₂ / Δ")

    # 4. Таблица расчётов
    print("\n4. ТАБЛИЦА РАСЧЕТОВ")
    print("-" * 80)
    print(" i |   Xᵢ   |   Yᵢ   |   Xᵢ²   |   Xᵢ³   |   Xᵢ⁴   |   Xᵢ·Yᵢ   |   Xᵢ²·Yᵢ")
    print("-" * 70)

    sum_X, sum_Y, sum_X2, sum_X3, sum_X4, sum_XY, sum_X2Y = 0, 0, 0, 0, 0, 0, 0

    for i in range(n):
        xi = X[i]
        yi = Y[i]
        xi2 = xi ** 2
        xi3 = xi ** 3
        xi4 = xi ** 4
        xiyi = xi * yi
        xi2yi = xi2 * yi

        sum_X += xi
        sum_Y += yi
        sum_X2 += xi2
        sum_X3 += xi3
        sum_X4 += xi4
        sum_XY += xiyi
        sum_X2Y += xi2yi

        print(f"{i + 1:2d} | {xi:6.1f} | {yi:6.1f} | {xi2:7.1f} | {xi3:7.1f} | {xi4:7.1f} | {xiyi:9.1f} | {xi2yi:9.1f}")

    print("-" * 70)
    print(f" Σ | {sum_X:6.1f} | {sum_Y:6.1f} | {sum_X2:7.1f} | {sum_X3:7.1f} | {sum_X4:7.1f} | {sum_XY:9.1f} | {sum_X2Y:9.1f}")

    # 5. Численное решение системы
    print("\n5. ЧИСЛЕННОЕ РЕШЕНИЕ СИСТЕМЫ")
    print("-" * 80)

    M = np.array([
        [n,      sum_X,   sum_X2],
        [sum_X,  sum_X2,  sum_X3],
        [sum_X2, sum_X3,  sum_X4]
    ], dtype=float)

    B = np.array([sum_Y, sum_XY, sum_X2Y], dtype=float)

    print("\nМатрица системы M:")
    print(M)
    print("\nВектор правой части B:")
    print(B)

    try:
        A = np.linalg.solve(M, B)
        A0, A1, A2 = A
    except np.linalg.LinAlgError:
        print("Ошибка: система вырождена!")
        return

    print(f"\nРешение системы:")
    print(f"A₀ = {A0:.6f}")
    print(f"A₁ = {A1:.6f}")
    print(f"A₂ = {A2:.6f}")

    print(f"\nУравнение параболической регрессии:")
    print(f"Y = {A2:.6f}·X² + {A1:.6f}·X + {A0:.6f}")

    # 6. Расчёт ошибок и стандартного отклонения
    print("\n6. РАСЧЕТ ОШИБОК И СТАНДАРТНОГО ОТКЛОНЕНИЯ")
    print("-" * 80)

    Y_theor = A2 * X**2 + A1 * X + A0
    E = Y - Y_theor
    E2 = E ** 2

    print("\nТаблица расчетов ошибок:")
    print(" i |   Xᵢ   |   Yᵢ   |  Yᵢтеор  |   Eᵢ = Yᵢ-Yᵢтеор   |   Eᵢ²   ")
    print("-" * 70)

    for i in range(n):
        print(f"{i + 1:2d} | {X[i]:6.1f} | {Y[i]:6.1f} | {Y_theor[i]:8.4f} | {E[i]:18.6f} | {E2[i]:9.6f}")

    print("-" * 70)
    sum_E = np.sum(E)
    sum_E2 = np.sum(E2)
    print(f" Σ | {' ':6} | {' ':6} | {' ':8} | {sum_E:18.6f} | {sum_E2:9.6f}")

    print(f"\nСуммарная ошибка F = ΣEᵢ² = {sum_E2:.6f}")

    sigma = np.sqrt(sum_E2 / n)
    print(f"\nСтандартное отклонение:")
    print(f"σ = √(F/n) = √({sum_E2:.6f}/{n}) = √{sum_E2 / n:.6f} = {sigma:.6f}")

    # 7. Расчёт ширины полосы S
    print("\n7. РАСЧЕТ ШИРИНЫ ПОЛОСЫ S")
    print("-" * 80)

    X_mid = (np.min(X) + np.max(X)) / 2
    dY_dX_mid = A1 + 2 * A2 * X_mid
    angle_rad = np.arctan(dY_dX_mid)
    angle_deg = np.degrees(angle_rad)
    beta = 90 - angle_deg
    beta_rad = np.radians(beta)
    sin_beta = np.sin(beta_rad)

    print(f"Расчёт угла наклона в середине диапазона X = {X_mid:.2f}:")
    print(f"dY/dX = A₁ + 2·A₂·X = {A1:.6f} + 2·{A2:.6f}·{X_mid:.2f} = {dY_dX_mid:.6f}")
    print(f"α = arctan(dY/dX) = arctan({dY_dX_mid:.6f}) = {angle_deg:.2f}°")
    print(f"β = 90° - α = {beta:.2f}°")
    print(f"sin(β) = {sin_beta:.6f}")

    S = sigma / sin_beta
    print(f"\nШирина полосы S:")
    print(f"S = σ/sin(β) = {sigma:.6f}/{sin_beta:.6f} = {S:.6f}")

    # 8. Доверительные границы
    print("\n8. ОПРЕДЕЛЕНИЕ ДОВЕРИТЕЛЬНЫХ ГРАНИЦ")
    print("-" * 80)

    Y_upper_S = Y_theor + S
    Y_lower_S = Y_theor - S
    Y_upper_2S = Y_theor + 2 * S
    Y_lower_2S = Y_theor - 2 * S

    print("\nДоверительные границы для каждой точки (полоса ±S):")
    print(" i |   Yᵢ   |  Yтеор  | Yтеор-S | Yтеор+S | В полосе?")
    print("-" * 65)

    points_in_S = 0
    for i in range(n):
        in_S = Y_lower_S[i] <= Y[i] <= Y_upper_S[i]
        if in_S:
            points_in_S += 1
        symbol = "✓" if in_S else "✗"
        print(f"{i + 1:2d} | {Y[i]:6.1f} | {Y_theor[i]:7.3f} | {Y_lower_S[i]:7.3f} | {Y_upper_S[i]:7.3f} |   {symbol}")

    points_in_2S = sum((Y >= Y_lower_2S) & (Y <= Y_upper_2S))

    # 9. Проверка гипотезы
    print("\n9. ПРОВЕРКА ГИПОТЕЗЫ")
    print("-" * 80)

    percentage_S = (points_in_S / n) * 100
    percentage_2S = (points_in_2S / n) * 100

    print(f"Точек в полосе Yтеор ± S: {points_in_S} из {n} = {percentage_S:.2f}%")
    print(f"Точек в полосе Yтеор ± 2S: {points_in_2S} из {n} = {percentage_2S:.2f}%")

    print(f"\nКритерии принятия гипотезы:")
    print("- Если ≥68.26% точек в полосе Yтеор ± S → гипотеза принимается")
    print("- Если ≥95.44% точек в полосе Yтеор ± 2S → дополнительная уверенность")

    print(f"\nРезультат:")
    if percentage_S >= 68.26:
        print(f"✓ {percentage_S:.2f}% ≥ 68.26% → ГИПОТЕЗА ПРИНЯТА")
    else:
        print(f"✗ {percentage_S:.2f}% < 68.26% → гипотеза отклонена")

    if percentage_S >= 68.26:
        if percentage_2S >= 95.44:
            print(f"✓ {percentage_2S:.2f}% ≥ 95.44% → высокая уверенность в результате")
        else:
            print(f"→ умеренная уверенность в результате")

    # 10. График
    print("\n10. ГРАФИЧЕСКОЕ ПРЕДСТАВЛЕНИЕ")
    print("-" * 80)

    plt.figure(figsize=(12, 8))

    x_line = np.linspace(min(X) - 1, max(X) + 1, 200)
    y_line = A2 * x_line**2 + A1 * x_line + A0
    y_upper_S_line = y_line + S
    y_lower_S_line = y_line - S
    y_upper_2S_line = y_line + 2 * S
    y_lower_2S_line = y_line - 2 * S

    plt.fill_between(x_line, y_lower_2S_line, y_upper_2S_line,
                     alpha=0.1, color='yellow', label='Полоса Yтеор ± 2S')
    plt.fill_between(x_line, y_lower_S_line, y_upper_S_line,
                     alpha=0.3, color='lightgreen', label=f'Полоса Yтеор ± S (S={S:.3f})')

    plt.plot(x_line, y_line, 'r-', linewidth=3, label=f'Y = {A2:.3f}X² + {A1:.3f}X + {A0:.3f}')
    plt.scatter(X, Y, color='blue', s=100, zorder=5, label='Экспериментальные точки')

    plt.plot(x_line, y_upper_S_line, 'g--', linewidth=1, alpha=0.7, label='Yтеор + S')
    plt.plot(x_line, y_lower_S_line, 'g--', linewidth=1, alpha=0.7, label='Yтеор - S')

    plt.xlabel('X (вход)', fontsize=12)
    plt.ylabel('Y (выход)', fontsize=12)
    plt.title('Параболическая регрессия с доверительными полосами ±S и ±2S', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')

    info_text = f'Y = {A2:.3f}X² + {A1:.3f}X + {A0:.3f}\n'
    info_text += f'σ = {sigma:.3f}\n'
    info_text += f'S = {S:.3f}\n'
    info_text += f'Точек в ±S: {points_in_S}/{n} ({percentage_S:.1f}%)\n'
    info_text += f'Точек в ±2S: {points_in_2S}/{n} ({percentage_2S:.1f}%)'

    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    for i, (x, y) in enumerate(zip(X, Y)):
        offset_x = 0.2 if i % 2 == 0 else -0.2
        plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points",
                     xytext=(offset_x * 15, 10), ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

    # 11. Итоговый вывод
    print("\n" + "=" * 80)
    print("ИТОГОВЫЙ ВЫВОД")
    print("=" * 80)

    print(f"\n1. Уравнение параболической регрессии:")
    print(f"   Y = {A2:.4f}·X² + {A1:.4f}·X + {A0:.4f}")

    print(f"\n2. Результаты расчёта:")
    print(f"   A₀ = {A0:.4f}")
    print(f"   A₁ = {A1:.4f}")
    print(f"   A₂ = {A2:.4f}")
    print(f"   F = ΣE² = {sum_E2:.4f}")
    print(f"   σ = √(F/n) = {sigma:.4f}")
    print(f"   S = σ/sin(β) = {S:.4f}")

    print(f"\n3. Проверка гипотезы о параболической модели:")
    print(f"   Точек в полосе Yтеор ± S: {points_in_S}/{n} ({percentage_S:.2f}%)")

    if percentage_S >= 68.26:
        print(f"   ✓ Гипотеза принята (параболическая модель адекватна)")
        print(f"   ✓ Точек в полосе Yтеор ± 2S: {points_in_2S}/{n} ({percentage_2S:.2f}%)")
        if percentage_2S >= 95.44:
            print(f"   ✓ Высокая уверенность в модели")
    else:
        print(f"   ✗ Гипотеза отклонена (возможно, нужна другая модель)")

    return {
        'A0': A0, 'A1': A1, 'A2': A2,
        'sigma': sigma, 'S': S,
        'points_in_S': points_in_S, 'points_in_2S': points_in_2S,
        'percentage_S': percentage_S, 'percentage_2S': percentage_2S
    }


# Запуск анализа
if __name__ == "__main__":
    results = parabolic_regression_analysis()

    print("\n" + "=" * 80)
    print("ПРИМЕР ПРОГНОЗИРОВАНИЯ")
    print("=" * 80)

    print(f"\nИспользуем модель для прогноза:")
    print(f"Модель: Y = {results['A2']:.4f}·X² + {results['A1']:.4f}·X + {results['A0']:.4f}")

    print("\nПрогноз с доверительными интервалами:")
    print(" X  |  Yпрогноз  |  Доверительный интервал (±S)")
    print("-" * 55)

    for x in [0, 5, 11, 15, 20]:
        y_pred = results['A2'] * x**2 + results['A1'] * x + results['A0']
        y_lower = y_pred - results['S']
        y_upper = y_pred + results['S']
        print(f"{x:3.0f} | {y_pred:10.4f} | [{y_lower:7.4f}, {y_upper:7.4f}]")