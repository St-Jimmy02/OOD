class TorKham:

	def __init__(self):

		self.words = []
    
	def restart(self):
		self.words.clear()
		print("game restarted")

	def play(self, word):
		if not word.isalpha():
			self.words.clear()
			print("game over")
			return 
		
		if len(self.words) == 0:
			self.words.append(word)
			print(f"'{word}' -> {self.words}")
			return 
		
		if self.words[-1][-2:].lower() == word[:2].lower():
			self.words.append(word)
			print(f"'{word}' -> {self.words}")
		else:
			print(f"'{word}' -> game over")
			self.words.clear()
			return



torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')

for pang in S:
	if 'P ' in pang: torkham.play(pang[2:])
	elif 'R' in pang: torkham.restart()
	elif 'X' in pang: break
	else: 
		print(f"'{pang}' is Invalid Input !!!")
		break
 ### Enter Your Code Here ###