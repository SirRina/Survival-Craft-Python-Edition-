from api.util import AABB;

from OpenGL import GL as GL11;

class Block:
	MASK_BLOCK = [
		[0, 0, 0],
		[0, 0, -1],
		[-1, 0, -1],
		[-1, 0, 0],
	
		[0, 0, 0],
		[-1, 0, 0],
		[-1, -1, 0],
		[0, -1, 0],
	
		[0, 0, 0],
		[0, -1, 0],
		[0, -1, -1],
		[0, 0, -1],
	
		[-1, 0, 0],
		[-1, 0, -1],
		[-1, -1, -1],
		[-1, -1, 0],
	
		[0, 0, 0],
		[0, -1, -1],
		[-1, -1, -1],
		[-1, -1, 0],
	
		[0, 0, 0],
		[-1, 0, -1],
		[-1, -1, -1],
		[0, -1, -1]
	]

	def __init__(self, name):
		self.name = name;
		self.aabb = AABB();

		self.aabb.max.x = 1;
		self.aabb.max.y = 1;
		self.aabb.max.z = 1;

	def move(self):
		self.aabb.min.x += 0.1;

	# No caso o min e maz AABB colisao fodase, negro.
	def camera_in(self, camera):
		return (camera.position.x >= self.aabb.min.x and camera.position.x <= self.aabb.max.x) and \
			   (camera.position.y >= self.aabb.min.y and camera.position.y <= self.aabb.max.y) and \
			   (camera.position.z >= self.aabb.min.z and camera.position.z <= self.aabb.max.z);

	def on_render(self):
		# aqui eu desenho a pora, o que e pora;
		GL11.glPushMatrix();
		GL11.glTranslate(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);

		GL11.glBegin(GL11.GL_QUADS);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y, self.aabb.min.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z); 
		
		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);
		
		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.y, self.aabb.min.y - self.aabb.min.y, self.aabb.min.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);
		
		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y, self.aabb.min.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x - self.aabb.max.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glColor(1, 0, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y, self.aabb.min.z);

		GL11.glColor(0, 1, 0);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z);

		GL11.glColor(0, 0, 1);
		GL11.glVertex(self.aabb.min.x, self.aabb.min.y - self.aabb.max.y, self.aabb.min.z - self.aabb.max.z);

		GL11.glEnd();

		GL11.glPopMatrix();