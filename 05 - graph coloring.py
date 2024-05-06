def is_safe(graph, color, v, colored):

  for i in range(len(graph[v])):
    if colored[i] == color and graph[v][i] == 1:
      return False
  return True

def backtrack(graph, m, colored, v, assignment):
 
  if v == len(graph):
    return True

  
  for c in range(1, m + 1):
    if is_safe(graph, c, v, colored):
      colored[v] = c  # Assign color
      assignment.append(c)  # Add assignment to track colors used

     
      if backtrack(graph, m, colored, v + 1, assignment):
        return True
      colored[v] = 0  # Un-assign color
      assignment.pop()  # Remove assignment

  return False

def minimum_color(graph):
  num_vertices = len(graph)
  result = float('inf')  # Initialize upper bound
  min_colors = 0  # Minimum colors found so far
  colored = [0] * num_vertices  # To store vertex colors
  assignment = []  # To track color assignments
  for m in range(1, num_vertices + 1):
    if backtrack(graph, m, colored, 0, assignment):
      result = min(result, m)  # Update upper bound if a solution is found
      min_colors = m  # Keep track of minimum colors found so far
      assignment.clear()  # Clear assignment for next iteration

  return min_colors, colored
graph = [
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [1, 0, 1, 0],
]

min_colors, colored = minimum_color(graph)

print("Minimum colors needed:", min_colors)
print("Coloring of vertices:", colored)
