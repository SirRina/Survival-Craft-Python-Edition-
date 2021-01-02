from OpenGL import GL as GL11;
from api    import util;

import os;

import pygame;

class Face:
	def __init__(self, name):
		self.name = name;

FACE_BACK  = 0x00;
FACE_DOWN  = 0x01;
FACE_FRONT = 0x02;
FACE_LEFT  = 0x03;
FACE_RIGHT = 0x04;
FACE_UP    = 0x05;

REQUEST_FACE = [
	FACE_BACK, 
	FACE_DOWN, 
	FACE_FRONT,
	FACE_LEFT, 
	FACE_RIGHT,
	FACE_UP
];

FACES = {
	0x00 : Face("BACK"),
	0x01 : Face("DOWN"),
	0x02 : Face("FRONT"),
	0x03 : Face("LEFT"),
	0x04 : Face("RIGHT"),
	0x05 : Face("UP")
};

# pedreiros constrem rodrig , mx .
class Block:
	def __init__(self, name, current_path_textures = None):
		self.name = name;
		self.aabb = util.AABB();

		self.position = util.Vec(0.0, 0.0, 0.0);

		# blocos na teoria tem yaw e pitch simmm.
		self.yaw   = 0;
		self.pitch = 0;

		self.aabb.max.x = 1;
		self.aabb.max.y = 1;
		self.aabb.max.z = 1;

		self.textures = {};

		self.render_list = GL11.glGenLists(1);

		self.transparency = False;
		self.alpha        = 255;

		if None != current_path_textures:
			for faces in REQUEST_FACE:
				face_name_requested = FACES[faces].name.lower();

				path = os.path.join(os.path.abspath(current_path_textures + name + "_" + face_name_requested));

				self.textures[face_name_requested] = util.convert_to_texture(pygame.image.load(path + ".png"));

		GL11.glNewList(self.render_list, GL11.GL_COMPILE);
		GL11.glColor(1, 1, 1);

		GL11.glEnable(GL11.GL_TEXTURE_2D);
		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["front"]);

		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["back"]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 0)
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["left"]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["right"]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["up"]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y + self.aabb.max.y, self.aabb.min.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, self.textures["down"]);
		GL11.glBegin(GL11.GL_QUADS);
		GL11.glTexCoord2f(0, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glTexCoord2f(1, 0);
		GL11.glVertex3f(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(1, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z + self.aabb.max.z);
		GL11.glTexCoord2f(0, 1);
		GL11.glVertex3f(self.aabb.min.x + self.aabb.max.x, self.aabb.min.y, self.aabb.min.z);
		GL11.glEnd();

		GL11.glBindTexture(GL11.GL_TEXTURE_2D, 0);
		GL11.glDisable(GL11.GL_TEXTURE_2D);

		GL11.glEndList();

	def on_render(self):
		self.aabb.min.x = self.position.x;
		self.aabb.min.y = self.position.y;
		self.aabb.min.z = self.position.z;

		print(self.aabb.min.x + self.aabb.max.x);

		# aqui eu desenho a pora, o que e pora;
		GL11.glPushMatrix();
		GL11.glTranslate(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);

		if self.transparency:
			GL11.glEnable(GL11.GL_BLEND);
			GL11.glBlendFunc(GL11.GL_SRC_ALPHA, GL11.GL_SRC_MINUS_ALPHA);

			GL11.glColor(1, 1, 1, self.alpha / 255.0);

		GL11.glCallList(self.render_list);

		if self.transparency:
			GL11.glDisable(GL11.GL_BLEND);

		GL11.glPopMatrix();