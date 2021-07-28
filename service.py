import json

from entities import Person


def create_person(name, surname, number):
    return Person(name=name, surname=surname, number=number)

def get_db():
    with open("db/db.json", "r") as file:
        people = json.loads(file.read())
    return people


def save_to_db(person):
    try:
        with open("db/db.json", "r") as file:
            people = json.loads(file.read())

        people.append(person.as_dict())

        with open("db/db.json", "w+") as file:
            file.write(json.dumps(people))
        return (True, person)
    except:
        return (False, None)

def update_db(person):
    with open("db/db.json", "w") as file:
        json.dump(person, file)
                
    