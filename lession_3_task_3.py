from address import Address
from mailing import Mailing

# Создаем экземпляр класса Address для адреса отправителя и получателя
to_address = Mailing.Address("123456", "Город1", "Улица1", "Дом1", "Квартира1")
from_address = Mailing.Address("654321", "Город2", "Улица2", "Дом2", "Квартира2")

# Создаем экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 200, "ABCD123456789")

# Выводим информацию об отправлении
print(f"Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mailing.cost} рублей.")