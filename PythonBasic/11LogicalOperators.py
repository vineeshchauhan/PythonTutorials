has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_high_income and not has_good_credit:
    print("no loan")

