#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

class MysqlPipline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = 'root',
            password = '1234',
            database = 'scrapy',
            charset = 'utf8'
        )

    def process_item(self, item, spilder):
        sql_str = 'insert tb_news(title, src, time, url) values(%s, %s, %s, %s)'
        
        cur = self.conn.cursor()
        try:
            cur.execute(sql_str,(
                item['title'],
                item['src'],
                item['time'],
                item['url']
            ))
            self.conn.commit()
        except:
            self.conn.rollback()
            print '添加数据到数据库失败'
            raise
        finally:
            cur.close()
