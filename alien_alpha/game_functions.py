import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

from alien_creator import *


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ 响应 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        elif event.type ==pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_click_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):

    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if not stats.game_active:
            start_new_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        else:
            fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
        if not stats.game_active:
            start_new_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        #else:
        #    fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: # event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):

    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_click_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if play_button_clicked and not stats.game_active:
        start_new_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

def start_new_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    ai_settings.initialize_dynamic_settings()

    stats.reset_stats()
    stats.game_active = True

    sb.prep_all()

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, stats, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # repaint
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    # aliens.draw(screen)
    
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()      
     
    # visual
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ create a bullet, add it into group"""
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
    if len(aliens) == 0:
        refresh_next_fleet(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:
        stats.ships_left -= 1
    
        aliens.empty()
        bullets.empty()

        sleep(1.0)

        create_fleet(ai_settings, stats, screen, ship, aliens)
        ship.center_ship()

    else:
        stats.game_active = False

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def refresh_next_fleet(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.empty()
    stats.level += 1
    if stats.level>3 and stats.level%5!=0:
        ai_settings.increase_speed()
    sb.prep_level()
    create_fleet(ai_settings, stats, screen, ship, aliens)
