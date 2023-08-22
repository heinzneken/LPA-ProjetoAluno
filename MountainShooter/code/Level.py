#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))


        # poderia ser feito desta forma, ou uma forma mais reduzida conforme mostrado acima, este codigo é relacionado
        # com o codigo EntityFactory.py
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg0'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg1'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg2'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg3'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg4'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg5'))
        # self.entity_list.append(EntityFactory.get_entity('Level1Bg6'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

