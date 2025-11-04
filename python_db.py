import mysql.connector 
from tabulate import tabulate

def open_db():
    global mydb
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "Shaggy123!",
    database = "test"
)
    global mycursor
    mycursor = mydb.cursor()





def printFormat(result):
    header = []

    #get headers
    for cd in mycursor.description:
        header.append(cd[0])
    print('')
    print('Query Result')
    print('')

    return(tabulate(result, headers=header))

def executeSelect(query):
    mycursor.execute(query)
    res = printFormat(mycursor.fetchall())
    return res

#open_db()

#print(executeSelect('Select * from Employee'))