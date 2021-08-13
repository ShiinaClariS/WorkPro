from ExvelUplaod import MongoConn
import pandas as pd
import numpy as np


class UplaodToMongoDB:
    file_path = r'W:/ScrapyTest/ExvelUplaod/rankdata.xlsx'
    mongo = MongoConn.mongo()

    def __init__(self):
        self.data = pd.read_excel(self.file_path)

    def uplaod(self):
        data_list = list(self.data.loc[i] for i in range(len(self.data)))
        for d in data_list:
            item = dict(d)
            item['序号'] = int(item['序号'])
            # item.update({'_id': str(item['序号'])})
            if isinstance(item['pc软件'], np.ndarray):
                item['pc软件'] = int(item['pc软件'])

            if d['榜单名称'] == '影音大全':
                self.mongo.cluster0.insert_one(item)
            elif d['榜单名称'] == '满分教育':
                self.mongo.cluster1.insert_one(item)


UplaodToMongoDB().uplaod()
