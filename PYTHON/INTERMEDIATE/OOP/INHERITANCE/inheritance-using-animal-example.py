class Animal:
    def __init__(self):
        self.num_eyes = 2
        print(f"Number of eyes {self.num_eyes}")
    def breathe(self):
        print("Inhale", "Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing this underwater")
    def swim(self):
        print("Fish can swim in the water")

fish = Fish()
fish.swim()
fish.breathe()