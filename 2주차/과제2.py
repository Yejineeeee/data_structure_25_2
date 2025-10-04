# 수열 an=2an-1 – 10의 n번째 항을 구하는 재귀 알고리즘

def seq(n):
    if n == 0:
        return 1
    else : 
        return 2*seq(n-1) - 10

print(seq(100))

