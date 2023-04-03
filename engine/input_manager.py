"""This implementation uses the pygame library to handle mouse and keyboard input.
The update() method is called once per frame to update the input state, and the various methods
such as is_key_pressed() and is_action_pressed() can be used to check the current input state.

The load_configurations() method loads input configurations from a file in the "volume" structure you described,
with each line in the file containing an action name followed by a comma-separated list of keys that map to that action.
The is_action_pressed() method checks if any of the keys associated with a given action are currently pressed.

Note that this is just a basic implementation and may need to be expanded or modified based on the specific needs of
your game."""


import pygame


class InputManager:
    def __init__(self):
        # Initialize input variables
        self.actions = None
        self.mouse_pos = (0, 0)
        self.left_mouse_down = False
        self.right_mouse_down = False
        self.left_mouse_pressed = False
        self.right_mouse_pressed = False
        self.keys_pressed = set()
        self.keys_just_pressed = set()

        # Load input configurations from file
        self.load_configurations()

    def update(self):
        # Update mouse position and button states
        self.mouse_pos = pygame.mouse.get_pos()
        self.left_mouse_pressed = False
        self.right_mouse_pressed = False

        for event in pygame.event.get():
            # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.left_mouse_down = True
                    self.left_mouse_pressed = True
                elif event.button == 3:
                    self.right_mouse_down = True
                    self.right_mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.left_mouse_down = False
                elif event.button == 3:
                    self.right_mouse_down = False

            # Handle key events
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)
                self.keys_just_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)

    def is_key_pressed(self, key):
        return key in self.keys_pressed

    def is_key_just_pressed(self, key):
        return key in self.keys_just_pressed

    def load_configurations(self):
        # Load input configurations from file
        with open('input_manager.configurations', 'r') as f:
            lines = f.readlines()

        self.actions = {}
        for line in lines:
            parts = line.strip().split(':')
            action = parts[0]
            keys = [int(k.strip()) for k in parts[1].split(',')]
            self.actions[action] = keys

    def is_action_pressed(self, action):
        keys = self.actions.get(action, [])
        for key in keys:
            if key in self.keys_pressed:
                return True
        return False
