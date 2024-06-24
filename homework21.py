# class car:
#     def __init__(self,arg)->None:
#         self.model=arg[0]
#         self.year=arg[1]
#         self.pro=arg[2]
#         self.obm=arg[3]
#         self.color=arg[4]
#         self.sel=arg[5]
# car1=car(input("Все характеристики через пробел: \n"
#                "1.Модель,\n"
#                "2.год выпуска,\n"
#                "3.производитель,\n"
#                "4.объем,\n"
#                "5.цвет,\n"
#                "6.цена:\n>>>>").split())
# print(f"Модель {car1.model} год выпуска{car1.year} производитель{car1.pro} объем{car1.obm} цвет{car1.color} цена{car1.sel}")

class book:
    def __init__(self,arg)->None:
        self.name=arg[0]
        self.year=arg[1]
        self.pro=arg[2]
        self.janr=arg[3]
        self.avtor=arg[4]
        self.sel=arg[5]
book1=book(input("Все о книге через пробел: \n"
               "1.Название книги,\n"
               "2.год выпуска,\n"
               "3.издатель,\n"
               "4.жанр,\n"
               "5.автор,\n"
               "6.цена:\n>>>>").split())
print(f"Название: {book1.name} \nгод выпуска: :{book1.year} \nиздатель: {book1.pro} \nжанр: {book1.janr} \nавтор: {book1.avtor} \nцена: {book1.sel}")


class stadion:
    name="stadion"
    date="xx.xx.xxxx"
    country="USA"
    gor="detroit"
    vms=100000
    
book1=stadion()
print(f"Название стадиона: {stadion.name} \nгод открытия: :{stadion.date} \nстрана: {stadion.country} \nгород: {stadion.gor} \nвместимость: {stadion.vms}")