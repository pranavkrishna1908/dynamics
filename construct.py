def canconstruct(target , bank):
    if target == '':
        return 1
    for item in bank:
        if target.startswith(item):
            return canconstruct(target[len(item)+ 1:], bank)
print(canconstruct('appagapa', ['a', 'p']))        
