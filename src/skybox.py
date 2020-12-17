from api.util import convert_to_texture;

from OpenGL import GL as GL11;

import pygame;

# filho de um anao
class Skybox:
	x = 0;
	y = 0;
	z = 0;

	w = 2048;
	h = 2048;
	l = 2048;

	def __init__(self, skybox_files):
		self.textures = [];

		for files in skybox_files:
			self.textures.append(convert_to_texture(pygame.image.load(files)));

	def on_render(self):
		self.list = GL11.glGenLists(1);

		self.x = self.x - self.w / 2;
		self.y = self.y - self.h / 2;
		self.z = self.z - self.l / 2;

		GL11.glNewList(self.list, GL11.GL_COMPILE);
		GL11.glColor(1, 1, 1);

		GL11.glEnable(GL11.GL_TEXTURE_2D);
		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures[0]);

		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.x, self.y, self.z + self.l);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.x, self.y + self.h, self.z + self.l);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.x + self.w, self.y + self.h, self.z + self.l);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.x + self.w, self.y, self.z + self.l);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.texture[1]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 0)
		GL11.glVertex3f(self.x + self.w, self.y, self.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.x + self.w, self.y + self.h, self.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.x, self.y + self.h, self.z);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.x, self.y, self.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.texture[2]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.x, self.y + self.h, self.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.x, self.y + self.h, self.z + self.l);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.x, self.y, self.z + self.l);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.x, self.y, self.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.texture[3]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.x + self.w, self.y, self.z);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.x + self.w, y, self.z + self.l);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.x + self.w, self.y + self.h, self.z + self.l);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.x + self.w, self.y + self.h, self.z);
		GL11.glEnd();

		glBindTexture(GL_TEXTURE_2D, self.texture["UP"])
		glBegin(GL_QUADS)
		glTexCoord2f(0, 0)
		glVertex3f(x+width, y+height, z)
		glTexCoord2f(1, 0)
		glVertex3f(x+width, y+height, z+length)
		glTexCoord2f(1, 1)
		glVertex3f(x, y+height, z+length)
		glTexCoord2f(0, 1)
		glVertex3f(x, y+height, z)
		glEnd()

		glBindTexture(GL_TEXTURE_2D, self.texture["DOWN"])
		glBegin(GL_QUADS)
		glTexCoord2f(0, 0)
		glVertex3f(x, y, z)
		glTexCoord2f(1, 0)
		glVertex3f(x, y, z+length)
		glTexCoord2f(1, 1)
		glVertex3f(x+width, y, z+length)
		glTexCoord2f(0, 1)
		glVertex3f(x+width, y, z)
		glEnd()

		glBindTexture(GL_TEXTURE_2D,0)
		glDisable(GL_TEXTURE_2D)

		glEndList()