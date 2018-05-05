#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

def get_conn():
    return pymysql.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = '1234',
        database = 'scrapy',
        charset = 'utf8' # 注意： 一定要添加此参数， 不然pymysql 会以默认的latin1连接数据苦导致中文乱码
    )

def insert():
    sql_str = "insert tb_news(title, src, time, url) values('数据库添加测试', 'yungyu', '20180501 10:12:41', 'http://yungyu.per/gg')"
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql_str)
        conn.commit()
    except:
        conn.rollback()
        print '添加数据失败'
        raise
    finally:
        cur.close()
        conn.close()

def select():
    sql_str = "select id, title, src, time, url from tb_news"
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()

    print rows
    cur.close()
    conn.close()

def update():
    sql_str = "update tb_news set title='数据库更新测试' where id=1"
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql_str)
        conn.commit()
    except:
        conn.rollback()
        print '更新失败'
        raise
    finally:
        cur.close()
        conn.close()

conn = get_conn()
print conn
insert()
# select()
update()
select()