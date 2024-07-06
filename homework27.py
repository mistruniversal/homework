class person():
    pass
id_1=person()
setattr(id_1,"name","Vasya")
print(id_1.name)
setattr(id_1,"name","Masha")
print(id_1.name)

class person():
    setup=['set_name', 'set_age', 'set_work', 'set_study']
id_1=person()
for i in id_1.setup:
    setattr(id_1,i,input(f"Значение для {i}:"))
    print(getattr(id_1,i))


