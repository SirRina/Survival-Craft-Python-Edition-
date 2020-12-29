from entity import EntityPlayer;

class World:
	def __init__(self, main):
		self.main               = main;
		self.loaded_entity_list = [];
		self.gravity            = 0.001;

	def implement_entity(self, entity):
		if EntityPlayer == type(entity):
			self.loaded_entity_list.append(entity);

	def kill_entity(self, entity):
		if EntityPlayer == type(entity):
			self.get_entity(entity.tag).set_living(False);

	def spawn_entity(self, entity, position):
		# nao podemos spanawe algo vivido.
		if EntityPlayer == type(entity) and not entity.is_living():
			self.get_entity(entity.tag).set_living(True);

			# sim pernas de pau.
			self.get_entity(entity.tag).position.x = position[0];
			self.get_entity(entity.tag).position.y = position[1];
			self.get_entity(entity.tag).position.z = position[2];

	def get_entity(self, entity_tag):
		for entities in self.loaded_entity_list:
			if entities.tag == entity_tag:
				return entities;