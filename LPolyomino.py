
from Polyomino import Polyomino
import numpy as np


class LPolyomino(Polyomino):
	def __init__(self, id, height, width):
		super().__init__(id, height, width)
		self.setShapesCount()

	def setShapesCount(self):
		self.shapesCount = 4

	def getArea(self):
		return self.getHeight() + (self.getWidth() - 1)

	def getShapes(self):
		shapes = np.array([
			np.array([
				np.array((x, y))
				for x in range(self.getWidth())
				for y in range(self.getHeight())
				if (x < 1 or y == self.getHeight() - 1)
			]),
			np.array([
				np.array((x, -y))
				for x in range(self.getWidth())
				for y in range(self.getHeight())
				if (y < 1 or x == self.getWidth() - 1)
			])
		])
		shapes = np.append(shapes, shapes * -1, axis=0)
		return shapes
