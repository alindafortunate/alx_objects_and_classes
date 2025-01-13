# Testing my knowledge of the classes and objects.
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        return (
            f"I am {self.name} {self.age} years and my occupation is {self.occupation}"
        )

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        return f"My new occupation is {new_occupation}"


person1 = Person("Fortunate", 19, "Software Developer")
introduction = person1.introduce()
print(introduction)
new_occupation = person1.change_occupation("Founder")
print(new_occupation)
