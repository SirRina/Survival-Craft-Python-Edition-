#
# Created by Rina at 28/11/2020 at 11:32pm
#
# Game util;
#

import pygame

import OpenGL.GL  as GL;
import OpenGL.GLU as GLU;

from math import sqrt;

class Vec:
	def __init__(self, x, y, z):
		self.x = x;
		self.y = y;
		self.z = z;

	def get_x(self):
		return self.x;

	def get_y(self):
		return self.y;

	def get_z(self):
		return self.z;

	def get(self):
		return [self.x, self.y, self.z];

	def length(self):
		return sqrt(self.x * self.x + self.y + self.z * self.z);

	def collide(self, x, y, z):
		if self.x >= x + 1 and self.x - 1 <= x and \
		   self.y >= y + 1 and self.y - 1 <= y and \
		   self.z >= z + 1 and self.y - 1 <= z:
		   	return True;

		return False;

	def __add__(self, num):
		if type(num) is Vec:
			return Vec(self.x + num.x, self.y + num.y, self.z + num.z);

		return Vec(self.x + num, self.y + num, self.z + num);

	def __sub__(self, num):
		if type(num) is Vec:
			return Vec(self.x - num.x, self.y - num.y, self.z - num.z);

		return Vec(self.x - num, self.y - num, self.z - num);

	def __mul__(self, num):
		if type(num) is Vec:
			return Vec(self.x * num.x, self.y * num.y, self.z * num.z);

		return Vec(self.x * num, self.y * num, self.z * num);

	def __div__(self, num):
		return Vec(self.x / num, self.vec.y / num, self.z / num);

	def __neg__(self):
		return Vec(-self.x, -self.y, -self.z);

def lerp(a, b, partial):
	return (a + (b - a) * partial);

def clamp(value, minimum, maximum):
	return (value if value <= maximum else maximum) if value >= minimum else minimum;

class CustomTextRender(object):
	def __init__(self, font = None, size = None):
		self.path  = font;
		self.size  = size;

		self.cfont = None;

		try:
			self.cfont = pygame.font.SysFont(font, self.size);
		except:
			self.cfont = pygame.font.Font(self.path, self.size);

	def draw(self, text, x, y, color):
		surface_text = self.cfont.render(text, 1, (color), False);
	
		data          = pygame.image.tostring(surface_text, "RGBA");
		width, height = surface_text.get_size();

		id = GL.glGenTextures(1)

		GL.glEnable(GL.GL_TEXTURE_2D);

		GL.glBindTexture(GL.GL_TEXTURE_2D, id)
		
		GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
		GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)

		GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, width, height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, data)			
		GL.glBindTexture(GL.GL_TEXTURE_2D, 0)

		GL.glEnable(GL.GL_BLEND)
		GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
		GL.glBindTexture(GL.GL_TEXTURE_2D, id)
		GL.glBegin(GL.GL_QUADS)
		GL.glTexCoord(0, 0); GL.glVertex(x, y, 0)
		GL.glTexCoord(0, 1); GL.glVertex(x, y + height, 0)
		GL.glTexCoord(1, 1); GL.glVertex(x + width, y + height, 0)
		GL.glTexCoord(1, 0); GL.glVertex(x + width, y, 0)
		GL.glEnd();

		GL.glBindTexture(GL.GL_TEXTURE_2D, 0);

		GL.glDisable(GL.GL_TEXTURE_2D);