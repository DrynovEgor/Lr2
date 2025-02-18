class user:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def  __str__(self):
        return f"Id клиента: {self.id}, Имя пользователя: {self.name}, Номер телефона: {self.phone}"

class employee:
    def __init__(self, id, name, last_name, post, worksAtTheAddress):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.post = post
        self.worksAtTheAddress = worksAtTheAddress

    def  __str__(self):
        return f"Id сотрудника: {self.id}, Имя сотрудника: {self.name}, Фамилия сотрудника: {self.last_name}, Должность сотрудника: {self.post}, Адресс работы: {self.worksAtTheAddress}"

class restaurant:
    def __init__(self, id, address, phone):
        self.id = id
        self.address = address
        self.phone = phone

    def  __str__(self):
        return f"Id ресторана: {self.id}, Адрес: {self.address}, Номер: {self.phone}"

class dish:
    def __init__(self, id, name, ingredients):
        self.id = id
        self.name = name
        self.ingredients = ingredients

    def  __str__(self):
        return f"Id блюда: {self.id}, Название: {self.name}, Инградиенты: {self.ingredients}"
    
    def GetName(self):
        return self.name 
    
class order:
    def __init__(self, id, idDish, idUser):
        self.id = id
        self.idDish = idDish
        self.idUser = idUser

    def  __str__(self):
        return f"Номер заказа: {self.id}, Id блюда: {self.idDish}, Id клиента: {self.idUser}"

user = user("76356345", "Ринг", "88005553535")
emp = employee("6195316", "Егор", "Дрынов", "Менеджер, Программист, Дизайнер, Аналитик, Маркетолог", "г. Барнаул, ул. пр. Ленина, д. 133")
rest = restaurant("1753", "г. Барнаул, пр. Ленина, д. 133", "3852001753")
dis = dish("18252", "Курица обжаренная в кляре", "курица, кляр")
orde = order("11523562","18252","76356345")

print(f"{user}\n{emp}\n{rest}\n{dis}\n{orde}")