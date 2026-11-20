import pytest
from week5.grades import get_grade


def test_grade_a():
    assert get_grade(95) == "A"


def test_grade_b():
    assert get_grade(85) == "B"


def test_grade_c():
    assert get_grade(75) == "C"


def test_grade_d():
    assert get_grade(65) == "D"


def test_grade_f():
    assert get_grade(50) == "F"


def test_grade_zero():
    assert get_grade(0) == "F"


def test_invalid_grade():
    with pytest.raises(ValueError):
        get_grade(110)


def test_negative_grade():
    with pytest.raises(ValueError):
        get_grade(-5)



def test_grade_boundary_90():
    assert get_grade(90) == "A"

def test_grade_boundary_80():
    assert get_grade(80) == "B"

def test_grade_boundary_70():
    assert get_grade(70) == "C"

def test_grade_boundary_60():
    assert get_grade(60) == "D"

def test_grade_boundary_100():
    assert get_grade(100) == "A"

def test_grade_above_100():
    with pytest.raises(ValueError):
        get_grade(101)    

def test_grade_boundary_70():
    assert get_grade(70) == "C"


def test_grade_boundary_60():
    assert get_grade(60) == "D"


def test_grade_boundary_100():
    assert get_grade(100) == "A"


def test_grade_above_100():
    with pytest.raises(ValueError):
        get_grade(101)        