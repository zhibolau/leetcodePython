from pymongo import MongoClient

# 创建MongoDB客户端
client = MongoClient('localhost', 27017)
db = client.mydatabase
collection = db.mycollection
doc = {"name": "Tom", "age": 20}
collection.insert_one(doc)
result = collection.find_one({"name": "Tom"})
print(result)


"""
Zhibos-MBP:mongoDB ZhiboLIU$ python3 monTest.py 
{'_id': ObjectId('65135144cd6d4ba450b4de08'), 'name': 'Tom', 'age': 20}
"""