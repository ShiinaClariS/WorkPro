package com.mongo.servlet1;

import com.mongodb.MongoClient;
import com.mongodb.MongoException;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

public class MongoConn {
    public String getData() {
        String data = "";
        try {
            //连接MongoDB
            MongoClient client = new MongoClient("localhost", 27017);
            //打开数据库
            MongoDatabase db = client.getDatabase("BilibiliRankDB");
            //打开集合
            MongoCollection<Document> collection = db.getCollection("BInfo");
            //获取文档
            FindIterable<Document> iterable = collection.find();
            //迭代返回文档信息
            MongoCursor<Document> iterator = iterable.iterator();
            while (iterator.hasNext()) {
                data = data.concat(iterator.next().toJson());
                data = data.concat("\n");
            }
            return data;
        } catch (MongoException e) {
            System.out.println(e);
        }
        return null;
    }
}
