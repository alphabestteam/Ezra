import pymongo

def print_database(mydb):
    for collections in mydb.list_collection_names():
        for document in mydb[collections].find():
            print(document)

def main():
    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    mydb = client["Aviv's_people"]
    family = mydb["family"]
    friends = mydb["friends"]
    army = mydb["army"]

    army_group = [
        {"name": "Aviv", "age": 20, "role": "Backend"},
        {"name": "Lihi", "age": 21, "role": "QA"},
        {"name": "Gabi", "age": 22, "role": "DevOps"},
        {"name": "Ori", "age": 23, "role": "Frond-end"},
        {"name": "Ido", "age": 22, "role": "developer"},
        {"name": "Yarden", "age": 24, "role": "DevOps"},
    ]

    family_group = [
        {"name": "mother", "age": 45, "role": "teacher"},
        {"name": "father", "age": 46, "role": "engineer"},
        {"name": "brother", "age": 12, "role": "school"},
        {"name": "sister", "age": 24, "role": "student"},
    ]

    friends_group = [
        { "_id": 1, "name": "Amit", "age": 20, "role": "waiter"},
        { "_id": 2, "name": "Yonatan", "age": 24, "role": "doctor"},
        { "_id": 3, "name": "Noa", "age": 22, "role": "student"},
        { "_id": 4, "name": "Michal", "age": 21, "role": "baker"},
    ]

    x = army.delete_many({})
    y = family.delete_many({})
    z = friends.delete_many({})
    
    # first way
    for person in army_group:
        army_insert = army.insert_one(person)

    # second way
    family_insert = family.insert_many(family_group)

    # third way
    friends_insert = friends.insert_many(friends_group)

    print_database(mydb)

    print('deleting Lihi')
    my_query = {"name" : "Lihi"}
    army.delete_one(my_query)

    print_database(mydb)

if __name__ == "__main__":
    main()
