import numpy as np

# EDO: y' = 1 + y, y(0) = 0
# Solución exacta: y(t) = e^t - 1

def f(t, y):
    return 1 + y

def euler(f, y0, t0, tf, h):
    N = int((tf - t0) / h)
    t_vals = [t0]
    y_vals = [y0]

    t = t0
    y = y0

    for n in range(N):
        y = y + h * f(t, y)
        t = t + h
        t_vals.append(t)
        y_vals.append(y)

    return np.array(t_vals), np.array(y_vals)

if __name__ == "__main__":
    t0 = 0.0
    tf = 1.0
    h = 0.2
    y0 = 0.0

    t_vals, y_euler = euler(f, y0, t0, tf, h)
    y_exact = np.exp(t_vals) - 1

    print("t\tEuler\t\tExacta")
    for t, ye, ye_ex in zip(t_vals, y_euler, y_exact):
        print(f"{t:.1f}\t{ye:.6f}\t{ye_ex:.6f}")
