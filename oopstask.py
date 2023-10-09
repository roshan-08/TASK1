import pymongo

class classmongo:
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        self.collection.insert_many(data)

    def update_data(self, previous_update,after_update):
        self.collection.update_one(previous_update,after_update)

    def insert_single_data(self, data):
        self.collection.insert_one(data)

    def delete_data(self, delettte):
        self.collection.delete_one(delettte)

if __name__ == "__main__":
    print("Welcome")

    manager = classmongo("maindatabase", "collectionofdb2")

    # multiple value inserting
    # insert_data = [
    #     {'_id': 1, 'name': 'roshan', 'location': 'gullady', 'marks': 34},
    #     {'_id': 2, 'name': 'koushik', 'location': 'beloor', 'marks': 54},
    #     {'_id': 3, 'name': 'ganesh', 'location': 'barkur', 'marks': 74},
    #     {'_id': 4, 'name': 'sathish', 'location': 'beloor', 'marks': 64},
    #     {'_id': 5, 'name': 'roshan', 'location': 'gullady2', 'marks': 34},
    #     {'_id': 6, 'name': 'roshan', 'location': 'gullady3', 'marks': 34},
    #     {'_id': 7, 'name': 'roshan', 'location': 'gullady4', 'marks': 34},
    #     {'_id': 8, 'name': 'roshan', 'location': 'gullady5', 'marks': 34},
        
    # ]

    # manager.insert_data(insert_data)

    # previous_update = {'name': 'koushik'}
    # after_update = {"$set": {'marks': 90}}
    # manager.update_data(previous_update, after_update)

    # inserting the single data 
    # single_data = {'_id': 9, 'name': 'sathish', 'location': 'kundapura', 'marks': 99}
    # manager.insert_single_data(single_data)

    delettte= {'name':'sathish'}
    manager.delete_data(delettte)