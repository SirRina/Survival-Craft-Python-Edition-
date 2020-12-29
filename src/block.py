from api.util import AABB, convert_to_texture;

from OpenGL import GL as GL11;

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
		self.aabb = AABB();

		self.aabb.max.x = 1;
		self.aabb.max.y = 1;
		self.aabb.max.z = 1;

		self.textures_by_face = {};

		if None != current_path_textures:
			for faces in REQUEST_FACE:
				face_name_requested = FACES[faces].name.lower();

				path = os.path.join(os.path.abspath(current_path_textures + face_name_requested));

				self.textures_by_face[sides] = convert_to_texture(pygame.image.load(filePath + ".png"));

	def move(self):
		self.aabb.min.x += 0.1;

	# No caso o min e maz AABB colisao fodase.
	def camera_in(self, camera):
		return (camera.position.x + camera.CAMERA_LENGHT >= self.aabb.min.x and camera.position.x - camera.CAMERA_LENGHT <= self.aabb.max.x) and \
			   (camera.position.y + camera.CAMERA_LENGHT >= self.aabb.min.y and camera.position.y - camera.CAMERA_LENGHT <= self.aabb.max.y) and \
			   (camera.position.z + camera.CAMERA_LENGHT >= self.aabb.min.z and camera.position.z - camera.CAMERA_LENGHT <= self.aabb.max.z);

	def on_render(self):
		# aqui eu desenho a pora, o que e pora;
		pass