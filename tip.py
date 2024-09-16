def tip_calc():
    bill = float(input('What is the bill? '))
    tip_pct = float(input('What is the tip percentage? '))
    tip_amt = tip_pct/100 * bill
    bill_amt = tip_amt + bill
    
    print(f'The tip is ${tip_amt:.2f}')
    print(f'The total is ${bill_amt:.2f}')

tip_calc()