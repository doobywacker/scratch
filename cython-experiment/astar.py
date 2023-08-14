import numpy as np


def test(grid: np.ndarray) -> np.float32:
    x_size = grid.shape[1]
    y_size = grid.shape[0]
    result = 0

    # x_order = range(x_size)
    # y_order = range(y_size)
    # np.random.shuffle(x_order)
    # np.random.shuffle(y_order)
    for x in range(x_size):
        for y in range(y_size):
            if grid[(y, x)] > result:
                result = grid[(y, x)]
    return result
