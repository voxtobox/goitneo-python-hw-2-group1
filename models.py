from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
      
    def __eq__(self, other):
        return self.value == other

class Name(Field):
    def __hash__(self):
        return hash(self.value)


class Phone(Field):
    def __init__(self, phone):
        if phone.isdigit() and len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        newPhone = Phone(phone)
        self.phones.append(newPhone)

    def delete_phone(self, phone):
      self.phones = list(filter(lambda p: p != phone, self.phones))
      
    def edit_phone(self, oldPhone, newPhone):
      phoneIndex = self.phones.index(oldPhone)
      if (phoneIndex != -1):
        self.phones[phoneIndex] = newPhone
        
    def find_phone(self, phone):
        if phone in self.phones:
            return phone

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join([str(p) for p in self.phones])}"
    
    def __hash__(self):
        return hash(self.name)

class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name] = contact
        
    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        del self.data[name]