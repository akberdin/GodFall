"""The asset_manager.py is responsible for loading and managing game assets such as images,
sounds, fonts, and other resources


In this example, we have a class called AssetManager that has three attributes: images, sounds, and fonts,
which are dictionaries to store the loaded assets. The __init__ method initializes these attributes as
empty dictionaries.

The load_images, load_sounds, and load_fonts methods are used to load the specific types of assets from the asset files.
The image_list, sound_list, and font_list parameters are lists of filenames for each type of asset.

The loaded assets are stored in the corresponding dictionaries with the asset name as the key.
The convert_alpha method is used for loading images to optimize their rendering performance.

With this asset_manager.py code, we can easily load and manage game assets from the assets folder.
"""


import pygame


class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def load_images(self, image_list):
        for image_name in image_list:
            self.images[image_name] = pygame.image.load(f"assets/images/{image_name}.png").convert_alpha()

    def load_sounds(self, sound_list):
        for sound_name in sound_list:
            self.sounds[sound_name] = pygame.mixer.Sound(f"assets/sounds/{sound_name}.wav")

    def load_fonts(self, font_list):
        for font_name, font_size in font_list.items():
            self.fonts[font_name] = pygame.font.Font(f"assets/fonts/{font_name}.ttf", font_size)