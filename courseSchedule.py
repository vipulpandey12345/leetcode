from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connections = defaultdict(list) #storing a node and all outgoing connections
        numCourseConnections = defaultdict(int)
        visited = set()
        queue = []
        for i in range(0,numCourses):
            numCourseConnections[i] = 0
            
        for course,prereq in prerequisites:
            connections[prereq].append(course)
            numCourseConnections[course] += 1
        for key in numCourseConnections.keys():
            if numCourseConnections[key] == 0:
                queue.append(key)
        while len(queue) != 0:
            current_course = queue.pop()
            if current_course in visited:
                continue
            else:
                visited.add(current_course)
            for neighbor in connections[current_course]:
                numCourseConnections[neighbor] -= 1
                if numCourseConnections[neighbor] == 0:
                    queue.append(neighbor)
        return len(visited) == numCourses
