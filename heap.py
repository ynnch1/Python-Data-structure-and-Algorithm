#importing "heapq" to implement heap queue
import heapq

#initializing list
li1 = [5, 7, 9, 1, 3]
#initializing list2
li2 = [5, 7, 9 , 1, 3]

#using heapify to convert lists into heap
heapq.heapify(li1)
heapq.heapify(li2)

#printing created heap
print("the heap is: ", end="")
print(list(li1))

#using heappush() to push elements into heap
#pushes 4
heapq.heappush(li1, 4)

#printing modified heap
print('the modified heap after push is:', end="")
print(list(li1))

#using heappop() to pop the smallest element
print('The popped and smallest element is: ', end="")
print(heapq.heappop(li1))

#using heappushpop() to push and pop element simultaniously
#pops 2
print("the popped item using heappushpop is: ", end="")
print(heapq.heappush(li1, 2))

#using heapreplace() to push and pop items simultaneously 
#pops 3
print(heapq.heapreplace(li2, 3))

#using nlargest to print 3 largest numbers
#prints 16, 9 and 8
print(heapq.nlargest(3, li1))

#using nsmallest to print 3 smallest numbers
#prints 1, 3 and 4
print(heapq.nsmallest(3, li1))