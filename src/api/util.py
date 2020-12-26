#
# Created by Rina at 28/11/2020 at 11:32pm
#
# Game util;
#

import pygame;
import time;

import OpenGL.GL  as GL11;
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

def convert_to_texture(surface):
	w = surface.get_width();
	h = surface.get_height();

	data    = pygame.image.tostring(surface, "RGBA", 1);
	texture = GL11.glGenTextures(1);

	GL11.glBindTexture(GL11.GL_TEXTURE_2D, texture);
	GL11.glPixelStorei(GL11.GL_UNPACK_ALIGNMENT, 1);
	GL11.glTexEnvf(GL11.GL_TEXTURE_ENV, GL11.GL_TEXTURE_ENV_MODE, GL11.GL_MODULATE);

	GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MIN_FILTER, GL11.GL_LINEAR);

	GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MAG_FILTER, GL11.GL_NEAREST);
	GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_WRAP_S, GL11.GL_CLAMP_TO_EDGE);
	GL11.glTexParameteri(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_WRAP_T, GL11.GL_CLAMP_TO_EDGE);

	GL11.glTexImage2D(GL11.GL_TEXTURE_2D, 0, GL11.GL_RGBA, w, h, 0, GL11.GL_RGBA, GL11.GL_UNSIGNED_BYTE, data);

	return texture;

class CustomTextRender(object):
	def __init__(self, font = None, size = None):
		self.path  = font;
		self.size  = size;

		self.cfont = None;

		try:
			self.cfont = pygame.font.SysFont(font, self.size);
		except:
			self.cfont = pygame.font.Font(self.path, self.size);

	def get_width(self, string):
		surface_text = self.cfont.render(string, 1, (255, 255, 255), False);

		width, height = surface_text.get_size();

		return width;

	def get_height(self):
		surface_text = self.cfont.render("", 1, (255, 255, 255), False);

		width, height = surface_text.get_size();

		return height;

	def draw(self, text, x, y, color):
		surface_text = self.cfont.render(text, 1, (color), False);
	
		data          = pygame.image.tostring(surface_text, "RGBA");
		width, height = surface_text.get_size();

		id = GL11.glGenTextures(1)

		GL11.glEnable(GL11.GL_TEXTURE_2D);

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, id)
		
		GL11.glTexParameterf(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MAG_FILTER, GL11.GL_NEAREST)
		GL11.glTexParameterf(GL11.GL_TEXTURE_2D, GL11.GL_TEXTURE_MIN_FILTER, GL11.GL_NEAREST)

		GL11.glTexImage2D(GL11.GL_TEXTURE_2D, 0, GL11.GL_RGBA, width, height, 0, GL11.GL_RGBA, GL11.GL_UNSIGNED_BYTE, data)			
		GL11.glBindTexture(GL11.GL_TEXTURE_2D, 0)

		GL11.glDisable(GL11.GL_DEPTH_TEST);

		GL11.glEnable(GL11.GL_BLEND)
		GL11.glBlendFunc(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA)
		GL11.glBindTexture(GL11.GL_TEXTURE_2D, id)
		GL11.glBegin(GL11.GL_QUADS)
		GL11.glTexCoord(0, 0); GL11.glVertex(x, y, 0)
		GL11.glTexCoord(0, 1); GL11.glVertex(x, y + height, 0)
		GL11.glTexCoord(1, 1); GL11.glVertex(x + width, y + height, 0)
		GL11.glTexCoord(1, 0); GL11.glVertex(x + width, y, 0)
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, 0);

		GL11.glEnable(GL11.GL_DEPTH_TEST);
		GL11.glDisable(GL11.GL_BLEND);
		GL11.glDisable(GL11.GL_TEXTURE_2D);

# NEgro.
class AABB:
	def __init__(self):
		self.min = Vec(0, 0, 0);
		self.max = Vec(0, 0, 0);

	def collide(self, aabb):
		return (self.min.x >= aabb.min.x and self.max.x <= aabb.max.x) and \
			   (self.min.y >= aabb.min.y and self.max.y <= aabb.max.y) and \
			   (self.min.z >= aabb.min.z and self.max.z <= aabb.max.z);

# oi brain
class Rect:
	def __init__(self, tag):
		self.x, self.y, self.w, self.h = 0, 0, 0, 0;

		self.tag = tag;

# aqui e so um contador de tempo, to fazendo mesmo e pra marcar tempo, tipo se passou 1 segundo etc.
class Tick:
	def __init__(self):
		self.ticks = -1;

	def reset(self):
		self.ticks = pygame.time.get_ticks();

	def current_ticks(self):
		return pygame.time.get_ticks() - self.ticks;

	def is_passed(self, ms):
		return pygame.time.get_ticks() - self.ticks >= ms;

	def count(self, ms_div):
		return (pygame.time.get_ticks() - self.ticks) / ms_div;