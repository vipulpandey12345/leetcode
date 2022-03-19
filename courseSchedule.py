from collections import defaultdict
def numCourses(prerequisites, numCourses):
  connections = defaultdict(list) #storing a node and all outgoing connections
  numCourseConnections = defaultdict(int)#storing a counter for the number of connections
  for course, prereq in range(len(prerequisites)):
    connections[prereq].append(course)
    numCourseConnections[course] += 1
  queue = []
  for key in numCourseConnections.keys():
    if numCourseConnections[key] == 0:
      queue.append(key)
  visited = set()
  while len(queue) != 0:
    first_position = queue.pop()
    visited.add(first_position)
    for neighbor in connections[first_position]:
      numCourseConnections[j] -= 1
      if numCourseConnections[j] == 0 and neighbor not in visited:
        queue.append(j)
  return len(visited) == NumCourses
