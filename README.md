# Linear-Regression

This repository contains examples of simple linear regression techniques.

## What is Linear Regression?
Linear regression is a technique used to model the relationship between two quantitative variables. Given a set of points, we assume there is a line that best represents their trend. A common approach to finding that line is gradient descent, which iteratively adjusts an initial guess until the error is minimized.

## Basic Plotting Example
The file `linear_regression_plotting_101.py` generates sample data, fits a regression line, and plots the result. It requires `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
python3 linear_regression_plotting_101.py
```

Running the script will open a window displaying the scatter points and the fitted line.
