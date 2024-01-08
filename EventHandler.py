import pygame
from .KeyManager import KeyManager


# TODO: Documentation
class EventHandler:
    def __init__(self):
        self.connected_methods = {}
        self.loop_start_methods = set()

        self.key_manager = KeyManager()
        self.connect_method(pygame.KEYUP, self.key_manager.update)
        self.connect_method(pygame.KEYDOWN, self.key_manager.update)

    def update(self):
        self.key_manager.event_loop_start()
        for e in pygame.event.get():
            t = e.type
            if t in self.connected_methods:
                for m in self.connected_methods[t]:
                    m(e)

    def connect_method(self, event_type, method):
        if event_type not in self.connected_methods:
            self.connected_methods[event_type] = set()
        self.connected_methods[event_type].add(method)

    def disconnect_method(self, event_type, method):
        if event_type in self.connected_methods:
            self.connected_methods[event_type].discard(method)
            if len(self.connected_methods[event_type]) == 0:
                self.connected_methods.pop(event_type)


event_handler_instance = EventHandler()
