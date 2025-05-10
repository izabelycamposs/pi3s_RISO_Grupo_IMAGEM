import pymongo

def mongoConnection(collection):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["riso"]
    mycol = mydb[collection]
    return mycol

def mongoInsert(collection, data):
    mycol = mongoConnection(collection)
    x = mycol.insert_one(data)
    return x.inserted_id

def mongoFind(collection, query):
    mycol = mongoConnection(collection)
    x = mycol.find(query)
    return x

def mongoUpdate(collection, query, newvalues):
    mycol = mongoConnection(collection)
    x = mycol.update_one(query, newvalues)
    return x.modified_count

def mongoDelete(collection, query):
    mycol = mongoConnection(collection)
    x = mycol.delete_one(query)
    return x.deleted_count

def mongoFindAll(collection):
    mycol = mongoConnection(collection)
    x = mycol.find()
    return x

def mongoFindOne(collection, query):
    mycol = mongoConnection(collection)
    x = mycol.find_one(query)
    return x

def mongoCount(collection, query):
    mycol = mongoConnection(collection)
    x = mycol.count_documents(query)
    return x

def mongoAggregate(collection, pipeline):
    mycol = mongoConnection(collection)
    x = mycol.aggregate(pipeline)
    return x

def mongoDistinct(collection, field):
    mycol = mongoConnection(collection)
    x = mycol.distinct(field)
    return x
