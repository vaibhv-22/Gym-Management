import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
from datetime import date

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return


def bmi(bm):
    if(bm>25):
        return "Overweight"
    elif(bm<18.5):
        return "Underweight"
    else:
        return "Normal"

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


def ret_trainer():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW DETAIL OF TRAINER BY TRAINER_ID")
            print("2. SHOW ALL TRAINERS WITH EXPERIENCE")
            print("3. SHOW ALL TRAINERS BY BRANCH CODE")
            print("4. SHOW ALL TRAINERS BY AGE_GROUP")
            print("5. RETURN TO PREVIOUS MENU")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                query = "SELECT * FROM TRAINER WHERE TRAINER_ID='%s'" % (input("Enter trainer_id: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==2:
                query = "SELECT * FROM TRAINER WHERE WORK_EXPERIENCE >= '%d'" % (int(input("Enter experience: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==3:
                query = "SELECT * FROM TRAINER WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==4:
                query = "SELECT * FROM TRAINER WHERE Age_group='%s'" % (input("Enter age_group: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==5:
                return
def ret_mem():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW DETAIL OF MEMBER BY MEMBER_ID")
            print("2. SHOW DETAIL OF MEMBER BY EMAIL_ID")
            print("3. SHOW ALL MEMBERS BY BRANCH CODE")
            print("4. SHOW ALL MEMBERS BY CITY_CODE")
            print("5. SHOW ALL MEMBERS BY AGE_GROUP")
            print("6. SHOW ALL MEMBERS BY GENDER")
            print("7. BMI OF All MEMBERS")
            print("8. RETURN TO PREVIOUS MENU")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                query = "SELECT * FROM MEMBER WHERE MEMBER_ID='%s'" % (input("Enter member_id: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==2:
                query = "SELECT * FROM MEMBER WHERE Email='%s'" % (input("Enter email_id: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==3:
                query = "SELECT * FROM MEMBER WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==4:
                query = "SELECT * FROM MEMBER WHERE City_Code='%d'" % (int(input("Enter city_code: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==5:
                query = "SELECT * FROM MEMBER WHERE Age_group='%s'" % (input("Enter age_group: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==6:
                query = "SELECT * FROM MEMBER WHERE Gender='%s'" % (input("Enter Gender(M/F/O): "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==7:
                query = "SELECT MEMBER_ID , WEIGHT*10000/(HEIGHT*HEIGHT) AS BMI FROM MEMBER "  # % (bmi(HEALTH_INDEX))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==8:
                return
def ret_non_trainer():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW DETAIL OF NON_TRAINER BY NON_TRAINER_ID")
            print("2. SHOW DETAIL OF NON_TRAINER BY EMAIL_ID")
            print("3. SHOW ALL NON_TRAINERS BY BRANCH CODE")
            print("4. SHOW ALL NON_TRAINERS BY PROFESSION")
            print("5. SHOW ALL NON_TRAINERS WITH SALARY GREATER THAN")
            print("6. RETURN TO PREVIOUS MENU")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                query = "SELECT * FROM NON_TRAINER_STAFF WHERE NON_TRAINER_STAFF_ID='%d'" % (int(input("Enter non_trainer_id: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==2:
                query = "SELECT * FROM NON_TRAINER_STAFF WHERE Email='%s'" % (input("Enter email_id: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==3:
                query = "SELECT * FROM NON_TRAINER_STAFF WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==4:
                query = "SELECT * FROM NON_TRAINER_STAFF WHERE WORK='%s'" % (input("Enter profession: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==5:
                query = "SELECT * FROM NON_TRAINER_STAFF WHERE SALARY >= '%d'" % (int(input("Enter Amount: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==6:
                return
def ret_equip():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW ALL EQUIPMENTS")
            print("2. SHOW ALL EQUIPMENT BY BRANCH CODE")
            print("3. SHOW DETAIL OF EQUIPMENT BY BODY PART")
            print("4. SHOW DETAIL OF EQUIPMENT BY CONDITION")
            print("5. RETURN TO PREVIOUS MENU")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                query = "SELECT * FROM EQUIPMENTS"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==2:
                query = "SELECT * FROM EQUIPMENTS WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==3:
                query = "SELECT * FROM EQUIPMENTS WHERE Body_part='%s'" % (input("Enter body part: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==4:
                query = "SELECT * FROM EQUIPMENTS WHERE HALAT='%s'" % (input("Enter condition: "))
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==5:
                return           
def ret_branch():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW NUMBER OF MEMBERS BY BRANCH_CODE")
            print("2. SHOW NUMBER OF TRAINERS BY BRANCH_CODE")
            print("3. SHOW NUMBER OF NON-TRAINER-STAFF BY BRANCH_CODE")
            print("4. SHOW NUMBER OF EQUIPMENTS BY BRANCH_CODE")
            print("5. TOTAL EXPENDITURE ON NON-TRAINER-STAFF BY BRANCH_CODE")
            print("6. RETURN TO PREVIOUS MENU")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                query = "SELECT COUNT(*) FROM MEMBER WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                # query = "SELECT Branch_Code, COUNT(*) FROM MEMBER GROUP BY Branch_Code"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==2:
                query = "SELECT COUNT(*) FROM TRAINER WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                # query = "SELECT Branch_Code, COUNT(*) FROM TRAINER GROUP BY Branch_Code"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==3:
                query = "SELECT COUNT(*) FROM NON_TRAINER_STAFF WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                # query = "SELECT Branch_Code, COUNT(*) FROM NON_TRAINER GROUP BY Branch_Code"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==4:
                query = "SELECT COUNT(*) FROM EQUIPMENTS WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                # query = "SELECT Branch_Code, COUNT(*) FROM EQUIPMENTS GROUP BY Branch_Code"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==5:
                query = "SELECT SUM(SALARY) FROM NON_TRAINER_STAFF WHERE Branch_Code='%d'" % (int(input("Enter branch_code: ")))
                # query = "SELECT Branch_Code, SUM(Salary) FROM NON_TRAINER GROUP BY Branch_Code"
                cur.execute(query)
                viewTable(cur.fetchall())
                input("Enter any key to CONTINUE> ")
            elif ch==6:
                return          
def retrieve():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear',shell=True)
            print("1. SHOW DETAILS OF BRANCH")
            print("2. SHOW DETAILS OF TRAINERS")
            print("3. SHOW DETAILS OF MEMBERS")
            print("4. SHOW DETAILS OF NON_TRAINER_STAFF")
            print("5. SHOW DETAILS OF EQUIPMENT")
            print("6. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp=sp.call('clear',shell=True)
            if ch==1:
                ret_branch()
                return
            elif ch==2:
                ret_trainer()
                return
            elif ch==3:
                ret_mem()
                return
            elif ch==4:
                ret_non_trainer()
                return
            elif ch==5:
                ret_equip()
                return
            elif ch==6:
                return


def update_equip():
    while(1):
        try:
            row={}
            print("Update Equipment details: ")
            row["Equipment_model"] = (input("Equipment Model: "))
            row["Branch_Code"] = int(input("Branch Code: "))
            row["Tag_id"] = int(input("Tag ID: "))
            row["Condition"] = input("Condition(New/Good/Average/Poor): ")
            row["Number_of_parts"] = int(input("Number of parts: "))
            row["Body_part"] = input("Body part(Chest/Back/Legs/Arms/Shoulders/Abs/Biceps/Triceps): ")
            query = "UPDATE EQUIPMENTS SET Model='%s', Branch_Code='%d', Tag_id='%d', Halat='%s', Number_of_parts='%d', Body_part='%s' WHERE Tag_id='%d'" % (row["Equipment_model"], row["Branch_Code"], row["Tag_id"], row["Condition"], row["Number_of_parts"], row["Body_part"], row["Tag_id"])
            # print(query)
            cur.execute(query)
            con.commit()

            print("Updated Into Database")
            input("Enter any key to CONTINUE> ")
            return
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return
def update_non_trainer():
    while(1):
        try:
            row={}
            print("Update Non-Trainer Staff details: ")
            row["Staff_id"] = int((input("Staff id: ")))
            name = (input("Name (F_name L_name): ")).split(' ')
            row["F_name"] = name[0]
            row["L_name"] = name[1]
            row["Email"] = input("E-Mail ID: ")
            row["Profession"] = input("Profession: ")
            row["Salary"] = int(input("Salary: "))
            row["Branch_Code"] = int(input("Branch Code: "))
            query = "UPDATE NON_TRAINER_STAFF SET Fname='%s', Lname='%s', Email='%s', Work='%s', Salary='%d', Branch_Code='%d' WHERE NON_TRAINER_STAFF_ID='%d'" % (row["F_name"], row["L_name"], row["Email"], row["Profession"], row["Salary"], row["Branch_Code"], row["Staff_id"])
            # print(query)
            cur.execute(query)
            con.commit()

            print("Updated Into Database")
            input("Enter any key to CONTINUE> ")
            return
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return
def update_mem():
    while(1):
        try:
            row={}
            print("Update Member details: ")
            row["Member_id"] = int((input("Member id: ")))
            name = (input("Name (F_name L_name): ")).split(' ')
            row["F_name"] = name[0]
            row["L_name"] = name[1]
            row["Branch_code"] = int(input("Branch code: "))
            row["City_code"] = int(input("City code: "))
            row["Email_ID"] = input("E-Mail ID: ")
            row["Address"] = input("Address: ")
            row["Gender"] = input("Gender(M/F/O): ")
            row["DOB"] = input("Date of Birth(DD/MM/YYYY): ")
            row["Height"] = int(input("Height(in cm): "))
            row["Weight"] = int(input("Weight(in kg): "))
            # row["Age_group"] = "A"
            p  = int(calculateAge(date(int(row["DOB"][6:]),int(row["DOB"][3:5]),int(row["DOB"][:2]))))
            if p<=18:
                row["Age_group"] = "A"
            elif p>18 and p<=25:
                row["Age_group"] = "B"
            elif p>25 and p<=35:
                row["Age_group"] = "C"
            elif p>35:
                row["Age_group"] = "D"
            query = "UPDATE MEMBER SET FNAME='%s', LNAME='%s', BRANCH_CODE='%d', CITY_CODE='%d', EMAIL='%s', ADDRESS='%s', GENDER= '%s', DOB= '%s', AGE_GROUP= '%s' ,Height='%d',Weight='%d' where Member_id='%d'" % (row["F_name"] , row["L_name"] , row["Branch_code"] , row["City_code"], row["Email_ID"] , row["Address"], row["Gender"] , row["DOB"] , row["Age_group"] , row["Height"] , row["Weight"] , row["Member_id"])
            cur.execute(query)
            con.commit()
            
            print("Updated Database")
            
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return
        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break
def update_trainer():
    while(1):
        try:
            row={}
            print("Update Trainer details: ")
            row["Trainer_id"] = int((input("Trainer id: ")))
            name = (input("Name (F_name L_name): ")).split(' ')
            row["F_name"] = name[0]
            row["L_name"] = name[1]
            # row["Email_ID"] = input("E-Mail ID: ")
            row["Address"] = input("Address: ")
            row["Branch_code"] = int(input("Branch code: "))
            row["Contact_number"] = int(input("Contact number: "))
            row["Age_group"] = input("Age group(A/B/C/D): ")
            row["Work_experience"] = int(input("Work experience: "))
            query = "UPDATE TRAINER SET FNAME='%s', LNAME='%s', ADDRESS='%s', BRANCH_CODE='%d', CONTACT_NUMBER='%d', AGE_GROUP='%s', WORK_EXPERIENCE='%d' WHERE TRAINER_ID='%d'" % (row["F_name"] , row["L_name"] , row["Address"], row["Branch_code"] , row["Contact_number"] , row["Age_group"],  row["Work_experience"] , row["Trainer_id"])
            # print(query)
            cur.execute(query)
            con.commit()

            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return
        ch = input("Enter any key to return to the menu> ")
        tmp=sp.call('clear',shell=True)
        break
def update():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear', shell=True)
            print("1. CHANGE DETAIL OF MEMBER")
            print("2. CHANGE DETAIL OF TRAINER")
            print("3. CHANGE DETAIL OF NON_TRAINER_STAFF")
            print("4. CHANGE CONDITION OF EQUIPEMENT")
            print("5. RETURN BACK TO MAIN MENU")
            ch=int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==1:
                update_mem()
            elif ch==2:
                update_trainer()
            elif ch==3:
                update_non_trainer()
            elif ch==4:
                update_equip()
            elif ch==5:
                return


def add_member():
    try:
        row={}
        print("Enter new Member details: ")
        row["Member_id"] = int((input("Member id: ")))
        # row["Ssn"] = input("SSN: ")
        name = (input("Name (F_name L_name): ")).split(' ')
        row["F_name"] = name[0]
        row["L_name"] = name[1]
        row["Branch_code"] = int(input("Branch code: "))
        row["City_code"] = int(input("City code: "))
        row["Email_ID"] = input("E-Mail ID: ")
        row["Address"] = input("Address: ")
        row["Gender"] = input("Gender(M/F/O): ")
        row["DOB"] = input("Date of Birth(DD/MM/YYYY): ")
        row["Height"] = int(input("Height(in cm): "))
        row["Weight"] = int(input("Weight(in kg): "))
        # row["Age_group"] = "A"
        p  = int(calculateAge(date(int(row["DOB"][6:]),int(row["DOB"][3:5]),int(row["DOB"][:2]))))
        if p<=18:
            row["Age_group"] = "A"
        elif p>18 and p<=25:
            row["Age_group"] = "B"
        elif p>25 and p<=35:
            row["Age_group"] = "C"
        elif p>35:
            row["Age_group"] = "D"

        query = "INSERT INTO MEMBER(MEMBER_ID, FNAME, LNAME, BRANCH_CODE , CITY_CODE , EMAIL,  ADDRESS, GENDER , DOB , AGE_GROUP , HEIGHT , WEIGHT) VALUES('%d', '%s', '%s' , '%d', '%d', '%s', '%s' , '%s' , '%s' , '%s' , '%d' , '%d')" % (row["Member_id"], row["F_name"] , row["L_name"] , row["Branch_code"] , row["City_code"] ,  row["Email_ID"] , row["Address"] , row["Gender"] , row["DOB"] , row["Age_group"] , row["Height"] , row["Weight"] )
        # print(query)
        cur.execute(query)
        con.commit()
        
        print("Inserted Into Database")
        input("Enter any key to CONTINUE> ")
        return
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return
def add_trainer():
    try:
        row={}
        print("Enter new Trainer details: ")
        row["Trainer_id"] = int((input("Trainer id: ")))
        name = (input("Name (F_name L_name): ")).split(' ')
        row["F_name"] = name[0]
        row["L_name"] = name[1]
        row["Address"] = input("Address: ")
        row["Branch_Code"] = input("Branch Code: ")
        row["Contact_number"] = int(input("Contact Number: "))
        row["Age-Group"] = input("Age Group(A/B/C/D): ")
        row["Work_exp"] = int(input("Work Experience(in years): "))
        query = "INSERT INTO TRAINER(TRAINER_ID, FNAME, LNAME, ADDRESS, BRANCH_CODE, CONTACT_NUMBER, AGE_GROUP, WORK_EXPERIENCE) VALUES('%d', '%s', '%s', '%s', '%s', '%d', '%s', '%d')" % (row["Trainer_id"], row["F_name"] , row["L_name"] , row["Address"] , row["Branch_Code"] , row["Contact_number"] , row["Age-Group"] , row["Work_exp"] )
        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
        input("Enter any key to CONTINUE> ")
        return
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return
def add_non_trainer_staff():
    try:
        row={}
        print("Enter new Non-Trainer Staff details: ")
        row["Staff_id"] = (input("Staff id: "))
        name = (input("Name (F_name L_name): ")).split(' ')
        row["F_name"] = name[0]
        row["L_name"] = name[1]
        row["Email"] = input("E-Mail ID: ")
        row["Profession"] = input("Profession: ")
        row["Salary"] = int(input("Salary: "))
        row["Branch_Code"] = int(input("Branch Code: "))
        query = "INSERT INTO NON_TRAINER_STAFF(NON_TRAINER_STAFF_ID, FNAME, LNAME, EMAIL, WORK, SALARY, BRANCH_CODE) VALUES('%s', '%s', '%s', '%s', '%s', '%d', '%d')" % (row["Staff_id"], row["F_name"] , row["L_name"] , row["Email"] , row["Profession"] , row["Salary"] , row["Branch_Code"] )
        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
        input("Enter any key to CONTINUE> ")
        return
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return
def add_equipment():
    try:
        row={}
        print("Enter new Equipment details: ")
        row["Equipment_model"] = (input("Equipment Model: "))
        row["Branch_Code"] = int(input("Branch Code: "))
        row["Tag_id"] = int(input("Tag ID: "))
        row["Condition"] = input("Condition(New/Good/Average/Poor): ")
        row["Number_of_parts"] = int(input("Number of parts: "))
        row["Body_part"] = input("Body part(Chest/Back/Legs/Arms/Shoulders/Abs/Biceps/Triceps): ")
        query = "INSERT INTO EQUIPMENTS(MODEL, BRANCH_CODE, TAG_ID, HALAT, NUMBER_OF_PARTS, BODY_PART) VALUES('%s', '%d', '%d', '%s', '%d', '%s')" % (row["Equipment_model"], row["Branch_Code"], row["Tag_id"], row["Condition"], row["Number_of_parts"], row["Body_part"] )
        # print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
        input("Enter any key to CONTINUE> ")
        return
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print
def insert():
    tmp=input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp=sp.call('clear', shell=True)
            print("1. ADD NEW MEMBER")
            print("2. ADD NEW TRAINER")
            print("3. ADD NEW NON_TRAINER_STAFF")
            print("4. ADD EQUIPMENT")
            print("5. Return to previous menu")
            ch=int(input("Enter choice> "))
            tmp = sp.call('clear',shell=True)
            if ch==1:
                add_member()
            elif ch==2:
                add_trainer()
            elif ch==3:
                add_non_trainer_staff()
            elif ch==4:
                add_equipment()
            elif ch==5:
                return




def delete_mem():
    while(1):
        try:
            row = {}
            print("Member Id to delete: ")
            row["Member_id"] = int(input("Member Id: "))
            query = "DELETE FROM MEMBER where MEMBER_ID='%d'" % (
                row["Member_id"])
            # print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp = sp.call('clear', shell=True)
        break
def delete_trainer():
    while(1):
        try:
            row = {}
            print("Trainer ID to delete: ")
            row["Trainer_id"] = int(input("Trainer id: "))
            query = "DELETE FROM TRAINER where TRAINER_ID='%d'" % (
                row["Trainer_id"])
            # print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp = sp.call('clear', shell=True)
        break
def delete_staff():
    while(1):
        try:
            row = {}
            print("NON-TRAINER-STAFF-ID to delete: ")
            row["STAFF_ID"] = int(input("Non-TRAINER-STAFF-ID: "))
            query = "DELETE FROM NON_TRAINER_STAFF where NON_TRAINER_STAFF_ID='%d'" % (
                row["STAFF_ID"])
            # print(query)
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp = sp.call('clear', shell=True)
        break
def delete_equipment():
    while(1):
        try:
            row = {}
            print("DELETING ALL EQIPUMENTS OF POOR CONDITION")
            query = "DELETE FROM EQUIPMENTS where HALAT='Poor'"
            cur.execute(query)
            con.commit()
            print("Updated Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)
            return

        ch = input("Enter any key to return to the menu> ")
        tmp = sp.call('clear', shell=True)
        break
def delete():
    tmp = input("Enter any key to CONTINUE> ")
    with con.cursor() as cur:
        while(1):
            tmp = sp.call('clear', shell=True)
            print("1. Delete Member")
            print("2. Delete Trainer")
            print("3. Delete Non-Trainer Staff")
            print("4. Delete Equipment")
            print("5. Return to the previous menu")
            ch = int(input("Enter choice> "))
            tmp = sp.call('clear', shell=True)
            if ch == 1:
                delete_mem()
            elif ch == 2:
                delete_trainer()
            elif ch == 3:
                delete_staff()
            elif ch == 4:
                delete_equipment()
            elif ch == 5:
                return



def dispatch(ch):
    if(ch==1):
        insert()
    elif(ch==2):
        update()
    elif(ch==3):
        delete()
    elif(ch==4):
        retrieve()
    else:
        print("Error: Invalid option")


while(1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    tmp = sp.call('clear', shell=True)
    try:
        con = pymysql.connect(host='localhost',user=username,password=password,db='OLYMPIA',cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)
        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE> ")
        with con.cursor() as cur:
            while(1):
                tmp=sp.call('clear',shell=True)
                print("1. Insert data")
                print("2. Update data")
                print("3. Delete data")
                print("4. Retrieve data")
                print("5. Logout")
                print("6. Exit")

                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch==5:
                    break
                if ch==6:
                    exit(0)
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE> ")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE> ")
