import sys
sys.stdin = open('input.txt')


def make_tree(idx, i):
    if tree[idx][0] == 0:
        tree[idx][0] = pre_order[i]
        if idx%2:
            tree[idx//2][2] = idx
        else:
            tree[idx//2][1] = idx
        return

    elif tree[idx][0] > pre_order[i]:
        make_tree(idx*2, i)
    else:
        make_tree(idx*2+1, i)
    return 

def post_order(node):
    if tree[node][1]:
        post_order(tree[node][1])
    if tree[node][2]:
        post_order(tree[node][2])
    print(tree[node][0])

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

tree = [[0 for _ in range(3)] for _ in range(1000005)]

tree[1][0] = pre_order[0]
idx = 1

for i in range(1,len(pre_order)):
    make_tree(1, i)

post_order(1)
