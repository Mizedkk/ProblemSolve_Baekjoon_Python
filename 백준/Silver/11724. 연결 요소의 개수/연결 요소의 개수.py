import sys


def main():
    node_num, iter_num = map(int, sys.stdin.readline().split())
    node_case = [[0] * node_num for _ in range(node_num)]
    for _ in range(iter_num):
        node1, node2 = map(lambda x: x - 1, map(int, sys.stdin.readline().split()))
        node_case[node1][node2] = node_case[node2][node1] = 1

    answer = 0
    node_chk = [False] * node_num

    def dfs(num):
        for nxt in range(node_num):
            if node_case[num][nxt] and not node_chk[nxt]:
                node_chk[nxt] = True
                dfs(nxt)

    for i in range(node_num):
        if not node_chk[i]:
            answer += 1
            node_chk[i] = True
            dfs(i)

    print(answer)


if __name__ == "__main__":
    main()
