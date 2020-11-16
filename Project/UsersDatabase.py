import sqlite3

def write_database(iden, Name, addr, num, readkey, writekey, sp):
    Id=iden
    name= Name
    address= addr
    phone= num
    Rkey= readkey
    Wkey= writekey
    specs= sp
    dbconnect = sqlite3.connect("users.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute('''INSERT INTO users values(?, ?, ?, ?, ?, ?, ?);''', (Id, name, address, phone, Rkey, Wkey, specs));
    dbconnect.commit();
    dbconnect.close();

#write_database("1", "A", "A", "A", "A", "A", "A")


def read_database(key):
    Id = key
    dbconnect = sqlite3.connect("users.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute('SELECT * FROM users WHERE ID = ?', (Id,));
    
    for row in cursor:
        return(row['readKey']);
    
    dbconnect.close();
    