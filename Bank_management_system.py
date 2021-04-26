class Bank:
    """
    Parent Class Bank Account contains basic information of all types of Bank Accounts.
    """

    # Class Variables
    numberOfAccounts = 0
    __accountNumbers = []

    # Default Constructor
    def __init__(self, accNum = None, name=None, balance=0):

        # Updating Instance Variables
        self.__accountNumber = accNum
        self._name = name
        self.__balance = balance
        if ((accNum) & (accNum != -1)):
            self.__accountNumber = accNum
        else:
            if self.__accountNumber in Bank.__accountNumbers:
                self.__accountNumber = Bank.__accountNumbers[-1] + 1
            else:
                self.__accountNumber = Bank.numberOfAccounts + 1

        # Updating Class Variables
        Bank.__accountNumbers.append(self.__accountNumber)
        Bank.numberOfAccounts += 1

    def get_AccNo(self):
        return self.__accountNumber

    def get_Name(self):
        return self._name

    def _get_Balance(self):
        return self.__balance

    def set_account_number(self, value):
        self.__accountNumber = value

    def set_name(self, value):
        self._name = value

    def _set_Balance(self, value):
        self.__balance = value

class SavingAccount(Bank):
    """
    Derived Class to implement Saving Accounts.
    """

    def __init__(self, accountNumber, name, balance, branchName):

        super().__init__(accountNumber, name, balance)

        if branchName == '-1':
            self.branchName = "RKL"
        else:
            self.branchName = branchName
    def withdrawMoney(self, amount):

        bal = super()._get_Balance()
        if bal >= amount:
            bal -= amount
            super()._set_Balance(bal)
            print('Money Withdrawn Successfully!')
        else:
            print('Insufficient Funds to withdraw Money!')

    def checkBalance(self):
        print(f'Your Current Balance is : $ {super()._get_Balance()}')

    def depositMoney(self, amount):

        bal = super()._get_Balance()
        bal += amount
        super()._set_Balance(bal)
        print('Money Successfully Deposited!')


class FixedDeposit(Bank):
    """
    Derived Class to implement Fixed Deposit Accounts.
    """

    def __init__(self, accNumber, name, duration, amount, rate):
        super().__init__(accNumber, name)

        # Updating Instance Variables
        self.__duration = duration
        self.__amount = amount
        self.__rate = rate

    def get_Duration(self):
        return self.__duration

    def get_Amount(self):
        return self.__amount

    def get_Rate_Of_Interest(self):
        return self.__rate

    def set_Duration(self, value):
        self.__duration = value

    def set_Amount(self, value):
        self.__amount = value

    def set_Rate(self, value):
        self.__rate = value

class RecurringDeposit(Bank):
    """
    Derived Class to implement Recurring Deposit Accounts.
    """

    # Default Constructor
    def __init__(self, accNumber, name, duration, monthlyPayement, rate):
        super().__init__(accNumber, name)

        self.__duration = duration
        self.__monthlyPayment = monthlyPayement
        self.rateOfInterest = rate

    def get_Duration(self):
        return self.__duration

    def get_Monthly_Payment(self):
        return self.__monthlyPayment

    def get_Rate_Of_Interest(self):
        return self.rate

    def set_Duration(self, value):
        self.__duration = value

    def set_Monthly_Payment(self, value):
        self.__monthlyPayment = value

    def set_Rate_Of_Interest(self, value):
        self.rate = value

def main():
    while True:

        print()
        print("**** Welcome to XYZ Bank Pvt. Ltd. ****")
        print("1. Create or Manage a Savings Account")
        print("2. Create or Manage a Fixed Deposit Account")
        print("3. Create or Manage a Recurring Deposit Account")
        print("4. Exit")

        choice = int(input("\nEnter your Choice : "))

        if choice == 1:

            print()
            print("**** Welcome to the Savings Section ****")
            n = int(input(
                "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

            if n == 1:
                name = input("Enter your Name : ")
                accNo = int(input("Enter an Account Number of your Choice or Leave it Random [-1] : "))
                balance = int(input("Enter your Opening Balance : "))
                branch = input("Enter a Branch Name of your Choice or Leave it Random [-1] : ")
                savingobj = SavingAccount(accNo, name, balance, branch)
                print(f"\nSaving Account Created Successfully for {name}!\n")

            if n == 2:

                x = int(input(
                    "Select : \n1. Know your Balance \n2. Withdraw Money \n3. Deposit Money\nEnter your Choice : "))

                # Checking Balance
                if x == 1:
                    savingobj.checkBalance()

                elif x == 2:
                    amount = int(input("Enter the Amount you want to Withdraw : "))
                    savingobj.withdrawMoney(amount)

                elif x == 3:
                    amount = int(input("Enter the Amount you want to Deposit : "))
                    savingobj.depositMoney(amount)

                else:
                    print("Illegal Input, Please Try Again")

        elif choice == 2:

            print()
            print("**** Welcome to the Fixed Deposit Section ****")
            n = int(input(
                "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))

            pass

        elif choice == 3:

            print()
            print("**** Welcome to the Recurring Deposit Section ****")
            n = int(input(
                "What do you want to do?\n1. Create a New Account. \n2. Checkout Existing Account.\nEnter your Choice : "))
            pass

        elif choice == 4:
            exit(0)

        else:
            print("Wrong Choice!! Please Try Again!>:")

if __name__ == '__main__':
    main()
