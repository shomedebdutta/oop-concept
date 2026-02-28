class Bird:
    def sound(self):
        return "Chirp"


class Cat:
    def sound(self):
        return "Meow"


class Dog:
    def sound(self):
        return "Woof"


def make_sound(animal):
    print(animal.sound())


# Example usage
if __name__ == "__main__":
    bird = Bird()
    cat = Cat()
    dog = Dog()

    make_sound(bird)
    make_sound(cat)
    make_sound(dog)
