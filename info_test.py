from info import Calculator, num_sample, BMI, BankAccount
import xml.etree.ElementTree as ET

tree = ET.parse('bank_account.xml')
root = tree.getroot()

# info_student('Deniel Ivor', '21', 'ivorcruz19@gmail.com')

# calc = Calculator()
#
# print('Add total: ', calc.add(2,5))
# print('Subtraction total: ', calc.sub(8,5))

# bmi = BMI('34cm', '355cm')
#
# print(bmi.height) # this will show
# print(bmi.get_weight()) # this will not show

# Create a new BankAccount object

while True:
    account_num_input = input('Enter your account number: ')
    get_account_num = root.find(f'./account[@id="{account_num_input}"]')

    if get_account_num is not None:
        account_balance = get_account_num.find(f'balance')
        account_name = get_account_num.find(f'name')

        print(f'Welcome! {account_name.text}\nYour Balance: {account_balance.text}')

        bank = BankAccount(account_num_input, int(account_balance.text))
        while True:
            choice = input('\nWhat would you like to do? \n[1] - Deposit \t[2] - Withdraw: ')
            if choice == '1':
                print('--Deposit--')

                deposit = int(input('Enter the amount you want to deposit: '))
                bank.deposit(deposit)

                account_balance.text = str(bank.get_balance())

                break
            elif choice == '2':
                print('--Withdraw--')

                withdraw = int(input('Enter the amount you want to withdraw: '))
                bank.withdraw(withdraw)

                account_balance.text = str(bank.get_balance())
                break
            else:
                print('Invalid Input: Try again.')
        break

    else:
        print(f'Invalid Input: Account Number "{account_num_input}" is not found. Try again.\n')


tree.write('bank_account.xml')