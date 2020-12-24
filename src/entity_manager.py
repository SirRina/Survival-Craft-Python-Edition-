class EntityManager:
	def __init__(self, main):
		self.main = main;

	def on_update(self):
		for entities in self.main.loaded_entity_list:
			if entities.rendering:
				if entities.get_health() <= 0:
					entities.set_living(False);

				if entities.camera():
					entities.yaw   = self.main.camera_manager.get_yaw_pitch()[0];
					entities.pitch = self.main.camera_manager.get_yaw_pitch()[1];

					# Eu poderia usar a coisa mas nao vai k
					entities.position.x = self.main.camera_manager.x;
					entities.position.y = self.main.camera_manager.y;
					entities.position.z = self.main.camera_manager.z;

	def on_render(self):
		for entities in self.main.loaded_entity_list:
			if entities.rendering:
				entities.render();