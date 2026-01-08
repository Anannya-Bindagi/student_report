from student import get_student_result
# -------- Grade S (90–100) --------
def test_S_start():
    result = get_student_result("anannya", "bca", "3", 90, 90, 90)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 90.00, Grade: S"
    assert result == expected
def test_S_middle():
    result = get_student_result("anannya", "bca", "3", 90, 95, 100)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 95.00, Grade: S"
    assert result == expected
def test_S_end():
    result = get_student_result("anannya", "bca", "3", 100, 100, 100)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 100.00, Grade: S"
    assert result == expected
# -------- Grade A (80–89) --------
def test_A_start():
    result = get_student_result("anannya", "bca", "3", 80, 80, 80)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 80.00, Grade: A"
    assert result == expected
def test_A_middle():
    result = get_student_result("anannya", "bca", "3", 80, 85, 90)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 85.00, Grade: A"
    assert result == expected
def test_A_end():
    result = get_student_result("anannya", "bca", "3", 89, 89, 89)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 89.00, Grade: A"
    assert result == expected
# -------- Grade B (65–79) --------
def test_B_start():
    result = get_student_result("anannya", "bca", "3", 65, 65, 65)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 65.00, Grade: B"
    assert result == expected
def test_B_middle():
    result = get_student_result("anannya", "bca", "3", 65, 72, 79)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 72.00, Grade: B"
    assert result == expected
def test_B_end():
    result = get_student_result("anannya", "bca", "3", 79, 79, 79)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 79.00, Grade: B"
    assert result == expected
# -------- Grade C (50–64) --------
def test_C_start():
    result = get_student_result("anannya", "bca", "3", 50, 50, 50)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 50.00, Grade: C"
    assert result == expected
def test_C_middle():
    result = get_student_result("anannya", "bca", "3", 50, 57, 64)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 57.00, Grade: C"
    assert result == expected
def test_C_end():
    result = get_student_result("anannya", "bca", "3", 64, 64, 64)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 64.00, Grade: C"
    assert result == expected
# -------- Grade D (40–49) --------
def test_D_start():
    result = get_student_result("anannya", "bca", "3", 40, 40, 40)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 40.00, Grade: D"
    assert result == expected
def test_D_middle():
    result = get_student_result("anannya", "bca", "3", 40, 45, 49)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 44.67, Grade: D"
    assert result == expected
def test_D_end():
    result = get_student_result("anannya", "bca", "3", 49, 49, 49)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 49.00, Grade: D"
    assert result == expected
# -------- Grade F (Below 40 → only one case) --------
def test_F_fail():
    result = get_student_result("anannya", "bca", "3", 30, 35, 38)
    expected = "Name: anannya, Department: bca, Semester: 3, Average: 34.33, Grade: F"
    assert result == expected
