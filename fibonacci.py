def fibonacci_sequence(n):
    n1 = 0
    n2 = 1

    sequence = [n1, n2]
    i = 1
    while i < n:
        n3 = n2 + n1
        sequence.append(n1 + n2)
        n1 = n2
        n2 = n3
        i += 1
    return n3


print(fibonacci_sequence(20))
