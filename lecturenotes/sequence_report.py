def sequence_report(name, seq, n):
    print(" n | " + name + "(n)")
    print("-"*3 + "+" + "-"*(len(name)+5))
    i = 1
    while i <= n:
        print(" "+str(i)+" | "+str(seq(i)))
        i = i + 1
