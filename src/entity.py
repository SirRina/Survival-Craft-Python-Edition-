from api.util import Vec;
from api.data_manager import DataManager;

import OpenGL.GL as GL11;

import block;

class Entity:
	def __init__(self, name, tag, description):
		self.name, self.tag, self.description = name, tag, description;

		self.flag = DataManager("Entity");

		self.position = Vec(0, 0, 0);
		self.yaw      = 0;
		self.pitch    = 0;

		self.rendering = True;
		self.collide   = True;
		self.physhic   = True;

		self.block = block.Block("Negro");

	def init(self):
		self.flag.add_data_value("Camera", False);
		self.flag.add_data_value("OnGround", False);
		self.flag.add_data_value("Living", True);
		self.flag.add_data_value("Walking", False);
		self.flag.add_data_value("Flying", False);
		self.flag.add_data_value("Health", 20); # Assim, a vida e 20 fovdasekk.

	def set_camera(self, boolean):
		self.flag.set_value_data("Camera", boolean);

	def camera(self):
		return self.flag.get("Camera");

	def set_on_ground(self, boolean):
		if (self.flag.get("Living") or self.flag.get("Health") > 0):
			self.flag.set_value_data("OnGround", boolean);

	def get_on_ground(self):
		return self.flag.get("OnGround");

	def set_living(self, boolean):
		if boolean:
			self.flag.set_value_data("Living", True);
			self.flag.set_value_data("Health", 20);

			self.rendering = True;
		else:
			self.flag.set_value_data("Living", False);
			self.flag.set_value_data("Health", 20);

			self.rendering = False;

	def is_living(self):
		return self.flag.get("Living");

	def set_walking(self, boolean):
		if ((self.flag.get("Living") or self.flag.get("Health") > 0) and self.flag.get("OnGround")):
			self.flag.set_value_data("Walking", boolean);

	def is_walking(self):
		return self.flag.get("Walking");

	def set_flying(self, boolean):
		if (self.flag.get("Living") or self.flag.get("Health") > 0):
			self.flag.set_value_data("Flying", boolean);

	def is_flying(self):
		return self.flag.get("Flying");

	def set_health(self, number):
		if (self.flag.get("Living")):
			self.flag.set_value_data("Health", number);
		else:
			self.flag.set_value_data("Health", number);
			self.flag.set_value_data("Living", True);

			self.rendering = True;

	def get_health(self):
		return self.flag.get("Health");

	def keyboard(self):
		if (self.rendering):
			if self.flag.get("Camera"):
				pass

	def render(self):
		if (self.rendering):
			self.block.aabb.min = self.position;

			self.block.on_render();

class EntityPlayer(Entity):
	def __init__(self, name, tag, description):
		super().__init__(name, tag, description);
