from entity import EntityPlayer;

import block;

class World:
	def __init__(self, main):
		self.main               = main;
		self.loaded_entity_list = [];
		self.gravity            = 0.001;

		self.chunk = [];

	def load_chunk(self, size):
		# Limpamos a chunk atual.
		self.chunk.clear();

		# Aqui vamos criar uns bloquinhos e bem simples mesmo, so para testar chunk.
		for s in range(size):
			_block = block.Block("dirty", "textures/blocks/");
			_block.aabb.min.x, _block.aabb.min.y, _block.aabb.min.z = s - 1, 1, 1;

			self.chunk.append(_block);

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

	def update_render_3d(self):
		for blocks in self.chunk:
			if self.main.player.camera():
				if blocks.camera_in(self.main.camera_manager):
					print("w")

			blocks.on_render();