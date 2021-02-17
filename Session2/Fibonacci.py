def fib(n):
    series = [0, 1]
    for e in range(0, n-1):
        new = series[-1] + series[-2]
        series.append(new)
    return series

n = 10
for e in (fib(n)):
    print (e, end=' ')
print('\nThe last fibonacci term from the series is:', fib(n)[-1])

def fibosum(series, f):
    count = 0
    a = 0
    for e in series:
        count += e
        a += 1
        if a == f:
            break
    return count
print(fibosum(fib(n), 5))