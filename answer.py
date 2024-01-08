def sequence(numn):
    if numn == 1:
        return 1
    if numn == 2:
        return 19/6
    return (1/numn)*(1 + sequence(numn - 1))  +(1 - 1/numn)* (sequence(numn - 2) + 1)

print([sequence(item) for item in range(1,7)])    