def sequence_report(name, seq, n):
    print(" n | " + name + "(n)")
    print("-"*3 + "+" + "-"*(len(name)+5))
    i = 1
    while i <= n:
        print(" "+str(i)+" | "+str(seq(i)))
        i = i + 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]


    
