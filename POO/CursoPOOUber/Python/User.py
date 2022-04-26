from account import Account


class User(Account):
    year = int
    sex = str

    def __init__(self, name, document, year, sex):
        super().__init__(name, document)
        self.year = year
        self.sex = sex

        
