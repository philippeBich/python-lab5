import pymysql

# DATABASE functions

# ---GETTING---

# 1) Get a task

def getTasks():

    sql = "SELECT text FROM tasks"

    conn = pymysql.connect(user='root', password='root',
                           database='lab4', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()

    res = []
    for row in result:
        res.extend(row)

    return res


# 2) Get urgency

def getUrgency(task):
    sql="select urgent from tasks where text=%s"
    conn = pymysql.connect(user='root', password='root',
                           database='lab4', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    result=cursor.fetchone()[0]
    # We do not want the extra comma

    conn.close()
    return result

# 3) Get ID

def getId(task):
    sql = "select id_task from tasks where text=%s"
    conn = pymysql.connect(user='root', password='root',
                           database='lab4', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    result = cursor.fetchone()[0]
    conn.close()
    return result


# ---ADDING---

# 4) Add a new task

def addTask(task):
    sql="insert into tasks (text) values (%s)"

    conn = pymysql.connect(user='root', password='root',
                           database='lab4', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (task,))
    conn.close()


# ---DELETING---

# 5) Delete Task

def deleteTask(id):
    sql = "delete from tasks where id_task=%s"

    conn = pymysql.connect(user='root', password='qwertyuiop',
                           database='lab4', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.close()