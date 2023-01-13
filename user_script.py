"""
Complete the script.

"""


### (1) Receiving user input for three employee PTO balances

print("Enter three employee's PTO balances in hours and I will tell you a PTO summary.")
print()

balance1 = float(input("Enter first employee's PTO balance: "))
balance2 = float(input("Enter second employee's PTO balance: "))
balance3 = float(input("Enter third employee's PTO Balance: "))
print()

# Needed variables pre analysis of employee PTO balances

balance_list = [balance1, balance2, balance3]
num_entrys = len(balance_list)

# Desired analysis of employee PTO balances

total_pto = round(sum(balance_list), 2)
avg_pto = round((total_pto / num_entrys), 2)
prod_pto = round((balance1 * balance2 * balance3), 2)
min_pto = round(min(balance_list), 2)
max_pto = round(max(balance_list), 2)


### (2) Printed calculations of final analysis of employee PTO balances

print('Employee PTO Summary:')
print()
print('Total of all employee PTO balances:', total_pto)
print('Average employee PTO balance:', avg_pto)
print('Product of all employee PTO balances:', prod_pto)
print('Smallest employee PTO balance:', min_pto)
print('Largest employee PTO balance:', max_pto)
print('Range of employee PTO balances:', min_pto, '-', max_pto)
print()


### (3) Decision-making based off employee PTO balance analysis results

print('Employee PTO Evaluation:')
print()

# Employee 1 PTO balance evauation

if balance1 < avg_pto:
    print('Employee 1 has a lower than average PTO balance!')
elif balance1 == avg_pto:
    print('Employee 1 has an average PTO balance.')
elif balance1 > avg_pto:
    print('Employee 1 has a higher than average PTO balance.')

# Employee 2 PTO balance evauation

if balance2 < avg_pto:
    print('Employee 2 has a lower than average PTO balance!')
elif balance2 == avg_pto:
    print('Employee 2 has an average PTO balance.')
elif balance2 > avg_pto:
    print('Employee 2 has a higher than average PTO balance.')

# Employee 3 PTO balance evauation

if balance3 < avg_pto:
    print('Employee 3 has a lower than average PTO balance!')
elif balance3 == avg_pto:
    print('Employee 3 has an average PTO balance.')
elif balance3 > avg_pto:
    print('Employee 3 has a higher than average PTO balance.')