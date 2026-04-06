"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.
"""

from collections import defaultdict
from math import gcd

def max_points(points):
    if len(points) <= 2:
        return len(points)
    
    max_count = 0
    
    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicate = 1
        
        for j in range(i + 1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            
            if dx == 0 and dy == 0:
                duplicate += 1
                continue
            
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            
            if dx < 0:
                dx, dy = -dx, -dy
            
            slopes[(dx, dy)] += 1
        
        max_count = max(max_count, duplicate + (max(slopes.values()) if slopes else 0))
    
    return max_count


try:
    n = int(input("ENTER NUMBER OF POINTS\n"))
    points = []
    print("ENTER POINTS (x y):")
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    print(f"MAX POINTS ON LINE: {max_points(points)}")
except Exception as e:
    print(f"An error occurred: {e}")
