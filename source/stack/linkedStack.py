from DS.list.linkedList import LinkedList

class LinkedStack:	# 연결 리스트 스택
	def __init__(self):	# 연결 리스트로 구현
		self.__list = LinkedListBasic()

	def push(self, newItem):	# 스택 맨 위에 원소 삽입하기
		self.__list.insert(0, newItem)

	def pop(self):	# 스택에서 원소 삭제하기
		return self.__list.pop(0)

	def top(self):	# 스택의 맨 위 원소 알려주기 (인덱스로 접근 불가)
		if self.isEmpty():	# .get(0): 리스트의 맨 위 원소 리턴
			return None
		else:
			return self.__list.get(0)

	def isEmpty(self) -> bool:	# 스택이 비었는지 확인하기
		return self.__list.isEmpty()

	def popAll(self):	# 스택 비우기
		self.__list.clear()

	def printStack(self):	# 스택 전체 출력하기 (맨 위부터)
		print("Stack from top:", end = '')
		for i in range(self.__list.size()):
			print(self.__list.get(i), end = '')
		print()

# 코드 6-13