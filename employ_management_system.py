import sqlite3 as sq
con = sq.connect('employ_management_system.db')
cur = con.cursor()
def add_dep():
    deptno = int(input("Enter a department number: "))
    dname = input("Enter department name: ")
    loc = input("Enter department location: ")
    cur.execute('INSERT INTO DEPT (deptno, dname, loc) VALUES (?, ?, ?)', (deptno, dname, loc))
    print("Department added successfully")
    con.commit()
def search_dep():
    deptno = int(input("Enter Department number: "))
    cur.execute('SELECT * FROM DEPT WHERE DEPTNO = ?', (deptno,))
    row = cur.fetchall()
    print("-" * 60)
    print(f"{'Dep number':<20} {'Dep name':<20} {'Dep Location':<15}")
    print("-" * 60)
    for row in row:
        deptno = row[0] if row[0] is not None else "None"
        dname = row[1] if row[1] is not None else "None"
        loc = row[2] if row[2] is not None else "None"
        print(f"{deptno:<20} {dname:<20} {loc:<10}")
    print("-" * 60)
    con.commit()
def delete_dep():
    deptno = int(input("Enter the department number: "))
    cur.execute('DELETE FROM DEPT WHERE DEPTNO = ?', (deptno,))
    con.commit()
def list_all_dep():
    cur.execute('SELECT * FROM DEPT')
    row = cur.fetchall()
    print("-" * 60)
    print(f"{'Dep number':<20} {'Dep name':<20} {'Dep Location':<15}")
    print("-" * 60)
    for row in row:
        deptno = row[0] if row[0] is not None else "None"
        dname = row[1] if row[1] is not None else "None"
        loc = row[2] if row[2] is not None else "None"
        print(f"{deptno:<20} {dname:<20} {loc:<10}")
    print("-" * 60)
    con.commit()
def edit_dep_by_choice():
    user_input = int(input('''What do you want to edit ?
    1. Department number.
    2. Department name
    3. Department Location
    '''))
    if user_input == 1:
        deptno = int(input("Enter Department number: "))
        dname = input("Enter Department name: ")
        cur.execute('UPDATE DEPT SET DEPTNO = ? WHERE DNAME = ?', (deptno, dname))
    elif user_input == 2:
        deptno = int(input("Enter Department number: "))
        dname = input("Enter Department name: ")
        cur.execute('UPDATE DEPT SET DNAME = ? WHERE DEPTNO = ?', (dname, deptno))
    elif user_input == 3:
        deptno = int(input("Enter Department number: "))
        loc = input("Enter Department location: ")
        cur.execute('UPDATE DEPT SET LOC = ? WHERE DEPTNO = ?', (loc, deptno))
    else:
        print("Invalid Input")
    con.commit()
