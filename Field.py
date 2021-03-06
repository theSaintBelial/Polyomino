
from utils import getSeparateLine


class Field:
	def __init__(self, width=None, height=None) -> None:
		if not width and not height:
			self.setSize()
		else:
			self.width = width
			self.height = height

	def setSize(self):
		self.width, self.height = list(map(lambda x: int(x), input("Enter width and heigth of the Field (use space to separate): ").split()))

	def getSize(self):
		return self.width, self.height

	def info(self):
		print(f"""{getSeparateLine()}
Field:
	- width: {self.width}
	- heigth: {self.height}
{getSeparateLine()}""")