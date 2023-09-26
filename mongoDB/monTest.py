#pip3 install pymongo
#install on mac
# brew cask install gcollazo-mongodb

from pymongo import MongoClient

# 创建MongoDB客户端
client = MongoClient('localhost', 27017)
db = client.mydatabase
collection = db.mycollection
doc = {"name": "Tom", "age": 20}
collection.insert_one(doc)
result = collection.find_one({"name": "Tom"})
print(result)


documents = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 40}
]
collection.insert_many(documents)

# 查询所有文档
results = collection.find()
for result in results:
    print(result)

# 查询特定条件的文档
query = {"age": {"$gt": 30}}
results = collection.find(query)
for result in results:
    print(result)
    
# 更新单个文档
query = {"name": "Alice"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)

# 更新多个文档
query = {"age": {"$lt": 30}}
new_values = {"$set": {"age": 31}}
collection.update_many(query, new_values)

# 删除单个文档
query = {"name": "Alice"}
collection.delete_one(query)

# 删除多个文档
query = {"age": {"$gt": 40}}
collection.delete_many(query)

# 关闭连接
client.close()


"""
Zhibos-MBP:mongoDB ZhiboLIU$ python3 monTest.py 
{'_id': ObjectId('65135144cd6d4ba450b4de08'), 'name': 'Tom', 'age': 20}
"""