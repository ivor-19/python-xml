def info_student(name, age, email):
    print('Name: ', name)
    print('Age: ', age)
    print('Email: ', email)


class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2

class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.__weight = weight

    def get_weight(self):
        return self.__weight

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float):
        self._account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f'Your new balance: {self._balance}')
        else:
            print('Insufficient Funds.')

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f'Your new balance: {self._balance}')
            else:
                print('Insufficient Funds. Make sure you put a validsasd')
        else:
            print('Insufficient Funds.')

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance




def num_sample(num):
    print(f'Num is: {num}')


if __name__ == '__main__':
    print('I was run directly')

