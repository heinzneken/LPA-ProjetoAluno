#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #se a tecla seta para cima for pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: #se a tecla seta para cima for pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: #se a tecla seta para cima for pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: #se a tecla seta para cima for pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
            return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx,self.rect.centery))