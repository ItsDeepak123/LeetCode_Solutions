class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26
        new_parent = parent[:]

        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()
            ch = ord(s[node]) - ord('a')

            if state == 0:
                old = last[ch]

                if old != -1:
                    new_parent[node] = old

                last[ch] = node

                stack.append((node, 1, old))

                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                last[ch] = old

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n
        stack = [(0, False)]

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                for child in new_children[node]:
                    stack.append((child, False))

            else:
                for child in new_children[node]:
                    answer[node] += answer[child]

        return answer