class TransferError(Exception):
    def __init__(self, text):
        self.text = text


class Storage:
    def __init__(self):
        self.__storage = []

    def add(self, equipment):
        self.__storage.extend(equipment)
        return print(f'На склад добавлен {equipment[0].eq_type} {equipment[0].model} серийный номер: {equipment[0].serial_number} цена: {equipment[0].price}')

    def __str__(self):
        return f"На складе находится {len(self.__storage)} единиц техники"

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferError(f"Недопустимый тип индекса '{type(idx)}'")

        item: Office_Equipment = self.__storage[idx]
        item.department = department
        return print(f'{self.__storage[idx].eq_type} {self.__storage[idx].model} серийный номер: {self.__storage[idx].serial_number} был передан в отдел {self.__storage[idx].department}')

class Office_Equipment:
    def __init__(self, eq_type: str = None, model: str = "", serial_number: str = "", price: float = 0):
        self.eq_type = eq_type
        self.model = model
        self.serial_number = serial_number
        self.price = price

    def __str__(self):
        return f'{self.eq_type} {self.model} серийный номер: {self.serial_number} цена: {self.price}'

    @classmethod
    def create(cls, **properties):
        return [cls(**properties)]


class Printer(Office_Equipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)

class Scanner(Office_Equipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)

class MFP(Office_Equipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='MFP', **kwargs)


storage = Storage()
storage.add(Printer.create(model='HP LaserJer P1200', serial_number='CNC84237942', price=10500))
storage.add(Printer.create(model='HP LaserJer P1005', serial_number='CVC95345455', price=9600))
storage.add(Scanner.create(model='Epson Perfection V19', serial_number='CHN987654345', price=34500))
storage.add(MFP.create(model='HP LaserJet Pro MFP M426fdn', serial_number='SNM73754358349', price=110000))
print(storage)

storage.transfer(1, 'HR')
#storage.transfer(7.1, 'IT')