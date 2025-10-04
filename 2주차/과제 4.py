import time

def fib(n) :
    if n <= 2:      # F(1)=F(2)=1 가정
        return 1
    a, b = 1, 1     # a=F(1), b=F(2)
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

start = time.time()
k = fib(50)
end = time.time()
print(f"fib(50) 값: {k}")
print(f"걸린 시간: {end - start:.2f} 초")
