from entities.phone import Phone


class Contact:

    @classmethod
    def create(cls, phone_number: str):
        contact = cls()
        contact.set_phone(phone_number)
        return contact

    def __init__(self):
        self.phone: Phone = None

    def set_phone(self, phone_number: str) -> None:
        self.phone = Phone(phone_number)

    def get_phone_number(self) -> str:
        return self.phone.number