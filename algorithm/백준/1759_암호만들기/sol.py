import sys
sys.stdin = open('input.txt')

vowel = ['a','e','i','o','u']

def Word(d,result,s):
    if len(result)==L:
        count = 0
        for i in result:
            if i in vowel:
                count += 1
        if count >= 1 and L-count >= 2:
            print( "".join(result))
        return

    for i in range(s,C):
        result.append(password[i])
        s = i
        Word(d+1,result,s+1)
        result.remove(password[i])


L, C = map(int, input().split())
password = input().split()
password.sort()
result = []
Word(0, result, 0)
