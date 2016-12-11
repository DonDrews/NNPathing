import sfml.graphics as sfgr
import sfml.window as sfwi

class Window:

	def __init__(self):
		#set up window and viewport
		self.window = sfgr.RenderWindow(sfwi.VideoMode(400, 400), "NN Pathing")
		self.window.framerate_limit = 30

		v = sfgr.View(sfgr.Rectangle((0, 0), (400, -400))) #negative y for inverting of rendering
		self.window.view = v

		self.window.view.center = (200, 200)

		self.shape = sfgr.RectangleShape((20, 20))

	def update(self, map):

		self.window.clear()

		print("update") #TEST
		#render scene
		for i in range(map.raster.shape[0]):
			for j in range(map.raster.shape[1]):
				if map.raster[i][j] == map.FLOOR:
					self.shape.fill_color = sfgr.Color(255, 255, 255)
				else:
					self.shape.fill_color = sfgr.Color(0, 0, 0)
				
				self.shape.position = (i * 20, j * 20)
				self.window.draw(self.shape)

		self.window.display()
