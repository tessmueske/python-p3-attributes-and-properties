#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Otto", breed="Mastiff"):
        self.set_name(name)
        self.set_breed(breed)

    def set_breed(self, breed="Mastiff"):
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def set_name(self, name="Otto"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")