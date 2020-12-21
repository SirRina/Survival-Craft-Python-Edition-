#
# Created by Rina at 28/11/2020 at 11:32pm
#
# Main class and game client initializer.
#

from api.libs import GL as GL11, pygame, GLU;
from api.util import lerp, Vec, CustomTextRender, clamp;

import math;

import camera;
import overlay;
import guiscreen;
import block;
import skybox;

import game_gui;

NAME    = "kkjkjkjk minecrafr e pytion"
VERSION = "0.0.1";

SHOW_VERSION = True;
START        = True;

class Main:
	screen_width  = 800;
	screen_height = 600;

	def __init__(self):
		pygame.init();

		self.display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.OPENGL | pygame.DOUBLEBUF);

		pygame.display.set_caption(NAME + " " + (VERSION if SHOW_VERSION is True else ""));

	def set_new_title(self, title):
		pygame.display.set_caption(title + " - " + NAME + " " + (VERSION if SHOW_VERSION is True else ""));

	def refresh_size(self):
		self.display = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.OPENGL | pygame.DOUBLEBUF);

	def set_size(self, w, h):
		self.screen_width  = w;
		self.screen_height = h;

		# Refrescar agua.
		self.refresh_size();

	def do_run(self):
		self.fov = 60; self.fog = 5000.0;

		self.GL11 = GL11;

		self.camera_manager  = camera.Camera(self, False);
		self.overlay_manager = overlay.OverlayManager(CURRENT_OPENGL = GL11, main = self);
		self.gui_manager     = guiscreen.GUIManager();

		self.clock = pygame.time.Clock();
		self.fps   = 75; # locked;

		self.clock.tick(self.fps);

		self.font_renderer = CustomTextRender("Arial", 19);

		self.last_delta_time = 0;

		self.camera_manager.focused = True;

		overlay.SPLIT = 0;

		self.background = [190, 190, 190];

		# O skybox ou seja aquele bagulho do ceu, incesto insano[
		self.skybox = skybox.Skybox("textures/skybox/");
		self.skybox.prepare();

		self.gui_manager.add(game_gui.GamePaused(self));
		self.gui_manager.add(game_gui.MainMenu(self));
		self.gui_manager.add(game_gui.Inventory(self));

		# NEGRO
		self.block = block.Block("kjkjk");

		self.cancel_render_3D = False;

		# Ok ele foi ativado entao.
		# Mas olha, eu fiz no final por que eu preciso iniciar 
		# antes as variaveis como 
		# cancel_render_3d
		# por que se nao da errokkk
		# ou seja, eu preciso cancelar o render 3D
		# depois que a variavel foi criada.
		self.gui_manager.get("MainMenu").open();

		# Aplicamos o OPENGL.
		GL11.glClearDepth(1)

		GL11.glViewport(0, 0, self.screen_width, self.screen_height);
		GL11.glMatrixMode(GL11.GL_PROJECTION);
		GL11.glLoadIdentity();
	
		GLU.gluPerspective(self.fov, (self.screen_width / self.screen_height), 0.1, self.fog);
	
		GL11.glMatrixMode(GL11.GL_MODELVIEW);
		GL11.glLoadIdentity();

		GL11.glDisable(GL11.GL_CULL_FACE);
		GL11.glEnable(GL11.GL_DEPTH_TEST);

		while (True):
			self.partial_ticks   = self.clock.tick() / self.fps;
			self.delta_time      = self.partial_ticks - self.last_delta_time;
			self.last_delta_time = self.partial_ticks;

			self.update_event();

			GL11.glClear(GL11.GL_COLOR_BUFFER_BIT | GL11.GL_DEPTH_BUFFER_BIT);
			GL11.glClearColor(float(self.background[0] / 255.0), float(self.background[1] / 255.0), float(self.background[2] / 255.0), 1.0);

			if self.cancel_render_3D != True:
				self.render_3D();

			GL11.glPushMatrix();

			GL11.glViewport(0, 0, self.screen_width, self.screen_height);
			GL11.glMatrixMode(GL11.GL_PROJECTION);
			GL11.glLoadIdentity();
	
			GLU.gluOrtho2D(0, self.screen_width, self.screen_height, 0)
	
			GL11.glMatrixMode(GL11.GL_MODELVIEW);
			GL11.glLoadIdentity();

			self.render_2D();

			GL11.glViewport(0, 0, self.screen_width, self.screen_height);
			GL11.glMatrixMode(GL11.GL_PROJECTION);
			GL11.glLoadIdentity();
	
			GLU.gluPerspective(self.fov, (self.screen_width / self.screen_height), 0.1, self.fog);
	
			GL11.glMatrixMode(GL11.GL_MODELVIEW);
			GL11.glLoadIdentity();
	
			GL11.glPopMatrix();

			pygame.display.flip();

	def update_event(self):
		for current_event in pygame.event.get():
			if (current_event.type == pygame.QUIT):
				pygame.quit();

				quit();

			if current_event.type == pygame.MOUSEBUTTONUP:
				self.gui_manager.update_click_up(current_event.button);

			if current_event.type == pygame.MOUSEBUTTONDOWN:
				self.gui_manager.update_click_down(current_event.button);

			if self.gui_manager.get("MainMenu").active == False:
				if current_event.type == pygame.KEYDOWN:
					try:
						self.gui_manager.open(game_gui.KEYBIND_GUI[current_event.key]);
					except:
						pass

		keys = pygame.key.get_pressed();

		if (keys[pygame.K_r]):
			self.camera_manager.set_pos(0, 0, 0);

		if (keys[pygame.K_t]):
			self.camera_manager.set_static_pos(0, 0, 0);

		self.camera_manager.update_camera(0.1, self.screen_width, self.screen_height);

	def render_3D(self):
		# ok liguei a lista criada na classe skybox que renderiza tudo.
		self.skybox.on_render();
		self.block.on_render();

	def render_2D(self):
		self.overlay_manager.on_render();
		self.gui_manager.update_render();

if (__name__ == "__main__"):
	game = Main();

	game.do_run();