my_string = 'aaaaaaaa'
# from https://www.youtube.com/watch?v=_i4Yxeh5ceQ
print(my_string)
import numpy as np
def coder(string):
    answer = ''
    for item in string:
        answer = answer + str(ord(item) - 96)
    return answer
print(coder(my_string))

def counter_slow(string):
    if string == '':
        return 0
    num = int(string)
    if len(string) == 1 and num > 0:
        return 1
    if len(string) == 2 and num >9 and num < 27:
        return 1
    return counter_slow(string[1:]) + counter_slow(string[2:])
print(counter_slow(coder(my_string)))     
def counter_fast(string, memo = {}):
    if string in memo:
        return memo[string]
    if string == '' or string == '0':
        return 0
    num = int(string)
    if len(string) == 1 and num > 0:
        return 1
    if len(string) == 2 and num >9 and num < 27:
        return 1
    elif num < 10 and len(string) == 2:
        return 0
    slice = int(string[0:2])
    temp = 0
    if slice < 26:
        temp = counter_fast(string[2:], memo) 


    memo[string] =  counter_fast(string[1:], memo) + temp
    return memo[string]     
print(counter_fast(coder(my_string)))   
# but I want to see all the elemts in the list too
def lister(string, memo = {}):
    if string in memo:
        return memo[string]
    if string == '' or string == '0':
        memo[string] = [None]
        return memo[string]
    num = int(string)
    if len(string) == 1 and num > 0:
        memo[string] = [chr(num + 96)]
        return memo[string]
    if len(string) == 2 and num >9 and num < 27:
        memo[string] =     [chr(num + 96)]
        return memo[string]

    elif num < 10 and len(string) == 2:
        return None
        
    slice = int(string[0:2])
    temp = []
    if slice < 26:
        temp = lister(string[2:], memo) 
        thing1 = [chr(slice + 96) + item for item in temp]

    temp2 = lister(string[1:], memo)
    if temp2 == None:
        memo[string] = temp
    else:
        thing2 =   [chr(int(string[0:1]) + 96) + item for item in temp2]
    memo[string] = thing1 + thing2
    return memo[string]     
print(lister(coder(my_string)))   
# just for fnu, verification
temp = lister(coder(my_string))
print(len(temp))
print(set([coder(item) for item in temp]))
# best list can be just the smallest entry in the lister output.