def emp_details(name, emp_id, dept, salary):
    result = (
        f"Employee name: {name}\n"
        f"Employee id: {emp_id}\n"
        f"Department: {dept}\n"
        f"Salary: {salary}"
    )
    return result

if __name__ == "__main__":
    name = "Vishwa"
    emp_id = 146
    dept = "BCA"
    salary = 20000000
    
    print(emp_details(name, emp_id, dept, salary))