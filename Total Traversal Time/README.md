**Total Traversal Time** ==>

Given two arrays arr[ ] and peanlty[ ], each of size n.
All elements in arr[ ] are in the range of 1 to n. You have to traverse arr[ ] from start to end while following the given conditions.

1. If element has never occured before, it takes 1 second to move a step ahead.
2. If element has occured before, it will take penalty[arr[i]] seconds to move a step. Here i is the index of current element with 1 based indexing.
Find the total time taken to traverse through the array

**Example 1**:

Input:n = 4 arr[ ] = {1, 2, 3, 3} penalty[ ] = {1, 2, 3, 4}

Output: 5

Explanation:

For i = 1, traversal time = 0 second since this is the start point.  
For i = 2, traversal time = 1 second 
For i = 3, traversal time = 1 second 
For i = 4, traversal time = penalty[arr[4]]  = penalty[3] = 3
Total = 0+1+1+3 = 5 

**Example 2**:

Input:n = 8 arr = {6, 6, 1, 8, 1, 1, 3, 1} time ={8, 4, 1, 5, 2, 8, 9, 3}

Output:35

**Your Task**:

You don't need to read input or print anything. Your task is to complete the function totalTime() which takes three input parameters n, arr[ ], penalty[ ] and returns the total time taken to traverse through the array. 

**Expected Time Complexity**: O(n)

**Expected Auxiliary Space**: O(n)

**Constraints**:

1 <= n <= 10^5
1 <= arr[i] <= n
1 <= time[i] <= 10^5
