from api.util import Vec, lerp, clamp;
from math     import sin, cos, sqrt, degrees, radians, pi;

import pygame, OpenGL.GL as GL11;

class CameraManager:
	MOUSE_SENSIVITY = 0.1;
	MOUSE_INVERTED  = False;

	CAMERA_LENGHT = 0.2;

	def __init__(self, main):
		self.position = Vec(0, 0, 0);

		self.yaw   = 60;
		self.pitch = 0;

		self.focused = False;

		self.main = main;

		self.x, self.y, self.z = 0, 0, 0;

	def get_pos(self):
		return self.position.get();

	def set_pos(self, x, y, z):
		self.position.x, self.position.y, self.position.z = x, y, z;

	def get_yaw_pitch(self):
		return [self.yaw, self.pitch];

	def set_yaw(self, amount):
		self.yaw -= amount;

	def set_pitch(self, amount):
		if self.MOUSE_INVERTED:
			self.pitch -= amount;
		else:
			self.pitch += amount

	def calcule_x_from_angle(self, angle):
		return sin(radians(angle));

	def calcule_z_from_angle(self, angle):
		return cos(radians(angle));

	def focus(self):
		self.focused = True;

	def set_pos(self, x, y, z):
		self.position.x = x;
		self.position.y = y;
		self.position.z = z;

	def set_static_pos(self, x, y, z):
		self.set_pos(x, y, z);

		self.x = x;
		self.y = y;
		self.z = z;

	def update_camera(self):
		GL11.glLoadIdentity();

		keys = pygame.key.get_pressed();
		rel  = pygame.mouse.get_rel();

		if self.focused:
			self.set_yaw((rel[0]) * self.MOUSE_SENSIVITY);
			self.set_pitch((rel[1]) * self.MOUSE_SENSIVITY);

		pygame.event.set_grab(self.focused)
		pygame.mouse.set_visible(self.focused != True);

		if self.pitch >= 90:
			self.pitch = 90;

		if self.pitch <= -90:
			self.pitch = -90;

		GL11.glRotate(self.pitch, 1, 0, 0)
		GL11.glRotate(360 - self.yaw, 0, 1, 0);

		# el ogro
		self.x = lerp(self.x, self.position.x, self.main.partial_ticks);
		self.y = lerp(self.y, self.position.y, self.main.partial_ticks);
		self.z = lerp(self.z, self.position.z, self.main.partial_ticks);

		GL11.glTranslate(self.x, self.y, self.z);