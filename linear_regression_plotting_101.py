import numpy as np
import matplotlib.pyplot as plt


def generate_data(n=50, noise_scale=10):
    """Generate sample linear data with optional noise."""
    rng = np.random.default_rng(seed=42)
    x = np.arange(n)
    noise = rng.normal(scale=noise_scale, size=n)
    y = 3 * x + 4 + noise
    return x, y


def fit_line(x, y):
    """Fit a line y = m*x + b and return m and b."""
    m, b = np.polyfit(x, y, 1)
    return m, b


def plot_regression(x, y, m, b):
    """Plot the data and the fitted regression line."""
    plt.scatter(x, y, label="Data")
    plt.plot(x, m * x + b, color="red", label="Fitted line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Regression Example")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    x, y = generate_data()
    m, b = fit_line(x, y)
    plot_regression(x, y, m, b)


if __name__ == "__main__":
    main()
