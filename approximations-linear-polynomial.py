def linear_interpolation(x_vals, y_vals, x_interp):
    """
    Linear interpolation: estimates value between two known points
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y arrays must be of the same length.")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required for linear interpolation.")

    for i in range(len(x_vals) - 1):
        x0, x1 = x_vals[i], x_vals[i + 1]
        y0, y1 = y_vals[i], y_vals[i + 1]

        if x0 == x1:
            raise ZeroDivisionError(f"Duplicate X values detected at index {i} and {i + 1}.")

        if x0 <= x_interp <= x1 or x1 <= x_interp <= x0:  # Handle decreasing x
            return y0 + (x_interp - x0) * (y1 - y0) / (x1 - x0)

    raise ValueError("Interpolation point is out of bounds.")


def polynomial_interpolation(x_vals, y_vals, x_interp):
    """
    Polynomial interpolation using Lagrange method
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("X and Y arrays must be of the same length.")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required for polynomial interpolation.")
    if len(set(x_vals)) != len(x_vals):
        raise ValueError("Duplicate X values detected.")

    n = len(x_vals)
    result = 0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                denominator = x_vals[i] - x_vals[j]
                if denominator == 0:
                    raise ZeroDivisionError("Zero division due to duplicate X values.")
                term *= (x_interp - x_vals[j]) / denominator
        result += term
    return result


def main():
    # Define data table
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    # Point to interpolate
    x_interp = 2.5

    # Call interpolation functions with error handling
    try:
        y_linear = linear_interpolation(x, y, x_interp)
        print(f'Linear interpolation at x = {x_interp}: y ≈ {y_linear:.4f}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Linear interpolation error: {e}')
    except Exception as e:
        print(f'Unexpected error in linear interpolation: {e}')

    try:
        y_poly = polynomial_interpolation(x, y, x_interp)
        print(f'Polynomial interpolation at x = {x_interp}: y ≈ {y_poly:.4f}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Polynomial interpolation error: {e}')
    except Exception as e:
        print(f'Unexpected error in polynomial interpolation: {e}')


if __name__ == "__main__":
    main()