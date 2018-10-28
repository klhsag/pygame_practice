
from time import sleep

from alien import Alien

def create_alien(ai_settings, stats, screen, aliens, alien_number_x, alien_number_y):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width * (0.5 + 2*alien_number_x)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height * ( - stats.level/2.5 + 2*alien_number_y)
    aliens.add(alien)

def create_fleet(ai_settings, stats, screen, ship, aliens):
    """ create a group of aliens """

    # sleep(0.5)

    alien = Alien(ai_settings, screen)
    alien_tot_x = get_alien_xmax(ai_settings, alien.rect.width)
    alien_tot_y = get_alien_ymax(ai_settings, ship.rect.height, alien.rect.height)

    alien_tot_y += int(stats.level/5)

    for alien_number_x in range(alien_tot_x):
        for alien_number_y in range(alien_tot_y):
            create_alien(ai_settings, stats, screen, aliens, alien_number_x, alien_number_y)

def get_alien_xmax(ai_settings, alien_width):
    """ """
    avl_s_x = ai_settings.screen_width - 2*alien_width
    n_a_x = int(avl_s_x / (2*alien_width) )
    return n_a_x

def get_alien_ymax(ai_settings, ship_height, alien_height):
    avl_s_y = ai_settings.screen_height - 0*alien_height - 2*ship_height
    n_y = int(avl_s_y / (2*alien_height))
    return n_y
