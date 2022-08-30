"""Pseudo code:
Generate an initial solution x randomly
Generate a candidate solution y randomly based on current solution x and a specified neighbourhood structure
if x is better than y: 
    p = -(f(y) - f(x))) /t
    Generate r in [0, 1) randomly
if r < p: 
    x=y
if condition of inner loop is met:
    Decrease the temperature t
else: 
    break
if condition of outer loop is met:
    return x
else: 
    break
"""

"""In order to apply the SA algorithm to a specific problem, 
one must specify the neighbourhood structure and cooling schedule."""

"""These choices and their corresponding parameter
setting can have a significant impact on the SA's performance."""