import pymongo


class mongo:
    host = 'mongodb://127.0.0.1:27017'
    db_name = 'AppRank'
    cluster_name = ['video', 'edu']

    def __init__(self):
        client = pymongo.MongoClient(self.host)
        db = client[self.db_name]
        self.cluster0 = db[self.cluster_name[0]]
        self.cluster1 = db[self.cluster_name[1]]
