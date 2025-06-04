"""Example script that plots a simple linear regression fit.

The goal of this file is to show how to generate some sample data,
fit a line using NumPy, and display the resulting plot with Matplotlib.
Each step is heavily commented for clarity.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(n: int = 50, noise_scale: float = 10):
    """Generate sample linear data with optional noise.

    Parameters
    ----------
    n : int
        Number of data points to create.
    noise_scale : float
        Standard deviation of the Gaussian noise added to the points.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Arrays of ``x`` and ``y`` values following roughly a line.
    """
    rng = np.random.default_rng(seed=42)  # deterministic random numbers
    x = np.arange(n)                       # feature values 0, 1, 2, ...
    noise = rng.normal(scale=noise_scale, size=n)  # random perturbation
    y = 3 * x + 4 + noise                  # linear relation with noise
    return x, y


def fit_line(x: np.ndarray, y: np.ndarray):
    """Fit a line ``y = m*x + b`` using least squares.

    Parameters
    ----------
    x : np.ndarray
        Input feature array.
    y : np.ndarray
        Target values corresponding to ``x``.

    Returns
    -------
    Tuple[float, float]
        The slope ``m`` and intercept ``b`` of the fitted line.
    """
    # NumPy's polyfit returns coefficients for a polynomial of given degree.
    m, b = np.polyfit(x, y, 1)  # degree 1 -> straight line
    return m, b


def plot_regression(x: np.ndarray, y: np.ndarray, m: float, b: float):
    """Display the data points and their fitted regression line."""
    plt.scatter(x, y, label="Data")        # draw the sample points
    plt.plot(x, m * x + b, color="red", label="Fitted line")  # plot y = mx + b
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Regression Example")
    plt.legend()
    plt.tight_layout()                      # ensure labels fit in the figure
    plt.show()


def main() -> None:
    """Generate data, fit a line, and plot the result."""
    x, y = generate_data()       # create a noisy linear dataset
    m, b = fit_line(x, y)        # find the slope and intercept
    plot_regression(x, y, m, b)  # visualize the regression


# Run the example when executed as a script
if __name__ == "__main__":
    main()
