import pygame


# TODO: Documentation
class KeyManager:
    def __init__(self):
        self.last_pressed_keys = set()
        self.pressed_keys = set()

    def update(self, key_event):
        if key_event.type == pygame.KEYDOWN:
            self.pressed_keys.add(key_event.key)
        elif key_event.type == pygame.KEYUP:
            self.pressed_keys.discard(key_event.key)

    def event_loop_start(self):
        self.last_pressed_keys = self.pressed_keys.copy()

    def key_just_released(self, key):
        return key not in self.pressed_keys and key in self.last_pressed_keys

    def key_just_pressed(self, key):
        return key in self.pressed_keys and key not in self.last_pressed_keys

    def key_pressed(self, key):
        return key in self.pressed_keys

    def clear_pressed(self):
        self.last_pressed_keys.clear()
        self.pressed_keys.clear()
