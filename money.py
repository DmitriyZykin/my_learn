'''return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum'''

def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal += (principal * interest) * (1 - tax)
        year += 1
    return year