class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ingresses = [0] * numCourses
        adj = defaultdict(set)

        for dep, indep in prerequisites:
            ingresses[dep] += 1
            adj[indep].add(dep)

        que = deque([])
        ordering = []
        for i in range(numCourses):
            if ingresses[i] == 0:
                que.append(i)

        while que:
            node = que.popleft()
            ordering.append(node)
            for ad in adj[node]:
                ingresses[ad] -= 1
                if ingresses[ad] == 0:
                    que.append(ad)

        if len(ordering) == numCourses:
            return ordering
        return []