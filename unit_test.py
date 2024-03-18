

def calculate_final_bill(billing_method: str, total: float, coupon: bool):
    if total <= 0 or (coupon and total <= 200):
        return 'invalid input'

    discount = 0
    if billing_method == 'card':
        discount += 1
    if total >= 500:
        discount += 2
    
    total = total - total * discount / 100
    
    if coupon:
        total -= 5
    
    return total


def test_calculate_final_bill_1():
    assert calculate_final_bill('card', -1, True) == 'invalid input'
    assert calculate_final_bill('card', 100, True) == 'invalid input'
    assert calculate_final_bill('card', 300, True) == 292
    assert calculate_final_bill('card', 500, True) == 480
    assert calculate_final_bill('card', -1, False) == 'invalid input'
    assert calculate_final_bill('card', 100, False) == 99
    assert calculate_final_bill('card', 300, False) == 297
    assert calculate_final_bill('card', 500, False) == 485
    assert calculate_final_bill('COD', -1, True) == 'invalid input'
    assert calculate_final_bill('COD', 100, True) == 'invalid input'
    assert calculate_final_bill('COD', 300, True) == 295
    assert calculate_final_bill('COD', 500, True) == 485
    assert calculate_final_bill('COD', -1, False) == 'invalid input'
    assert calculate_final_bill('COD', 100, False) == 100
    assert calculate_final_bill('COD', 300, False) == 300
    assert calculate_final_bill('COD', 500, False) == 490

def test_calculate_final_bill_2():
    assert calculate_final_bill('card', 100, True) == 'invalid input'
    assert calculate_final_bill('card', 100, False) == 99
    assert calculate_final_bill('card', 0, False) == 'invalid input'
    assert calculate_final_bill('card', 0.1, False)  * 1000 == 99
    assert calculate_final_bill('COD', 100, False) == 100

if __name__ == "__main__":
    test_calculate_final_bill_1()
    test_calculate_final_bill_2()
    print("everything passed")