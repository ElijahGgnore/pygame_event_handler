import pygame
from .KeyManager import KeyManager


# TODO: Documentation
class EventHandler:
    def __init__(self):
        self.connected_callables = {}
        self.loop_start_methods = set()

        self.key_manager = KeyManager()
        self.connect_callable(pygame.KEYUP, self.key_manager.update)
        self.connect_callable(pygame.KEYDOWN, self.key_manager.update)

    def update(self):
        self.key_manager.event_loop_start()
        for e in pygame.event.get():
            t = e.type
            if t in self.connected_callables:
                for c in self.connected_callables[t]:
                    c(e)

    def connect_callable(self, event_type, callable_):
        if event_type not in self.connected_callables:
            self.connected_callables[event_type] = set()
        self.connected_callables[event_type].add(callable_)

    def disconnect_callable(self, event_type, callable_):
        if event_type in self.connected_callables:
            self.connected_callables[event_type].discard(callable_)
            if len(self.connected_callables[event_type]) == 0:
                self.connected_callables.pop(event_type)


event_handler_instance = EventHandler()
