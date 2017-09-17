from multiprocessing import Pool
from time import time, sleep


def f(x):
    sleep(0.1)
    return x, x*x, x*x*x
if __name__ == "__main__":
    results = []
    start = time()
    for i in range(10):
        results.append(f(i))
    print(results)
    print('Seq:', time() - start, 's')

    pool = Pool(processes=4)

    results = []
    start = time()
    results = pool.map(f, list(range(10)))
    print(results)
    print(time() - start, 's')
