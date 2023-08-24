import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234")
m = mydb.cursor()

def opt1():
    q=input("Enter desired team: ")
    m.execute(("SELECT * FROM Flight WHERE Team_01 = %s OR Team_02 = %s;"),(q,q))
    result = m.fetchall()
    for x in result:
        print(x)
def opt2():
    q2=input("Enter desired Location: ")
    m.execute(("SELECT * FROM Flight WHERE Match_Location=%s"),(q2,))
    for x in m:
        print(x)
def opt3():
    q3=input("Enter desired Timming (DAY/DAY-NIGHT): ")
    m.execute(("SELECT * FROM Flight WHERE Timming=%s"),(q3,))
    result=m.fetchall()
    for x in result:
        print(x)

print("ISHANI JAISWAL       E22CSEU0442")
m.execute("use agnm")
while True:
    print("CHOOSE FROM THE FOLLOWING OPTIONS: ")
    print("1.List of all the matches of a Team \n2. List of Matches on a Location \n3. List of Matches based on timing \n4.Exit")
    a=int(input("Enter option number: "))
    if a==1:
        opt1()
    elif a==2:
        opt2()
    elif a==3:
        opt3()
    else:
        break
    p=input("Do you want to choose again (y/n)")
    if p=='y':
        continue
    else:
        break