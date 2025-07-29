import string
from collections import deque

def least_steps_to_transform_string(start,end,production_sequence):
    letters = list(string.ascii_lowercase)
    visited = set()
    queue = deque([(start, 0)])  # (current string, steps)
    visited.add(start)
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for s in current:
            for letter in letters:
                next_string = current.replace(s, letter, 1)
                if next_string in production_sequence and next_string not in visited:
                    visited.add(next_string)
                    queue.append((next_string, steps + 1))
    return -1  # If no transformation is possible





print(least_steps_to_transform_string("cat","dog",["bat","cot","dog","dag","dot","cat"]))