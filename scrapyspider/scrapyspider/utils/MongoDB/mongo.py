import pymongo


class mongo:
    mongo_connect = 'mongodb://127.0.0.1:27017'
    db_name = 'BilibiliRankDB'
    cluster_name = 'BInfo'

    def __init__(self):
        client = pymongo.MongoClient(self.mongo_connect)
        db = client[self.db_name]
        self.cluster = db[self.cluster_name]
