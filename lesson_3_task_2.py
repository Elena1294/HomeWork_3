from smartphone import Smartphone

# Создаем экземпляры класса Smartphone
phone1 = Smartphone("Samsung", "Galaxy S20", "+79123456789")
phone2 = Smartphone("Apple", "iPhone 12", "+79234567890")
phone3 = Smartphone("Google", "Pixel 5", "+79345678901")
phone4 = Smartphone("Xiaomi", "Mi 11", "+79456789012")
phone5 = Smartphone("OnePlus", "9 Pro", "+79567890123")

# Создаем список с экземплярами класса Smartphone
catalog = [phone1, phone2, phone3, phone4, phone5]

# Печатаем каталог
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")