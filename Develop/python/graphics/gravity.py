from pygame import surface
from pygame import gfxdraw
import pygame

s = surface.Surface((200, 200))
gfxdraw.pixel(s, 20, 20, pygame.color.Color(100, 100, 100))
s.