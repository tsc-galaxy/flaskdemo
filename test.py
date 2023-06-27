import pymysql

if __name__=='__main__':
#  1、连接到数据库
    con = pymysql.connect(host='127.0.0.1',
                port=3308,
                user='root',
                password='root',
                database='weibodemo',
                charset='utf8')
# 2、创建一个游标 cursor
    cur = con.cursor()
# 3、执行对应的sql语句  execute()
    sql = 'select * from user where password="123" '
# 查询到的数据条数
    res = cur.execute(sql)
    print(res)
# 4、获取查询到的数据
# 方法二：获取所有的查询数据
    data = cur.fetchall()
    print(data)
