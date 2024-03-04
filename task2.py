from collections import UserDict

class Field:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)    


class Name(Field):
     def __init__(self,value):
         self.value = value


class Phone(Field):
    
    def __init__(self,value):
            self.value = value

    def validate_phone(self):
        if len(self.value) == 10:
            return self.value
        else:
            raise ValueError("Phone number must be exactly 10 digits")            

class Record:
    def __init__(self,name):
        self.name = Name(name)
        self.phones = []   

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        phone_obj.validate_phone()
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
         for p in self.phones:
            if p.value == phone:
               self.phones.remove(p)
               break

    def edit_phone(self, old_phone, new_phone):
      for p in self.phones:
          if p.value == old_phone:
              p.value = new_phone
              break
    
    def find_phone(self, phone):      
         for p in self.phones:
             if p.value == phone:
                 return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" 
    

class AdressBook(UserDict):

     def add_record(self, record):
        self.data[record.name.value] = record

     def find(self, name):
         return self.data[name]
     
     def delete(self, name):
         del self.data[name]
            

book = AdressBook()

john_record = Record("John")
john_record.add_phone("0674567456")
john_record.add_phone("0985678453")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("0998978678")

book.add_record(jane_record)

for name, record in book.data.items():
        print(record)

john = book.find("John")
john.edit_phone("0674567456", "0671111111")

print(john)

found_phone = john.find_phone("0671111111")
print(f"{john.name}: {found_phone}") 

book.delete("Jane")
