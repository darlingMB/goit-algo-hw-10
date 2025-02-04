import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2

def monte_carlo_integration(f, a, b, n=100000):
    """Обчислення інтеграла методом Монте-Карло"""
    x_random = np.random.uniform(a, b, n)
    y_random = f(x_random)

    integral_mc = (b - a) * np.mean(y_random)

    return integral_mc

def plot_function_and_points(f, a, b, x_random, y_random):
    """Побудова графіка функції та випадкових точок"""
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.1)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 от ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def main():
    a = 0
    b = 2
    n = 100000

    integral_mc = monte_carlo_integration(f, a, b, n)
    x_random = np.random.uniform(a, b, n)
    y_random = f(x_random)

    plot_function_and_points(f, a, b, x_random, y_random)
    result, error = spi.quad(f, a, b)

    print(f"Наближене значення інтеграла методом Монте-Карло: {integral_mc}")
    print(f"Точне значення інтегралу: {result}")
    print(f"Оцінка похибки: {error}")

if __name__ == "__main__":
    main()
