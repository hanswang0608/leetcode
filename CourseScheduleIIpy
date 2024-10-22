class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        cycle = set()
        ans = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(course):
            if course in visited and course in cycle:
                return True
            elif course in visited:
                return False
            visited.add(course)
            cycle.add(course)
            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True
            cycle.remove(course)
            ans.append(course)
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return []
        return ans