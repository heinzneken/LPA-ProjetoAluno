#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), list_bg=None):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            # poderia ser feito desta forma, ou uma forma mais reduzida conforme mostrado acima, este codigo é relacionado
            # com o codigo Level.py
            # case "Level1Bg0":
            #     return Background(f'Level1Bg0', position)
            # case "Level1Bg1":
            #     return Background(f'Level1Bg1', position)
            # case "Level1Bg2":
            #     return Background(f'Level1Bg2', position)
            # case "Level1Bg3":
            #     return Background(f'Level1Bg3', position)
            # case "Level1Bg4":
            #     return Background(f'Level1Bg4', position)
            # case "Level1Bg5":
            #     return Background(f'Level1Bg5', position)
            # case "Level1Bg6":
            #     return Background(f'Level1Bg6', position)

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0+40, WIN_HEIGHT - 40)))
