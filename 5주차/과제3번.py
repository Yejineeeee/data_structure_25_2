import time

def sample(n):
    start = time.perf_counter()
    s = 0
    for i in range(n):
        for j in range(n):
            s += (i + j) & 1 
    end = time.perf_counter()
    return s, end - start

# 측정
sizes = [100, 1_000, 10_000]
prev_n, prev_t = None, None
for n in sizes:
    _, t = sample(n)
    print(f"n={n:>6} | time={t:.6f}s")
    if prev_t is not None:
        print(f"  비율 T({n})/T({prev_n}) ≈ {t/prev_t:.2f} (이론 {(n/prev_n)**2:.0f})")
    prev_n, prev_t = n, t