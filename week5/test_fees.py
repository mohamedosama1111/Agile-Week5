import pytest
from fees import calculate_fee


def test_fee_without_discount():
    assert calculate_fee(1000, 0) == 1000


def test_fee_with_discount():
    assert calculate_fee(1000, 10) == 900


def test_fee_with_50_percent_discount():
    assert calculate_fee(1000, 50) == 500


def test_fee_with_full_discount():
    assert calculate_fee(1000, 100) == 0


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_fee(-100, 10)


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_fee(1000, 110)