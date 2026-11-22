from prog_6 import employee

def test_employee():
    result = employee("Megha", 101, "IT", 50000)

    expected = "Name: Megha, ID: 101, Department: IT, Salary: 50000"

    assert result == expected