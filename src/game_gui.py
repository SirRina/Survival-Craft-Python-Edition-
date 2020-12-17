import guiscreen;
import overlay;
import pygame;

KEYBIND_GUI = {
	pygame.K_ESCAPE : "GamePaused",
	pygame.K_e : "Inventory"
};

class GamePaused(guiscreen.GUI):
	def __init__(self, main):
		super().__init__("Game Paused", "GamePaused", "When game is paused.");

		self.main = main;

	def closed(self):
		pygame.mouse.set_pos(self.main.screen_width / 2, self.main.screen_height / 2);

		self.main.camera_manager.focused = True;
	
		overlay.SPLIT     = 1;
		overlay.DEVELOPER = 1;

	def opened(self):
		overlay.SPLIT     = 0;
		overlay.DEVELOPER = 0;

		self.main.camera_manager.focused = False;

	def on_click_up(self, button):
		if button == 1:
			self.close();

	def on_render(self):
		text = "Game Paused";

		self.main.font_renderer.draw(text, self.main.screen_width / 2 - self.main.font_renderer.get_width(text) / 2, self.main.screen_height / 2, [0, 0, 0]);

class MainMenu(guiscreen.GUI):
	def __init__(self, main):
		super().__init__("Main Menu", "MainMenu", "Main menu");

		self.main = main;

	def closed(self):
		pygame.mouse.set_pos(self.main.screen_width / 2, self.main.screen_height / 2);

		self.main.camera_manager.focused = True;
	
		overlay.SPLIT     = 1;
		overlay.DEVELOPER = 1;

		self.main.cancel_render_3D = False;

	def opened(self):
		overlay.SPLIT     = 0;
		overlay.DEVELOPER = 0;

		self.main.camera_manager.focused = False;
		self.main.cancel_render_3D       = True;

	def on_click_up(self, button):
		if button == 1:
			self.close();

	def on_render(self):
		text = "Main Menu";

		self.main.font_renderer.draw(text, self.main.screen_width / 2 - self.main.font_renderer.get_width(text) / 2, self.main.screen_height / 2, [0, 0, 0]);

class Inventory(guiscreen.GUI):
	def __init__(self, main):
		super().__init__("Inventory", "Inventory", "Inventory");

		self.main = main;

	def closed(self):
		pygame.mouse.set_pos(self.main.screen_width / 2, self.main.screen_height / 2);

		self.main.camera_manager.focused = True;
	
		overlay.SPLIT     = 1;
		overlay.DEVELOPER = 1;

	def opened(self):
		overlay.SPLIT     = 0;
		overlay.DEVELOPER = 0;

		self.main.camera_manager.focused = False;

	def on_click_up(self, button):
		if button == 1:
			self.close();
	
	def on_render(self):
		text = "Inventory";
		coordinates = "Your in";

		height = self.main.font_renderer.get_height();
		
		self.main.font_renderer.draw(text, self.main.screen_width / 2 - self.main.font_renderer.get_width(text) / 2, self.main.screen_height / 2, [0, 0, 0]);
		
		#self.main.font_renderer.draw(coordinates + str(int(self.main.camera_manager.position.x)) + " " + str(int(self.main.camera_manager.position.y)) + " " + str(int(self.main.camera_manager.position.z)), 10, [0, 0, 0]);