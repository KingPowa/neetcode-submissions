class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = defaultdict(set)
        for dependent, indep in prerequisites:
            requirements[dependent].add(indep)
        
        def progressiveExploration(k, requirements, explored = set(), recursed = set()):
            if k in recursed:
                return False

            if k in explored:
                return True

            if k not in requirements:
                return True

            explored.add(k)
            recursed.add(k)
            
            for val in requirements[k]:
                no_cycle = progressiveExploration(val, requirements, explored, recursed)
                if not no_cycle: return False
            
            recursed.remove(k)
            return True

        visited = set()
        recursed = set()
        no_cycle = True
        for key in requirements:
            if key not in visited:
                no_cycle = no_cycle and progressiveExploration(key, requirements, visited, recursed)

        return no_cycle


