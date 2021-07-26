import json
from service import (
    create_person,
    get_db,
    save_to_db,
    update_db
)

texts = {
    "welcome" : "Welcome to Address Book. You can add/get/update/delete people from your terminal",
    "action_helper" : "Choose 1 for adding new person, 2 for searching, 3 for updating and 4 for deleting.",
    "action_create": "Cool! Now, you will add new person. Please follow the steps.",
    "action_create_success" : "Nice job! You have added new person.",
}

print(texts["welcome"])
print(texts["action_helper"])

action_type = input("Choose next step: ")

if action_type == "1":
    print(texts["action_create"])
    name = input("Add person name: ")
    surname = input("Add person surname: ")
    number = input("Add number: ")
    new_person = create_person(name,surname,number)
    saved, person = save_to_db(new_person)
    if saved:
        print(texts["action_create_success"])

elif action_type == "2":
    people=get_db()
    for person in people:
        print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')
        print("---")

elif action_type == "3":
    person_name=input("Please, enter name which you want to update: ")
    people=get_db()
    for person in people:
        if person['name'] == person_name:
            print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')
            new_data = input("what do you want to change?(for name select 1, surname select 2, number select 3): ")
            if new_data == "1":
                new_name = input("Please, add person new name: ")
                person["name"] = new_name
                update_db(person)
                print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')
            elif new_data == "2":
                new_surname = input("Please, add person new surname: ")
                person["surname"] = new_surname
                update_db(person)
                print(texts["action_create_success"])
                print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')
            elif new_data == "3":
                new_number = input("Please, add person new number: ")
                person["number"] = new_number
                update_db(person)
                print(texts["action_create_success"])
                print(f'Name: {person["name"]} , Surname: {person["surname"]}, Number: {person["number"]}')

elif action_type == "4":
    person_name=input("Please, enter name which you want to delete: ")
    people=get_db()
    try:
        for person in people:
            if person['name'] == person_name:
                people.remove(person)
                json.dump(people, open('db/db.json','w'))
                print(texts["action_create_success"])
    except:
        print("Please, enter right value")
        