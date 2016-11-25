import sfml.graphics as sfgr
import sfml.window as sfwi

class Window:

	def __init__(self):
		#set up window and viewport
                self.window = sfgr.RenderWindow(sfwi.VideoMode(1280, 720), "NN Pathing")
                self.window.framerate_limit = 30

                v = sfgr.View(sfgr.Rectangle((0, 0), (1280, -720))) #negative y for inverting of rendering
                self.window.view = v

	def update(self):
		pass
