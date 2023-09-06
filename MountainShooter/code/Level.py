#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


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
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):

        # pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        # pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            # DESENHAR NA TELA
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) #mostra as imagens do fundo.
                ent.move()
                if isinstance(ent,(Player, Enemy)):
                    self.entity_list.append(ent.shoot())
            # texto para ser printado na tela
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (30, 10))  # apresentar o fps na tela
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (60, 20))
            # CONFERIR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            # ATUALIZAR TELA
            pygame.display.flip()

            # VERIFICAR RELACIONAMENTOS DE ENTIDADES
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self,text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect( center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
