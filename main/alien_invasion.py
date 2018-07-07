import pygame
from main.settings import Settings
from main.ship import Ship
import main.game_functions as gf
from pygame.sprite import Group
from main.game_stats import GameStats
from main.button import Button
from main.scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    # 穿件一个用于储存子弹的编组
    bullets = Group()
    aliens = Group()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("亓澎湃 · 星际迷航")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    # 穿件一个外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建存储游戏信息的实例，穿件计分板
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()