# -*- coding: utf-8 -*-
"""
Given a stack, the task is to sort it such that the top of the stack has
the greatest element.
"""

# Function to insert the value at correct position in stack
def insertion(stack, val):
    
    # Since top value must be highest, so insert value at position where
    # the value at its lower position is less than inserted value
    if not stack or val > stack[0]:
        
        stack.insert(0, val)
    
    else:
        
        tmp = stack.pop(0)
        
        insertion(stack, val)
        
        stack.insert(0, tmp)
    
    # Return updated stack
    return stack

# Function to sort the stack
def sorting(stack):
    
    # If stack is non empty, keep taking the top element out, then insert it
    # at its right position
    if stack:
        
        val = stack.pop(0)
        
        sorting(stack)
        
        insertion(stack, val)
    
    # Return sorted stack
    return stack

# The driver code
if __name__ == "__main__":
    
    # No of test cases
    t = int(input())
    
    for _ in range(t):
        
        # Number of elements in the stack
        n = int(input())
        
        # Input the stack
        stack = list(map(int, input().split()))
        
        # Sort the stack
        stack = sorting(stack)
        
        # Print the stack
        for i in range(n):
            
            print(stack.pop(0), end = " ")