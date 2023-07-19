def f(a, b, m, t):
    if a > 45 or b > 45:
        return 0

    if a + b > 54:
        return m % 2 == 0

    if m == 0:
        return 0

    h = (f(a * 2 - 1, b - 1, m - 1, t), f(a + 3, b - 1, m - 1, t), f(a + 2, b - 1, m - 1, t),
         f(a - 1, b * 2 - 1, m - 1, t), f(a - 1, b + 3, m - 1, t), f(a - 1, b + 2, m - 1, t))

    return all(h) if m % 2 == 0 and t != 19 else any(h)


print('19.', len([s for s in range(1, 51) if f(20, s, 2, 19)]))
print('20.', [s for s in range(1, 51) if f(20, s, 3, 20) and not f(20, s, 1, 20)])
print('21.', [s for s in range(1, 51) if f(20, s, 4, 21) and not f(20, s, 2, 21)])
