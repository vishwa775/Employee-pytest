from emp import emp_details

def test_emp():
    expected_op = (
        "Employee name: Vishwa\n"
        "Employee id: 146\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert emp_details("Vishwa", 146, "MCA", 200000) == expected_op