import time

def fib(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)

start = time.time()
k = fib(50)
end = time.time()
print(f"fib(50) 값: {k}")
print(f"걸린 시간: {end - start:.2f} 초")
