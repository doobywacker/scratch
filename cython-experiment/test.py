from timeit import timeit

import numpy as np

import astar
import astarx

grid_size = (100, 155)
numits = 1000

print("")
print("running tests")

grid = np.array(np.random.random(grid_size), dtype=np.float32)
# print("input data:")
# print(grid)

time = timeit(lambda: astar.test(grid), number=numits)
timex = timeit(lambda: astarx.test(grid), number=numits)

print(f"astar.test(): {time}")
print(f"astarx.test(): {timex}")
