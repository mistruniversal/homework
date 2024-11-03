# # # Абстрактная фабрика
# # class AbstractFactory(object):
# #     def create_drink(self):
# #         raise NotImplementedError()
# #
# #     def create_food(self):
# #         raise NotImplementedError()
# #
# #
# # class Drink(object):
# #     def __init__(self, name):
# #         self._name = name
# #
# #     def __str__(self):
# #         return self._name
# #
# #
# # class Food(object):
# #     def __init__(self, name):
# #         self._name = name
# #
# #     def __str__(self):
# #         return self._name
# #
# #
# # class ConcreteFactory1(AbstractFactory):
# #     def create_drink(self):
# #         return Drink('Coca-cola')
# #
# #     def create_food(self):
# #         return Food('Hamburger')
# #
# #
# # class ConcreteFactory2(AbstractFactory):
# #     def create_drink(self):
# #         return Drink('Pepsi')
# #
# #     def create_food(self):
# #         return Food('Cheeseburger')
# #
# #
# # def get_factory(ident):
# #     if ident == 0:
# #         return ConcreteFactory1()
# #     elif ident == 1:
# #         return ConcreteFactory2()
# #
# # factory = get_factory(1)
# # print (factory.create_drink())  # Pepsi
# # print (factory.create_food())  # Cheeseburger
# #
# #
# # # Строитель
# # class Builder(object):
# #     def build_body(self):
# #         raise NotImplementedError()
# #
# #     def build_lamp(self):
# #         raise NotImplementedError()
# #
# #     def build_battery(self):
# #         raise NotImplementedError()
# #
# #     def create_flashlight(self):
# #         raise NotImplementedError()
# #
# #
# # class Flashlight(object):
# #     """Карманный фонарик"""
# #     def __init__(self, body, lamp, battery):
# #         self._shine = False  # излучать свет
# #         self._body = body
# #         self._lamp = lamp
# #         self._battery = battery
# #
# #     def on(self):
# #         self._shine = True
# #
# #     def off(self):
# #         self._shine = False
# #
# #     def __str__(self):
# #         shine = 'on' if self._shine else 'off'
# #         return 'Flashlight [%s]' % shine
# #
# #
# # class Lamp(object):
# #     """Лампочка"""
# #
# #
# # class Body(object):
# #     """Корпус"""
# #
# #
# # class Battery(object):
# #     """Батарея"""
# #
# #
# # class FlashlightBuilder(Builder):
# #     def build_body(self):
# #         return Body()
# #
# #     def build_battery(self):
# #         return Battery()
# #
# #     def build_lamp(self):
# #         return Lamp()
# #
# #     def create_flashlight(self):
# #         body = self.build_body()
# #         lamp = self.build_lamp()
# #         battery = self.build_battery()
# #         return Flashlight(body, lamp, battery)
# #
# #
# # builder = FlashlightBuilder()
# # flashlight = builder.create_flashlight()
# # flashlight.on()
# # print (flashlight ) # Flashlight [on]
# #
# #
# #
# #
# # # Фабричный метод
# # class Document(object):
# #     def show(self):
# #         raise NotImplementedError()
# #
# #
# # class ODFDocument(Document):
# #     def show(self):
# #         print 'Open document format'
# #
# #
# # class MSOfficeDocument(Document):
# #     def show(self):
# #         print 'MS Office document format'
# #
# #
# # class Application(object):
# #     def create_document(self, type_):
# #         # параметризованный фабричный метод `create_document`
# #         raise NotImplementedError()
# #
# #
# # class MyApplication(Application):
# #     def create_document(self, type_):
# #         if type_ == 'odf':
# #             return ODFDocument()
# #         elif type_ == 'doc':
# #             return MSOfficeDocument()
# #         else:
# #             return Document()
# #
# #
# # app = MyApplication()
# # app.create_document('odf').show()  # Open document format
# # app.create_document('doc').show()  # MS Office document format
# # try:
# #     app.create_document('pdf').show()
# # except:
# #     print("NotImplementedError")
#
#
#
#
# # Прототип
# # import copy
# # class Prototype(object):
# #     def __init__(self):
# #         self._objects = {}
# #
# #     def register(self, name, obj):
# #         self._objects[name] = obj
# #
# #     def unregister(self, name):
# #         del self._objects[name]
# #
# #     def clone(self, name, attrs):
# #         obj = copy.deepcopy(self._objects[name])
# #         obj.__dict__.update(attrs)
# #         return obj
# #
# #
# # class Bird(object):
# #     """Птица"""
# #
# #
# # prototype = Prototype()
# # prototype.register('bird', Bird())
# #
# # owl = prototype.clone('bird', {'name': 'Owl'})
# # print type(owl), owl.name  # <class '__main__.Bird'> Owl
# #
# # duck = prototype.clone('bird', {'name': 'Duck'})
# # print type(duck), duck.name  # <class '__main__.Bird'> Duck
#
# # Одиночка
# # class SingletonMeta(type):
# #     def __init__(cls, *args, **kwargs):
# #         cls._instance = None
# #         # глобальная точка доступа `Singleton.get_instance()`
# #         cls.get_instance = classmethod(lambda c: c._instance)
# #         super(SingletonMeta, cls).__init__(*args, **kwargs)
# #
# #     def __call__(cls, *args, **kwargs):
# #         if not cls._instance:
# #             cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
# #         return cls._instance
# #
# #
# # class Singleton(object):
# #     __metaclass__ = SingletonMeta
# #
# #     def __init__(self, name):
# #         self._name = name
# #
# #     def get_name(self):
# #         return self._name
# #
# #
# # obj1 = Singleton('MyInstance 1')
# # print obj1.get_name()  # MyInstance 1
# #
# # obj2 = Singleton('MyInstance 2')
# # print obj2.get_name()  # MyInstance 1
# #
# # print obj1 is obj2 is Singleton.get_instance()  # True
#
#
#
# # Адаптер
# class Dog(object):
#     def __init__(self, name):
#         self._name = name
#
#     def bark(self):
#         return '%s: гав-гав!' % self._name
#
#
# class Cat(object):
#     def __init__(self, name):
#         self._name = name
#
#     def meow(self):
#         return '%s: мяу-мяу!' % self._name
#
#
# class CatAdapter(Dog):
#     # благодаря адаптеру мы можем использовать
#     # интерфейс класса `Dog`, а реализацию класса `Cat`.
#
#     def __init__(self, name):
#         super(CatAdapter, self).__init__(name=name)
#         self._cat = Cat(name=name)
#
#     def bark(self):
#         # запрос `bark` преобразуется в запрос `meow`
#         return self._cat.meow()
#
#
# dog = Dog('Тузик')
# print dog.bark()  # Тузик: гав-гав!
#
# dog = CatAdapter('Тузик')
# print dog.bark()  # Тузик: мяу-мяу!
#
#
#
#
# Мост
# class TVBase(object):
#     """Абстрактный телевизор"""
#     def tune_channel(self, channel):
#         raise NotImplementedError()
#
#
# class SonyTV(TVBase):
#     """Телевизор Sony"""
#     def tune_channel(self, channel):
#         print('Sony TV: выбран %d канал' % channel)
#
#
# class SharpTV(TVBase):
#     """Телевизор Sharp"""
#     def tune_channel(self, channel):
#         print('Sharp TV: выбран %d канал' % channel)
#
#
# class RemoteControlBase(object):
#     """Абстрактный пульт управления"""
#     def __init__(self):
#         self._tv = self.get_tv()
#
#     def get_tv(self):
#         raise NotImplementedError()
#
#     def tune_channel(self, channel):
#         self._tv.tune_channel(channel)
#
#
# class RemoteControl(RemoteControlBase):
#     """Пульт управления"""
#     def __init__(self):
#         super(RemoteControl, self).__init__()
#         self._channel = 0  # текущий канал
#
#     def get_tv(self):
#         return SharpTV()
#
#     def tune_channel(self, channel):
#         super(RemoteControl, self).tune_channel(channel)
#         self._channel = channel
#
#     def next_channel(self):
#         self._channel += 1
#         self.tune_channel(self._channel)
#
#     def previous_channel(self):
#         self._channel -= 1
#         self.tune_channel(self._channel)
#
#
# remote_control = RemoteControl()
# remote_control.tune_channel(5)  # Sharp TV: выбран 5 канал
# remote_control.next_channel()  # Sharp TV: выбран 6 канал
#
#
#
#
# Компоновщик
# class Graphic(object):
#     def draw(self):
#         raise NotImplementedError()
#
#     def add(self, obj):
#         raise NotImplementedError()
#
#     def remove(self, obj):
#         raise NotImplementedError()
#
#     def get_child(self, index):
#         raise NotImplementedError()
#
#
# class Line(Graphic):
#     def draw(self):
#         print 'Линия'
#
#
# class Rectangle(Graphic):
#     def draw(self):
#         print 'Прямоугольник'
#
#
# class Text(Graphic):
#     def draw(self):
#         print 'Текст'
#
#
# class Picture(Graphic):
#     def __init__(self):
#         self._children = []
#
#     def draw(self):
#         print 'Изображение'
#         # вызываем отрисовку у вложенных объектов
#         for obj in self._children:
#             obj.draw()
#
#     def add(self, obj):
#         if isinstance(obj, Graphic) and not obj in self._children:
#             self._children.append(obj)
#
#     def remove(self, obj):
#         index = self._children.index(obj)
#         del self._children[index]
#
#     def get_child(self, index):
#         return self._children[index]
#
#
# pic = Picture()
# pic.add(Line())
# pic.add(Rectangle())
# pic.add(Text())
# pic.draw()
# # Изображение
# # Линия
# # Прямоугольник
# # Текст
#
# line = pic.get_child(0)
# line.draw()  # Линия
#
#
#
# Декоратор
# class Man(object):
#     """Человек"""
#     def __init__(self, name):
#         self._name = name
#
#     def say(self):
#         print 'Привет! Меня зовут %s!' % self._name
#
#
# class Jetpack(object):
#     """Реактивный ранец"""
#     def __init__(self, man):
#         self._man = man
#
#     def __getattr__(self, item):
#         return getattr(self._man, item)
#
#     def fly(self):
#         # расширяем функциональность объекта добавляя возможность летать
#         print '%s летит на реактивном ранце!' % self._man._name
#
#
# man = Man('Виктор')
#
# man_jetpack = Jetpack(man)
# man_jetpack.say()  # Привет! Меня зовут Виктор!
# man_jetpack.fly()  # Виктор летит на реактивном ранце!
#
#
#
#
# Фасад
# class Paper(object):
#     """Бумага"""
#     def __init__(self, count):
#         self._count = count
#
#     def get_count(self):
#         return self._count
#
#     def draw(self, text):
#         if self._count > 0:
#             self._count -= 1
#             print text
#
#
# class Printer(object):
#     """Принтер"""
#     def error(self, msg):
#         print 'Ошибка: %s' % msg
#
#     def print_(self, paper, text):
#         if paper.get_count() > 0:
#             paper.draw(text)
#         else:
#             self.error('Бумага закончилась')
#
#
# class Facade(object):
#     def __init__(self):
#         self._printer = Printer()
#         self._paper = Paper(1)
#
#     def write(self, text):
#         self._printer.print_(self._paper, text)
#
#
# f = Facade()
# f.write('Hello world!')  # Hello world!
# f.write('Hello world!')  # Ошибка: Бумага закончилась
