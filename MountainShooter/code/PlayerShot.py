from code.Entity import Entity


class PlayerShot(Entity):

    def __int__(self, name: str, position: tuple):
        super().__int__(name, position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]