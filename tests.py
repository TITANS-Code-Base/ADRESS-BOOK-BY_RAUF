import unittest
import json

from entities import Person
from service import (
    create_person,
    get_db,
    save_to_db
)


class EntityTest(unittest.TestCase):

    def test_create_person(self):
        john=Person(name="John", surname="Doe", number="+100000000")
        john_as_dict = {
            "name" : "John",
            "surname" : "Doe",
            "number" : "+100000000",
        }
        self.assertEqual(john_as_dict, john.as_dict())


class ServiceTest(unittest.TestCase):

    def test_create_person(self):
        p1 = Person(name="john", surname="doe", number="+1")
        p2 = create_person(name="john", surname="doe", number="+1")
        self.assertEqual(p1.name,p2.name)
        self.assertIsInstance(p2, Person)
    
    def test_get_db(self):
        people=get_db()
        self.assertIsInstance(people, list)
    
    def test_save_to_db(self):
        p1=Person(name="john", surname="doe", number="+1")
        saved, person = save_to_db(p1)
        self.assertEqual(True, saved)
        self.assertIsInstance(person, Person)

if __name__ == "__main__":
    unittest.main()