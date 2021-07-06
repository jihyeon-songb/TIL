import sys
sys.stdin = open('input.txt')

def post_order(value):
    if root > value:
        if node[-1] > value:
            node.append(value)
        else:
            print(node.pop())
            print(value)
            if node[-2] == root:
                print(node.pop())
    else:
        if node[-1] > value:
            node.append(value)
        else:
            print(value)
            print(node.pop())
            if node[-2] == root:
                print(node.pop())

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

root = pre_order[0]
node = [root,]

for i in range(1,len(pre_order)):
    post_order(pre_order[i])
