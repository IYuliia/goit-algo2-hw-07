from functools import lru_cache
import time
import random

CACHE_SIZE = 1000

N = 100000
array = [random.randint(1, 100) for _ in range(N)]

queries = [('Range', random.randint(0, N-1), random.randint(0, N-1)) for _ in range(25000)]
queries += [('Update', random.randint(0, N-1), random.randint(1, 100)) for _ in range(25000)]

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

@lru_cache(maxsize=CACHE_SIZE)
def range_sum_with_cache(L, R):
    return sum(array[L:R+1])

def update_with_cache(array, index, value):
    array[index] = value
    range_sum_with_cache.cache_clear()

def measure_execution_time(queries, use_cache=False):
    start_time = time.time()

    for query in queries:
        if query[0] == 'Range':
            L, R = query[1], query[2]
            if use_cache:
                result = range_sum_with_cache(L, R)
            else:
                result = range_sum_no_cache(array, L, R)

        elif query[0] == 'Update':
            index, value = query[1], query[2]
            if use_cache:
                update_with_cache(array, index, value)
            else:
                update_no_cache(array, index, value)

    end_time = time.time()
    return end_time - start_time

time_without_cache = measure_execution_time(queries, use_cache=False)
print(f"Time without cache: {time_without_cache:.2f} seconds")

time_with_cache = measure_execution_time(queries, use_cache=True)
print(f"Time with LRU cache: {time_with_cache:.2f} seconds")
