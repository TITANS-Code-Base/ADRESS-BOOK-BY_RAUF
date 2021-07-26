class Person:
    def __init__(self, name, surname, number):
        self.name=name
        self.surname=surname
        self.number=number

    def as_dict(self):
        return {
            "name" : self.name,
            "surname" : self.surname,
            "number" : self.number, 
        }