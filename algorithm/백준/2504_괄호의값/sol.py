import sys
sys.stdin = open('input.txt')

b_list = list(input())
blanket = [')':'(', ']':'[']

op_list = []
stack = []
for i in b_list:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')':
        if stack[-1] == '(':
            if i+1   
    
