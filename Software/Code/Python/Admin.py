import os
import psycopg2

def printf(str):
    # Output: more friendlier interface
    pass
    #col = os.get_terminal_size().columns
    #print(str.center(col))

def monitoring():
    # Input: postgre or excel
    # Output: Informations 
    os.system("clear")
    print("Monitoring interface")

    # At the moment
    print("1. Numbers of cars")
    # postgre code

    print("2. History")
    # postgre code

    # At the moment
    print("3. Total of money")
    # postgre code

    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0

def informations():
    # Input: postgre or excel
    # Output: Informations
    os.system("clear")
    # postgre code 

    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def sale():
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="parking_db_last")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from sale"
    cursor.execute(postgreSQL_select_Query)
    sale = cursor.fetchall()
    print("                  This Monitor Sale             ")
    print("----------------------------------------------------")
    for row in sale:
            print("Day : ",row[0])
            print("Sale In Day : ",row[1])
            print("Month : ", row[2])
            print("Sale In Month : ",row[3])
            
    conn.commit()
    conn.close()
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def admin():
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="parking_db_last")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from admin"
    cursor.execute(postgreSQL_select_Query)
    admin = cursor.fetchall()
    print("                  This Monitor Admin             ")
    print("----------------------------------------------------")
    for row in admin:
            print("ID RIF : ",row[0])
            print("Member ID : ",row[1])
            print("Full Name : ", row[2])
            
    conn.commit()
    conn.close()
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def security():
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="parking_db_last")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from security"
    cursor.execute(postgreSQL_select_Query)
    secu = cursor.fetchall()
    print("                  This Monitor Security             ")
    print("----------------------------------------------------")
    for row in secu:
            print("ID RIF : ",row[0])
            print("Money Pay : ",row[1])
            print("Transaction id : ", row[2])
            print("Time in : ",row[3])
            print("Time Out : ", row[4])
            
    conn.commit()
    conn.close()
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0

def menu():
    os.system("clear")
    print("Welcome to project ")
    check = 1
    while (check):
        print("Admin interface")
        print("1. Monitoring")
        print("2. Customers Information")
        print("3. Security Screen")
        print("4. Sale")
        print("5. Admin")
        print("Your choice: ", end = "")
        choice = input()
        if choice == '1':
            check = monitoring()
        elif choice == '2':
            check = informations()
        elif choice == '3':
            check = security()
        elif choice == '4':
            check = sale()
        elif choice == '5':
            check = admin()
        os.system("clear")

def main():
    menu()

if __name__ == '__main__':
    main()
