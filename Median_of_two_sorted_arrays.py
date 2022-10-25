class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        #merging the two list
        list = num1+num2
        n=len(list)
        
        #sorting the merged list
        list.sort()
        
        #find the middle element using similar binary search approach
        start=0
        end=n-1
        median=0
        if(len(list)%2==0): #if list has even number of elements
            mid=int((start+end)/2)
            median=(list[mid]+list[mid+1])/2
            return median
        else:
            mid=int((start+end)/2)
            median=list[mid]
            return median
