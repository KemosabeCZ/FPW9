from cat import Cat
# данные с сайта
cats = [
    {
     'name': 'Baron',
     'gen': 'male',
     'age': 2
    },
    {
     'name': 'Sam',
     'gen': 'male',
     'age': 2
    }
]
for elem in cats:
    #  для каждого объекта словаря возвращаем по три атрибута
    sub = Cat(name=elem.get('name'), gen = elem.get('gen'), age = elem.get('age'))
    print(sub.name)
    print(sub.gen)
    print(sub.age)
