class ListQueue:	# 선입선출 (FIFO)
	def __init__(self):
		self.__queue = []

	def enqueue(self, x):	# 큐에 원소 x 삽입하기 (맨 끝에 원소 삽입됨)
		self.__queue.append(x)

	def dequeue(self):	# 큐에서 원소 x 삭제하기 
		return self.__queue.pop(0) # .pop(0): 리스트의 첫 원소를 삭제한 후 원소 리턴

	def front(self):	# 큐의 맨 앞 원소 알려주기
		if self.isEmpty():
			return None
		else:
			return self.__queue[0]

	def isEmpty(self) -> bool:	# 큐가 비었는지 확인하기
		return (len(self.__queue) == 0)
 
	def dequeueAll(self):	# 큐 비우기
		self.__queue.clear()

	def printQueue(self):	# 큐 전체 출력하기
		print("Queue from front:", end = ' ')
		for i in range(len(self.__queue)):
			print(self.__queue[i], end = ' ')
		print()

# 코드 7-6

