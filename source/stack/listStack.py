class ListStack:	# 후입후출 (LIFO)
	def __init__(self):
		self.__stack = []

	def push(self, x):	# 스택에 원소 삽입하기 (맨 끝에 원소 삽입됨)
		self.__stack.append(x)

	def pop(self):	# 스탹에서 원소 삭제하기 (맨 끝 원소 삭제)
		return self.__stack.pop() # .pop(): 리스트의 끝(top) 원소를 삭제한 후 원소 리턴

	def top(self):	# 스택 맨 끝 원소 알려주기
		if self.isEmpty():
			return None
		else:
			return self.__stack[-1]

	def isEmpty(self) -> bool:	# 스택이 비었는지 확인하기
		return not bool(self.__stack)

	def popAll(self):	# 스택 비우기
		self.__stack.clear() 

	def printStack(self):	# 스택 전체 출력하기 (멘 위에서부터)
		print("Stack from top:", end = ' ')
		for i in range(len(self.__stack)-1, -1, -1):
			print(self.__stack[i], end = ' ')
		print()

# 코드 6-6