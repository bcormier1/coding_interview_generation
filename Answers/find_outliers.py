def _percentile(sorted_data: list[float], p: float) -> float:
    """Compute percentile using linear interpolation (matches numpy default)."""
    n = len(sorted_data)
    idx = p / 100 * (n - 1)
    lo = int(idx)
    hi = lo + 1
    frac = idx - lo
    if hi >= n:
        return sorted_data[lo]
    return sorted_data[lo] + frac * (sorted_data[hi] - sorted_data[lo])


def find_outliers(values: list[float]) -> list[float]:
    sorted_vals = sorted(values)
    q1 = _percentile(sorted_vals, 25)
    q3 = _percentile(sorted_vals, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [v for v in values if v < lower or v > upper]
