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
    checkAdm = 1
    while (checkAdm):
        print("Information Screen")
        print("1. Memmber")
        print("2. Seach Memmber")
        print("3. Add Memmber")
        print("4. Delete Memmber")
        print("Your choice: ", end = "")
        choiceAdm = input()
        if choiceAdm == '1':
            checkAdm = adminMemmber()
        elif choiceAdm == '2':
            idInput = input("Please Input RFID : ")
            checkAdm = admin(idInput)
        elif choiceAdm == '3':
            checkAdm = addMemmber()
        elif choiceAdm == '4':
            checkAdm = deleteMemmber()
        os.system("clear")

    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0

def securityScreen():
    # Input: postgre or excel
    # Output: Informations
    os.system("clear")
    checksecu = 1
    while (checksecu):
        print("Security Screen")
        print("1. Memmber INPUT")
        print("2. Memmber OUTPUT")
        print("Your choice: ", end = "")
        choicesecu = input()
        if choicesecu == '1':
            idInput = input("Please Input RFID : ")
            checksecu = inputMemmber(idInput)
        elif choicesecu == '2':
            idOutput = input("Please Input RFID : ")
            checksecu = outputMember(idOutput)
        os.system("clear")

    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def addMemmber():
    try:
        conn = psycopg2.connect(user="postgres",
                                password="1",
                                host="localhost",
                                port="5432",
                                database="postgres")
        cursor = conn.cursor()
        listMember = []
        print("Input Car_id : ")
        car_id = input()
        listMember.append(car_id)
        print("Input Memmber_id : ")
        memmber_id = input()
        listMember.append(memmber_id)
        print("Input Full Name : ")
        full_name = input()
        listMember.append(full_name)
        print(listMember)

        postgres_insert_query = """ INSERT INTO admin (car_id, member_id, full_name) VALUES (%s,%s,%s)"""
        cursor.execute(postgres_insert_query, listMember)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into admin table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into admin table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    
def deleteMemmber():
    try:
        conn = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")

        cursor = conn.cursor()
        idDelete = input("Please input ID want to delete : ")
        # Update single record now
        sql_delete_query = """Delete from admin where car_id = %s"""
        cursor.execute(sql_delete_query, (idDelete,))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
def sale(RFID):
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
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
def adminMemmber():
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from admin"
    cursor.execute(postgreSQL_select_Query)
    admin = cursor.fetchall()
    print("                  This Monitor Admin             ")
    print("----------------------------------------------------")
    for row in admin:
        print("ID RIF : ", row[0])
        print("Member ID : ", row[1])
        print("Full Name : ", row[2])     
    conn.commit()
    conn.close()
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def admin(RFID):
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    print("Successfully connected!")
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from admin where car_id = %s"
    cursor.execute(postgreSQL_select_Query, (RFID,))
    admin = cursor.fetchall()
    if cursor.rowcount > 0:
            print("True")
            print("                  This Monitor Admin             ")
            print("----------------------------------------------------")
            for row in admin:
                print("ID RIF : ", row[0])
                print("Member ID : ", row[1])
                print("Full Name : ", row[2])
    else:
        print("RFID not have")     
    conn.commit()
    conn.close()
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def inputMemmber(RFID):
    try:
        conn = psycopg2.connect(user="postgres",
                                    password="1",
                                    host="localhost",
                                    port="5432",
                                    database="postgres")
        print("Successfully connected!")
        cursor = conn.cursor()
        listMember = []
        print("Input Car_id : ")
        car_id = input()
        listMember.append(car_id)
        print("Input price : ")
        price = input()
        listMember.append(price)
        transaction_id = 'DDMMYYYYHH12MISS'
        listMember.append(transaction_id)
        in_time = 'localtimestamp'
        listMember.append(in_time)
        

        postgres_insert_query = """ INSERT INTO security (car_id, price, transaction_id, in_time) VALUES (%s,%s,%s,%s)"""
        cursor.execute(postgres_insert_query, listMember)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into admin table")

        postgreSQL_select_Query = "select * from security"
        cursor.execute(postgreSQL_select_Query, (RFID,))
        secu = cursor.fetchall()
        if cursor.rowcount > 0:
            print("                This Monitor Member Input           ")
            print("----------------------------------------------------")
            for row in secu:
                    print("ID RIF : ",row[0])
                    print("Transaction id : ", row[2])
                    print("Time in : ",row[3])
        else:
            print("RFID not have")  
    
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into admin table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
            
    print("Do you want to continue[Y/N]? ", end = "")
    ans = input()
    if (ans == 'Y' or ans == 'y'):
        return 1
    elif (ans == 'N' or ans == 'n'):
        return 0
def outputMember(RFID):
    conn = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    print("Successfully connected!")
    cursor = conn.cursor()
    out_time = 'CURRENT_TIMESTAMP'
    # payment = str((out_time - in_time)* price)
    postgreSQL_update_Query = "Update mobile set out_time = %s set payment = %s where id = %s"
    cursor.execute(postgreSQL_update_Query, (out_time,10000,RFID,))
    conn.commit()
    count = cursor.rowcount
    print(count, "Record Updated successfully ")
    postgreSQL_select_Query = "select * from security"
    cursor.execute(postgreSQL_select_Query, (RFID,))
    secu = cursor.fetchall()
    if cursor.rowcount > 0:
        print("                This Monitor Member Output           ")
        print("----------------------------------------------------")
        for row in secu:
                print("ID RIF : ",row[0])
                print("Time in : ",row[3])
                print("Payment : ", row[4])
    else:
        print("RFID not have")  
            
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
        print("Admin Screen")
        print("1. Information Screen")
        print("2. Security Screen")
        print("3. Sale Screen")
        print("Your choice: ", end = "")
        choiceAdm = input()
        if choiceAdm == '1':
            check = monitoring()
        elif choiceAdm == '2':
            # ID = input("Please input RIFID : ")
            check = securityScreen()
        elif choiceAdm == '3':
            check = sale()
        os.system("clear")

def main():
    menu()

if __name__ == '__main__':
    main()
