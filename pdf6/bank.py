import os


class Bank:
    def __init__(self):
        self._bank_users = []
        customers_path = (
            "C:/Users/ezrab/OneDrive/Desktop/New folder/Ezra/pdf6/customers"
        )
        # gets the list of all the files that are in that directory
        filenames = os.listdir(customers_path)
        for file in filenames:
            file_path = os.path.join(customers_path, file)
            print(file_path)
            with open(file_path, "r") as file:
                content = file.read()
                print(content)
                # self._bank_users.append(Customer(content))
        print(self)
