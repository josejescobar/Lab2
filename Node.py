"""
Created on Mon Oct 29 22:02:23 2018

@author: Jose Escobar
STILL WORKING!
"""

class Node(object): 
    password =  ""   
    count = - 1
    next =  None
    
    def   __init__ ( self , password, count, next):  
        self.password = password
        self.count = count
        self.next = next
        

    def solutionA(node, code):
        while node is not None:
            if node.password is code:
                node.count += 1
                return True
        return False


    def solutionB(dic, pass_code):
        if pass_code in dic.keys():
            dic[pass_code] += 1 
            return True
        return False
            

##Bubble Sort: 
    def is_sorted(x): 
        if x is None or x.next is not None:
            return True
        if x.password > x.next.password:
            return False
    
        is_sorted(x.next)
        return True

    def bubbleSort(bubble):
        if bubble is not None and bubble.next is None:
            return bubble
        if bubble.password > bubble.next.password:
            temp = bubble.password
            bubble.password = bubble.next.password
            bubble.next.password = temp
            bubbleSort(bubble, bubble.next)
        if not is_sorted(bubble): 
            bubble = bubble.next
            bubbleSort(bubble, bubble.next)
        return bubble


##Merge Sort:
    def list_length(length):
        count = 0
        while length is not None:
            count += 1 
            length = length.next
        return count
        
    def mergeSort(bubbleMerge):
        mergeSort = bubbleMerge
        if bubbleMerge is None or bubbleMerge.next is None:
            return bubbleMerge
        length = list_length(bubbleMerge)
        for i in range(int(length/2) - 1): #    Half link list 
            mergeSort = mergeSort.next
            right = mergeSort.next
            mergeSort.next = None
            left = bubbleMerge
    
        leftSide = mergeSort(left)
        rightSide = mergeSort(right)
    
        complete_sort = None
        if leftSide.password > rightSide.password:
            complete_sort = leftSide
            leftSide = leftSide.next
        else:
            complete_sort = rightSide
            rightSide = rightSide.next
        head = complete_sort
        while leftSide is not None and rightSide is not None:
            if leftSide.password > rightSide.password:
                complete_sort.next = leftSide
                leftSide = leftSide.next
            else:
                complete_sort.next = rightSide
                rightSide = rightSide.next
            complete_sort = complete_sort.next
    
        while leftSide is not None:
            complete_sort.next = leftSide
            leftSide = leftSide.next
            complete_sort = complete_sort.next
        
        while rightSide is not None:
            complete_sort.next = rightSide
            rightSide = rightSide.next
            complete_sort = complete_sort.next
        
        return head
    
    
##Main 
    def main():
        textFile = open("10-million-combos.txt", "r")
        linkList = None #  null linked list
 
        d = {} #    Dictionary
        try:
            print(textFile.read())
            with open(textFile):
                for file in textFile:
                    user_name = file.split("\t")
                    user_password = user_name[1]
                    if not solutionB(d, user_password):
                        d[user_password] = 1
                    if not solutionA(linkList, user_password):
                        linkList = Node(user_password, 1, linkList) 






        except:
            pass
        mergesort_list = merge_sort(linkList)
        while mergesort_list is not None:
            print(mergesort_list.password)
            mergesort_list = mergesort_list.next
        
    
        print_bubble = bubble_sort(linkList)
        while print_bubble is not None:
            print(print_bubble.password)
            print_bubble = print_bubble.next
        
        
        textFile.close()