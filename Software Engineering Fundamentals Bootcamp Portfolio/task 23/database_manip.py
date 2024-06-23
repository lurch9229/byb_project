import sqlite3
# .connect used to connect to the database
python_programming_db = sqlite3.connect('python_programming.db')

# Cursor object used to execute sql statements
cursor = python_programming_db.cursor()
cursor.execute('''
    CREATE TABLE python_programming_db(ID INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
    ''')

# Insert into a db the following student data

stu_id1 = 55
stu_name1 = 'Carl Davis'
stu_grade1 = 61

stu_id2 = 66
stu_name2 = 'Dennis Fredrickson'
stu_grade2 = 88

stu_id3 = 77
stu_name3 = 'Jane Richards'
stu_grade3 = 78

stu_id4 = 12
stu_name4 = 'Peyton Sawyer'
stu_grade4 = 45

stu_id5 = 2
stu_name5 = 'Lucas Brooke'
stu_grade5 = 99


# Function to add and display the first student
def show_student1():
    cursor.execute('''
        INSERT INTO python_programming_db(ID, name, grade)
        VALUES (?,?,?)''', (stu_id1, stu_name1, stu_grade1))
    id = 55
    cursor.execute('''
        SELECT ID, name, grade FROM python_programming_db
        WHERE id = ?''', (id,))
    student = cursor.fetchone()
    print(f"First student added\n{student}")


show_student1()


# Function to display the table and all data within
def display_table():
    cursor.execute('''
        SELECT ID, name, grade FROM python_programming_db''')
    print('Full Table')
    for row in cursor:
        # row[0] returns the first column in the query (ID),
        # row[1] returns the second column in the query (name)
        # row[2] returns the third column in the query (grade)
        print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))
    print("\n")


python_programming_db.commit()

# Create a list of students to add to db
student_founders = [(stu_id2, stu_name2, stu_grade2),
                    (stu_id3, stu_name3, stu_grade3),
                    (stu_id4, stu_name4, stu_grade4),
                    (stu_id5, stu_name5, stu_grade5)]

# Insert students to db
cursor.executemany('''
    INSERT INTO python_programming_db(ID, name, grade)
    VALUES (?,?,?)''', student_founders)

python_programming_db.commit()
display_table()


# SELECT all records with a grade 60-80
def grade_range():
    cursor.execute('''SELECT * FROM python_programming_db
        WHERE grade BETWEEN 60 and 80''')
    print_update = cursor.fetchall()
    print('Students with a grade between 60 and 80')
    for row in print_update:
        print(row)
    print("\n")


grade_range()
python_programming_db.commit()


# UPDATE Carl Davis's grade to 65
def update_carl(id):
    grade = 100
    cursor.execute('''
        UPDATE python_programming_db SET grade = ?
        WHERE ID = ?''', (grade, id))


update_carl(55)
print("Carl Davis Updated Grade")
display_table()

python_programming_db.commit()


# DELETE Dennis Fredrickson row
def delete_user(id):
    cursor.execute('''DELETE FROM python_programming_db
        WHERE id = ?''', (id,))


delete_user(66)
python_programming_db.commit()

print("Dennis Fredrickson Removed")
display_table()


# UPDATE grade of all students with an id > 55 to a grade of 80
def update_group_grade():
    cursor.execute('''
    UPDATE python_programming_db
    SET grade = 80
    WHERE id > 55''')


update_group_grade()
python_programming_db.commit()

print('Students with ID > 55 have grade updated')
display_table()
python_programming_db.close()
