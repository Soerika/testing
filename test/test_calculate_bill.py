import pytest
from source.calculate_bill_module import calculate_final_bill


param_list_1 = [
    ('card', -1, True, 'invalid input'),
    ('card', 100, True, 'invalid input'),
    ('card', 300, True, 292),
    ('card', 500, True, 480),
    ('card', -1, False, 'invalid input'),
    ('card', 100, False, 99),
    ('card', 300, False, 297),
    ('card', 500, False, 485),
    ('COD', -1, True, 'invalid input'),
    ('COD', 100, True, 'invalid input'),
    ('COD', 300, True, 295),
    ('COD', 500, True, 485),
    ('COD', -1, False, 'invalid input'),
    ('COD', 100, False, 100),
    ('COD', 300, False, 300),
    ('COD', 500, False, 490),
]

@pytest.mark.parametrize('billing_method, total, coupon, expected_output', param_list_1)
def test_calculate_final_bill_1(billing_method, total, coupon, expected_output):
    assert calculate_final_bill(billing_method, total, coupon) == expected_output

param_list_2 = [
    ('card', 100, True, 'invalid input'),
    ('card', 100, False, 99),
    ('card', 0, False, 'invalid input'),
    ('card', 0.1, False, 0.099),
    ('COD', 100, False, 100),
]

@pytest.mark.parametrize('billing_method, total, coupon, expected_output', param_list_2)
def test_calculate_final_bill_2(billing_method, total, coupon, expected_output):
    assert calculate_final_bill(billing_method, total, coupon) == expected_output