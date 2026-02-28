from collections import deque


def moving_average(values: list[float], k: int) -> list[float]:
    result = []
    window = deque()
    window_sum = 0.0
    for val in values:
        window.append(val)
        window_sum += val
        if len(window) > k:
            window_sum -= window.popleft()
        result.append(window_sum / len(window))
    return result
