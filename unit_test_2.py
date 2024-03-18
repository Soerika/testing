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

