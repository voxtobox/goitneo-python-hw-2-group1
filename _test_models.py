from models import AddressBook, Record

##### TEST #####

def show_all_records(book):
  print('show all records')
  # Виведення всіх записів у книзі
  for name, record in book.data.items():
    print(record)

# Створення нової адресної книги
print('Add new book')
book = AddressBook()
print('success')

# Створення запису для John
print('Create record John')
john_record = Record("John")
print('success')
print('Add 2 phones')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print('success')

# Додавання запису John до адресної книги
print('Add record John to book')
book.add_record(john_record)
show_all_records(book)

# Створення та додавання нового запису для Jane

print('Create new record Jane')
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
print('success')

show_all_records(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print('success')

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
print('success')

show_all_records(book)