# Required: Generate at random an array of n = 1,000 numbers using a PRNG in the range from 1 to n. 
# Build a BST on the array from left to right and compute the height of the BST. 
# Repeat this process for n times, what is the average height? 
# Note that the theoretical upper bound of the height of a BST built on n randomy generated numbers is log (n+3)(n+2)(n+1)/24, 
# where each number has an equal chance to become the root of the BST. 
# Is your result close to the threotical upper bound? Explain your answer. 
     
# Optional (50 bonus points): In the above, change the value range to 1 to 20 and compute the average height. 
# Is your average height about the same as that you obtained above? Explain why your result is what it is. 
 

import random
from math import log, floor

class BST(): # BST class

    def __init__(self, data=None): # constructor

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data): # function to insert values into the BST

        if self.data:
            if data < self.data: # comparing to current node
                if self.left is None:
                    self.left = BST(data) # if the given value is less than the node being compared, then add to left node if there is no left node
                else:
                    self.left.insert(data) # if there is a left node, then compare the inserted value to it
            elif data > self.data:
                if self.right is None:
                    self.right = BST(data) # if the given value is greater than the node being compared, then add to right node if there is no right node
                else:
                    self.right.insert(data) # if there is a right node, then compare the inserted value to it
        else:
            self.data = data

    def height(self, root): # recursive function to get height of BST
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

def get_stats(n): # prints the average height, maximum height and upper bound height for a BST of 'n' number of random numbers
    bst = BST()
    avg_height = []

    for _ in range(n): # running loop for n times

        arr = [random.choice(range(1, n+1)) for _ in range(n)] # generates an array of n random numbers from 1 to n
        for x in arr:
            bst.insert(x) # inserting into BST from left to right

        avg_height.append(bst.height(bst)) # calculate the height of this BST and append to an array

    print("For n = ",n)
    print("Average Height: ".format(n), floor(sum(avg_height)/n)) # calulates and prints average height of BSTs over the avg_height array
    print("Maximum Height: ", max(avg_height)) # prints maximum height

    upper_bound = log(((n+3)*(n+2)*(n+1))/24, 2) # calculates upper bound of height of BST with n random numbers (based on proof from CLRS)
    print("Upper bound is: ",floor(upper_bound))
    print("\n")

get_stats(1000) # for 1000 random numbers

# On running the above line, we get the average height always less than or equal to the upper bound.
# For 1000 random numbers, the upper bound is 25.
# It can be less than or equal to the upper bound as the tree can be a bit skewed due to the randomness of the numbers.


get_stats(20) # for 20 random numbers

# The upper bound for 20 random numbers is 8, and the average height is also less than or equal to it.
# The upper bound is lesser than the one for 1000 numbers as there are less numbers to fill the branches.
