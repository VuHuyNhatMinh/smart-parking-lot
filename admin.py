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
def security():
    conn = psycopg2.connect(user="postgres", password="1", database="demo", host="localhost", port="5432")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from ID"
    cursor.execute(postgreSQL_select_Query)
    oldID = cursor.fetchall()
    print("                  This Monitor Security             ")
    print("----------------------------------------------------")
    ID = input("Please input RIFID : ")
    for row in oldID:
        if(ID != row[0]):
            print("ID not Enabled")
        else:
            print("ID RIF : ",row[0])
            print("Time in : ",row[2])
            print("Time Out : ", row[3])
            print("Money Pay : ", row[4])
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
        print("Your choice: ", end = "")
        choice = input()
        if choice == '1':
            check = monitoring()
        elif choice == '2':
            check = informations()
        elif choice == '3':
            check = security()
        os.system("clear")

def main():
    menu()

if __name__ == '__main__':
    main()
