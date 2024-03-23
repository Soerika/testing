import pytest
from source.calculate_bill_module import calculate_final_bill

param_list = [
    ('card', 0, True, 'invalid input'),
    ('card', 600, True, 577),
    ('COD', 100, False, 100),
]

@pytest.mark.parametrize('billing_method, total, coupon, expected_output', param_list)
def test_c_2_coverage(billing_method, total, coupon, expected_output):
    assert calculate_final_bill(billing_method, total, coupon) == expected_output