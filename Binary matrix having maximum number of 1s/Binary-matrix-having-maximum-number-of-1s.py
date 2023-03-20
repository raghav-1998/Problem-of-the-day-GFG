#User function Template for python3

class Solution:

    def findMaxRow(self, mat, N):

        # Code here

        def binarysearch(arr):

            l=0

            r=N-1

            res=-1

            

            while l<=r:

                

                mid=l+((r-l)//2)

                

                if arr[mid]==1:

                    res=mid

                    r=mid-1

                else:

                    l=mid+1

            return res

        topa=float('-inf')

        for i in range(N):

            ans1=binarysearch(mat[i])

            if ans1==-1:

                ans1==0

                

            else:    

                ans1=N-(binarysearch(mat[i]))

            if ans1>topa:

                row=i

                

                topa=ans1

        if topa==-1:

            topa=0

        return [row,topa]