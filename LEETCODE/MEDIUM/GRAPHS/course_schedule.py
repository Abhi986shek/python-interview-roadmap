"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0
    
    while queue:
        course = queue.popleft()
        count += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return count == num_courses


try:
    num_courses = int(input("ENTER NUMBER OF COURSES\n"))
    n = int(input("ENTER NUMBER OF PREREQUISITES\n"))
    prerequisites = []
    print("ENTER PREREQUISITES (course prereq):")
    for _ in range(n):
        a, b = map(int, input().split())
        prerequisites.append([a, b])
    print(f"CAN FINISH: {can_finish(num_courses, prerequisites)}")
except Exception as e:
    print(f"An error occurred: {e}")
