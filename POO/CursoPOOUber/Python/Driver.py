from account import Account

class Driver(Account):
    yearsDrive = int
    typeLicense = str

    def __init__(self, name, document, yearsDrive, typeLicense):
        super().__init__(name, document)
        self.typeLicense = typeLicense
        self.yearsDrive = yearsDrive