import time

def factorial_limit():
    start = time.time()
    result = 1
    n = 1

    while True:
        result *= n
        n += 1

        if time.time() - start >= 600:
            break

    end = time.time()
    print(f"10분 동안 계산된 n 값: {n-1}")
    print(f"걸린 시간: {end - start:.2f} 초")

factorial_limit()

