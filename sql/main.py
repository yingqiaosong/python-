import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     user='username',
                     password='userpassword',
                     database='databasename')
# 获取操作游标
cursor = db.cursor()

# 插入操作
sql = "INSERT INTO employee(employee_id,name,age,income)\
       values({id},{name},{age},{income})"\
       .format(id=8, name="\"trump\"", age=70, income=1)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 向数据库提交
    db.commit()
except:
    # 发生错误则回滚
    db.rollback()
    print("Fail to insert!")
# commit 和 rollback 构成事务管理

# 查询操作,用format 字符串实现 动态语句

sql = "SELECT name,age FROM employee \
        WHERE employee.income > {inc}".format(inc=1000)
try:
    # 执行sql
    cursor.execute(sql)
    # 获取所有结果
    results = cursor.fetchall()
    # 遍历输出
    for row in results:
        name_ = row[0]
        age_ = row[1]
        print("name = {},age = {}".format(name_,age_))
except:
    print("Error:unable to fetch")

# 更新

sql = "UPDATE EMPLOYEE SET AGE = AGE + {delta} WHERE income >={inc}"\
    .format(delta=1, inc=20000)
try:
    cursor.execute(sql)
    db.commit()
except:
    print("Error in update!")
    db.rollback()

# 删除
sql = "DELETE FROM EMPLOYEE WHERE employee_id = {id_}".format(id_=8)
try:
    cursor.execute(sql)
    db.commit()
except:
    print("Error when delete")
    db.rollback()
# 关闭连接
db.close()
