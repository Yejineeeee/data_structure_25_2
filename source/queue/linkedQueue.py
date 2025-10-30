from DS.list.circularLinkedList import CircularLinkedList

class LinkedQueue:	# 연결 리스트 큐
	def __init__(self):	# 원형 연결 라스트로 구현
		self.__queue = CircularLinkedList()

	def enqueue(self, x):	# 큐에 원소 삽입하기
		self.__queue.append(x)

	def dequeue(self):	# 큐에서 원소 삭제하기
		return self.__queue.pop(0)	# .pop(0): 리스트의 첫 원소를 삭제한 후 원소 리턴

	def front(self):	# 큐의 맨 앞 원소 알려주기 (인덱스로 접근 불가)
		return self.__queue.get(0)	 # .get(0): 리스트의 첫 원소 리턴

	def isEmpty(self) -> bool:	# 큐가 비었는지 확인하기
		return self.__queue.isEmpty()
 
	def dequeueAll(self):	# 큐 비우기
		self.__queue.clear()
  
	def printQueue(self):	# 큐 전체 출력하기
		print("Queue from front:", end = ' ')
		for i in range(self.__queue.size()):
			print(self.__queue.get(i), end = ' ')
		print()

# 코드 7-13