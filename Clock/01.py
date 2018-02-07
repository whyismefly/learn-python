#!/usr/bin/python
# encoding:utf-8

import pygame

import time

import datetime

pygame.mixer.init()

pygame.mixer.music.load('0.mp3')

h = '07'

m = '30'

while True:

    time.sleep(1)

    now_h = datetime.datetime.now().strftime('%H')

    now_m = datetime.datetime.now().strftime('%M')

    if h == now_h and m == now_m:

            pygame.mixer.music.play()

            time.sleep(60)