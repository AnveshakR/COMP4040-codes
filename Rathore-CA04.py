import sys

# assuming min-heap starting at index 0

class MinHeapNode: # defining class for each node
	element = 0

	i, j = 0, 0

	def __init__(self, element, i, j): # node constructor
		self.element = element
		self.i = i
		self.j = j
		

class MinHeap: #defining class for the entire heap
	heap = None
	
	heap_size = 0
	
	def __init__(self, a, size): # heap constructor
		self.heap_size = size
		self.heap = a
		i = int((self.heap_size - 1) / 2)
		while (i >= 0):
			self.MinHeapify(i)
			i -= 1
			
	def MinHeapify(self, i): # function to heapify subtrees into main tree, assumes subtrees are already heapified
		l = self.left(i)
		r = self.right(i)
		smallest = i
		if (l < self.heap_size and self.heap[l].element < self.heap[i].element):
			smallest = l
		if (r < self.heap_size and self.heap[r].element < self.heap[smallest].element):
			smallest = r
		if (smallest != i):
			self.swap(self.heap, i, smallest)
			self.MinHeapify(smallest)
		
	def left(self, i): # get index of left child of node at index i
		return (2 * i + 1)
	
	def right(self, i): # get index of right child of node at index i
		return (2 * i + 2)
	
	def getMin(self): # get root of heap
		if (self.heap_size <= 0):
			print("Heap underflow")
			return None
		return self.heap[0]

	def replaceMin(self, root): # replace root with new node if it is smaller 
		self.heap[0] = root
		self.MinHeapify(0)
		
	def swap(self, arr, i, j): # swap two nodes
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		
	@staticmethod
	def printArray(arr): # print the array
		for i in arr:
			print(str(i) + " ", end ="")
		print()
		
	@staticmethod
	def mergeKSortedArrays(arr, K): # merges k sorted arrays
		heap = [None] * (K)
		resultSize = 0
		i = 0
		while (i < len(arr)):
			node = MinHeapNode(arr[i][0], i, 1)
			heap[i] = node
			resultSize += len(arr[i])
			i += 1
			
		mh = MinHeap(heap, K) # create min-heap with first element of every array
		result = [0] * (resultSize)
	
		i = 0
		while (i < resultSize): # heapify, get minimum element, remove it and replace with next number from same array
		
			root = mh.getMin()
			result[i] = root.element

			if (root.j < len(arr[root.i])):
				root.element = arr[root.i][root.j]
				root.j += 1
			else:
				root.element = sys.maxsize

			mh.replaceMin(root)
			i += 1
		MinHeap.printArray(result)
	
	@staticmethod
	def main(args): # main method
		arr = [[2, 4, 6, 8, 10, 5000], [1, 3, 5, 9, 11, 4000], [1, 2, 3, 5, 8, 13, 21, 3000]]
		print("Merged array is:", end=" ")

		MinHeap.mergeKSortedArrays(arr, len(arr))
	
if __name__=="__main__":
	MinHeap.main([])