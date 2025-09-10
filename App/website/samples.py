import sqlite3
import hashlib


def read_user_data():
    connection = sqlite3.connect("user_data.db")
    cur = connection.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            money VARINT(255) NOT NULL
        )
        """)
    
    cur.execute('SELECT * FROM user_data')
    userdata = cur.fetchall()

    connection.close()
    
    return userdata


def check_user(gmail):
    users = read_user_data()

    for user_data in users:
        if user_data[3] == gmail:
            return True
    
    return False


def valid_data(datas):
    for data in datas:
        if len(data) < 3:
            return (False, "Invalid Length")
    
    if check_user(datas[2]):
        return (False, "Email In Use")

    return (True, None)


def valid_login(gmail, password):
    users = read_user_data()
    hex_password = hashlib.sha256(password.encode()).hexdigest()

    for user_data in users:
        if user_data[3] == gmail:
            if user_data[4] == hex_password:
                return (True, None)
            else:
                return (False, "Wrong Password")          

    return (False, "Email Not Found")


def create_user(name, surname, username, password):
    connection = sqlite3.connect("user_data.db")
    cur = connection.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        money VARINT(255) NOT NULL
    )
    """)

    hex_password = hashlib.sha256(password.encode()).hexdigest()

    cur.execute("INSERT INTO user_data (name, surname, username, password, money) VALUES (?, ?, ?, ?, ?)", (name, surname, username, hex_password, 0))

    connection.commit()


def retrive_data(gmail):
    data = read_user_data()

    for user in data:
        if user[3] == gmail:
            return user
    
    return False


def check_valid_date(date):
    for x in date.split("/"):
        print(x.isnumeric())
        if not x.isnumeric() or int(x) > 12:
            return False
        
    return True


def update_bank(gmail, value):
    user_data = retrive_data(gmail)
    bank = user_data[5] + value

    connection = sqlite3.connect("user_data.db") 
    cur = connection.cursor()
    
    update = f"UPDATE user_data SET money = '{bank}' WHERE id = {user_data[0]}"

    cur.execute(update)

    connection.commit()
    connection.close()
