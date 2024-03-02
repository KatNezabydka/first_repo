"""
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white',і 
метод change_color, який повинен змінювати значення змінної класу color.

Створіть екземпляри об'єкта: first_animal та second_animal

Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal та змініть значення змінної класу color на "red".
"""
class Animal:
    colour = "white"
    
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        
    def say(self):
        pass
    
    def change_weight(self, new_weight):
        self.weight = new_weight
    
    def change_color(self, colour):
        Animal.colour = colour
    
first_animal = Animal("Musia", 3.9)
second_animal = Animal("Pusia", 2.1)
Animal.colour = "red"
print(first_animal.colour, second_animal.colour)