def add_emp():
    empno = int(input("Enter an Employee number: "))
    ename = input("Enter Employee name: ")
    job = input("Enter Employee JOB: ")
    mgr = input("Enter Employee MGR: ")
    hiredate = input("Enter Date in format dd-mon-y: ")
    sal = int(input("Enter Employee Salary: "))
    comm = int(input("Enter Employee Commission: "))
    deptno = int(input("Enter Employee Department number: "))
    cur.execute('INSERT INTO EMP (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (empno, ename, job, mgr, hiredate, sal, comm, deptno))
    print("Employee added successfully")
    con.commit()
def search_emp():
    empno = int(input("Enter Employee number: "))
    cur.execute('SELECT * FROM EMP WHERE empno = ?', (empno,))
    rows = cur.fetchall()
    print("-" * 120)
    print(f"{'Employee No':<10} {'Employee name':<15} {'Job':<15} {'Manager':<20} {'Hire date':<15} {'Salary':<15} {'Commission':<15} {'Dept no':<20}")
    print("-" * 120)
    for row in rows:
        empno = row[0] if row[0] is not None else "None"
        ename = row[1] if row[1] is not None else "None"
        job = row[2] if row[2] is not None else "None"
        mgr = row[3] if row[3] is not None else "None"
        hiredate = row[4] if row[4] is not None else "None"
        sal = row[5] if row[5] is not None else "None"
        comm = row[6] if row[6] is not None else "None"
        deptno = row[7] if row[7] is not None else "None"
        print(f"{empno:<13} {ename:<15} {job:<15} {mgr:<20} {hiredate:<15} {sal:<15} {comm:<15} {deptno:<10}")
    print("-" * 120)
    con.commit()
def delete_emp():
    empno = int(input("Enter the Employee number: "))
    cur.execute('DELETE FROM EMP WHERE empno = ?', (empno,))
    con.commit()
def list_all_emp():
    cur.execute('SELECT * FROM EMP')
    rows = cur.fetchall()
    print("-" * 120)
    print(f"{'Employee No':<10} {'Employee name':<15} {'Job':<15} {'Manager':<20} {'Hire date':<15} {'Salary':<15} {'Commission':<15} {'Dept no':<20}")
    print("-" * 120)
    for row in rows:
        empno = row[0] if row[0] is not None else "None"
        ename = row[1] if row[1] is not None else "None"
        job = row[2] if row[2] is not None else "None"
        mgr = row[3] if row[3] is not None else "None"
        hiredate = row[4] if row[4] is not None else "None"
        sal = row[5] if row[5] is not None else "None"
        comm = row[6] if row[6] is not None else "None"
        deptno = row[7] if row[7] is not None else "None"
        print(f"{empno:<13} {ename:<15} {job:<15} {mgr:<20} {hiredate:<15} {sal:<15} {comm:<15} {deptno:<10}")
    print("-" * 120)
    con.commit()
def edit_employ():
    empno = int(input("Enter Employee number to edit their record: "))
    ename = input("Enter Employee name: ")
    mgr = input("Enter Employee manager: ")
    job = input("Enter Employee job: ")
    hiredate = input("Enter Date in format dd-mon-y: ")
    sal = int(input("Enter Employee salary: "))
    comm = int(input("Enter Employee commission: "))
    deptno = int(input("Enter Employee department number: "))
    cur.execute('UPDATE EMP SET ename = ?, job = ?, mgr = ?, hiredate = ?, sal = ?, comm = ?, deptno = ? WHERE empno = ?', (ename, job, mgr, hiredate, sal, comm, deptno, empno))
    con.commit()
def edit_emp_mgr():
    mgr = input("Enter Employee manager: ")
    empno = int(input("Enter Employee number: "))
    cur.execute('UPDATE EMP SET mgr = ? WHERE empno = ?', (mgr, empno))
    con.commit()
def edit_emp_no():
    empno = int(input("Enter Employee number: "))
    ename = input("Enter Employee name: ")
    cur.execute('UPDATE EMP SET empno = ? WHERE ename = ?', (empno, ename))
    con.commit()
def edit_emp_name():
    empno = int(input("Enter Employee number: "))
    ename = input("Enter Employee name: ")
    cur.execute('UPDATE EMP SET ename = ? WHERE empno = ?', (ename, empno))
    con.commit()
def edit_emp_job():
    empno = int(input("Enter Employee number: "))
    job = input("Enter Employee job: ")
    cur.execute('UPDATE EMP SET JOB = ? WHERE empno = ?', (job, empno))
    con.commit()
def edit_emp_sale():
    empno = int(input("Enter Employee number: "))
    sal = int(input("Enter Employee salary: "))
    cur.execute('UPDATE EMP SET sal = ? WHERE empno = ?', (sal, empno))
    con.commit()
def order_emp_no():
    cur.execute('SELECT * FROM EMP ORDER BY EMPNO')
    con.commit()
    for row in cur:
        print(row)
def add_salgrade():
    grade = int(input("Enter grade: "))
    losal = float(input("Enter low salary: "))
    highsal = float(input("Enter high salary: "))
    cur.execute('INSERT INTO salgrade (grade, losal, highsal) VALUES (?, ?, ?)', (grade, losal, highsal))
    print("Salgrade added successfully")
    con.commit()
def search_salgrade():
    grade = int(input("Enter grade: "))
    cur.execute('SELECT * FROM salgrade WHERE grade = ?', (grade,))
    row = cur.fetchall()
    print("-" * 60)
    print(f"{'Grade':<20} {'Low salary':<20} {'High Salary':<15}")
    print("-" * 60)
    for row in row:
        grade = row[0] if row[0] is not None else "None"
        losal = row[1] if row[1] is not None else "None"
        highsal = row[2] if row[2] is not None else "None"
        print(f"{grade:<20} {losal:<20} {highsal:<10}")
    print("-" * 60)
    con.commit()
def delete_salgrade():
    grade = int(input("Enter grade to delete: "))
    cur.execute('DELETE FROM salgrade WHERE grade = ?', (grade,))
    con.commit()
def list_all_salgrades():
    cur.execute('SELECT * FROM salgrade')
    row = cur.fetchall()
    print("-" * 60)
    print(f"{'Grade':<20} {'Low salary':<20} {'High Salary':<15}")
    print("-" * 60)
    for row in row:
        grade = row[0] if row[0] is not None else "None"
        losal = row[1] if row[1] is not None else "None"
        highsal = row[2] if row[2] is not None else "None"
        print(f"{grade:<20} {losal:<20} {highsal:<10}")
    print("-" * 60)
    con.commit()
def edit_salgrade():
    grade = int(input("Enter grade to edit: "))
    user_input = int(input('''What do you want to edit?
    1. Grade
    2. Low Salary
    3. High Salary
    '''))
    if user_input == 1:
        new_grade = int(input("Enter new grade: "))
        cur.execute('UPDATE salgrade SET grade = ? WHERE grade = ?', (new_grade, grade))
    elif user_input == 2:
        new_losal = float(input("Enter new low salary: "))
        cur.execute('UPDATE salgrade SET losal = ? WHERE grade = ?', (new_losal, grade))
    elif user_input == 3:
        new_highsal = float(input("Enter new high salary: "))
        cur.execute('UPDATE salgrade SET highsal = ? WHERE grade = ?', (new_highsal, grade))
    else:
        print("Invalid input")
    con.commit()
def main():
    while True:
        print('''\nWellcome to Employee Management System !\n
        Choose from below choice :
        1. Add Department 2. Search Department
        3. Delete Department 4. List all Departments
        5. Edit Department  6. Add Employee
        7. Search Employee 8. Delete Employee
        9. List all Employees 10. Edit Employee
        11. Order Employees 12. Add Salary Grade
        13. Search Salary Grade  14. Delete Salary Grade
        15. List all Salary Grades 16. Edit Salary Grade
        17. Exit
        ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_dep()
        elif choice == 2:
            search_dep()
        elif choice == 3:
            delete_dep()
        elif choice == 4:
            list_all_dep()
        elif choice == 5:
            edit_dep_by_choice()
        elif choice == 6:
            add_emp()
        elif choice == 7:
            search_emp()
        elif choice == 8:
            delete_emp()
        elif choice == 9:
            list_all_emp()
        elif choice == 10:
            edit_employ()
        elif choice == 11:
            order_emp_no()
        elif choice == 12:
            add_salgrade()
        elif choice == 13:
            search_salgrade()
        elif choice == 14:
            delete_salgrade()
        elif choice == 15:
            list_all_salgrades()
        elif choice == 16:
            edit_salgrade()
        elif choice == 17:
            con.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 17.")

if __name__ == "__main__":
    main()
