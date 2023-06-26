class Solution:
    # Function to insert element into the queue
    def insert(self, q, k):
        #code here
        q.append(k)

        
    # Function to find frequency of an element
    # return the frequency of k
    def findFrequency(self, q, k):
        # code here
        return q.count(k)