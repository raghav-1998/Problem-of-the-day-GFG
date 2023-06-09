**Topological sort** ==>

Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

**Example 1:**

Input:

![image](https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700255/Web/Other/24aa5d54-bc1f-489c-bd2d-ad02ddccdf31_1684492511.png)

Output:1

Explanation:
The output 1 denotes that the order is valid. So, if you have, implemented your function correctly, then output would be 1 for all test cases. One possible Topological order for the graph is 3, 2, 1, 0.

**Example 2:**

Input:

![image](https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700255/Web/Other/c35bb1d1-130c-49aa-a17e-118181d7bdcd_1684492512.png)

Output: 1

Explanation:
The output 1 denotes that the order is valid. So, if you have, implemented your function correctly, then output would be 1 for all test cases. One possible Topological order for the graph is 5, 4, 2, 1, 3, 0.

**Your Task**:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

**Expected Time Complexity**: O(V + E).

**Expected Auxiliary Space**: O(V).

**Constraints**:
2 ≤ V ≤ 10^4
1 ≤ E ≤ (N*(N-1))/2