print("Хотите собрать самый вкусный в мире бургер?")
flag = True
while (flag):
    choice = int(input('Выберите вариант ответа\n1 - Да\n2 - Нет\n'))
    if choice == 1:
        print('Ты выбрал правильное решение!!!\n'
              + 'Вперед все в твоих руках!!!')
        break
    elif choice == 2:
        print('Вы ввели не корректный вариант ответа')
    else:
        flag = False
        print('Ну и ладно тогда останешься без бургера, если не можешь правильно нажать!!Шутка!!!!')
print("Собери самый вкусный в мире бургер!!!\n")
print("Какую булочку Вы желаете?")
print("1-Ржаную\n2-Пшеничную\n3-Тостовый хлеб")
h = int(input("Выберите желаемый вариант:"))
# while h = str(h)
# h = str(input("Вы ввели неверное значение, попробуйте еще раз:"))
while h >= 4:
    h = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
if h == 1:
    print("Хороший выбор\n\n --Ржаная булочка--\n\nПРОДОЛЖАЙ\n")
    print("Какую котлету Вы желаете?")
    print("1-Свинную\n2-Куриную\n3-Говяжью")
    kotl = int(input("Выберите желаемый вариант:"))
    while kotl >= 4:
        kotl = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
    if kotl == 1:
        print("Хороший выбор\n\n --Свинная котлета--\n\nПРОДОЛЖАЙ\n")
    if kotl == 2:
        print("Хороший выбор\n\n --Куриная котлета--\n\nПРОДОЛЖАЙ\n")
    if kotl == 3:
        print("Хороший выбор\n\n --Говяжья котлета--\n\nПРОДОЛЖАЙ\n")
    print("Укажите количество сочных котлет, которое Вы желаете?")
    print("1\n2\n3")
    kol = int(input("Выберите желаемый вариант:"))
    while kol >= 4:
        kol = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
    if kol == 1:
        print("Хороший выбор\n\n --Одна котлета--\n\nПРОДОЛЖАЙ\n")
    if kol == 2:
        print("Хороший выбор\n\n --Две котлеты--\n\nПРОДОЛЖАЙ\n")
    if kol == 3:
        print("Хороший выбор\n\n --Три котлеты--\n\nПРОДОЛЖАЙ\n")
if h == 2:
    print("Хороший выбор\n\n --Пшеничная булочка--\n\nПРОДОЛЖАЙ\n")
    print("Какую котлету Вы желаете?")
    print("1-Свинную\n2-Куриную\n3-Говяжью")
    kotl = int(input("Выберите желаемый вариант:"))
    while kotl >= 4:
        kotl = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
    if kotl == 1:
        print("Хороший выбор\n\n --Свинная котлета--\n\nПРОДОЛЖАЙ\n")
    if kotl == 2:
        print("Хороший выбор\n\n --Куриная котлета--\n\nПРОДОЛЖАЙ\n")
    if kotl == 3:
        print("Хороший выбор\n\n --Говяжья котлета--\n\nПРОДОЛЖАЙ\n")
    print("Укажите количество сочных котлет, которое Вы желаете?")
    print("1\n2\n3")
    kol = int(input("Выберите желаемый вариант:"))
    while kol >= 4:
        kol = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
    if kol == 1:
        print("Хороший выбор\n\n --Одна котлета--\n\nПРОДОЛЖАЙ\n")
    if kol == 2:
        print("Хороший выбор\n\n --Две котлеты--\n\nПРОДОЛЖАЙ\n")
    if kol == 3:
        print("Хороший выбор\n\n --Три котлеты--\n\nПРОДОЛЖАЙ\n")
if h == 3:
    print("Хороший выбор\n\n --Тостовый хлеб--\n\nПРОДОЛЖАЙ\n")
print("Давай выберем самые свежие овощи!!!")
print("1-Салатик\n2-Помидорчик\n3-Огурчик\n4-Выбрать всё сразу")
ov = int(input("Выберите желаемый вариант:"))
while ov >= 5:
    ov = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
if ov == 1:
    print("Хороший выбор\n\n --Салатик--\n\nПРОДОЛЖАЙ\n")
if ov == 2:
    print("Хороший выбор\n\n --Помидорчик--\n\nПРОДОЛЖАЙ\n")
if ov == 3:
    print("Хороший выбор\n\n --Огурчик--\n\nПРОДОЛЖАЙ\n")
if ov == 4:
    print("\n--Замечателльно, ты выбрал все овощи сразу и получаешь скидку - 5%--\n\nПРОДОЛЖАЙ\n")
print("Выберете самый вкусный соус!!!")
print("1-Сырный\n2-Барбекю\n3-Терияки\n4-Горчичный")
so = int(input("Выберите желаемый вариант:"))
while so >= 5:
    so = int(input("Вы выбрали неверный вариант, попробуйте еще раз:"))
if so == 1:
    print("Хороший выбор\n\n --Сырный--\n\n\nЗамечательно, Ты собрал самый вкусный в мире бургер!!!\n")
if so == 2:
    print("Хороший выбор\n\n --Барбекю--\n\n\nЗамечательно, Ты собрал самый вкусный в мире бургер!!!\n")
if so == 3:
    print("Хороший выбор\n\n --Терияки--\n\n\nЗамечательно, Ты собрал самый вкусный в мире бургер!!!\n")
if so == 4:
    print("Хороший выбор\n\n --Горчичный--\n\n\nЗамечательно, Ты собрал самый вкусный в мире бургер!!!\n")
print("Вот что у Тебя получилось!!!\n")
if h == 1:
    print("--Ржаная булочка--")
    if kotl == 1:
        print("--Свиная котлета--")
    if kotl == 2:
        print("--Куриная котлета--")
    if kotl == 3:
        print("--Говяжья котлета--")
    if kol == 1:
        print("  1 штука ")
    if kol == 2:
        print("  2 штуки ")
    if kol == 3:
        print("  3 штуки ")
if h == 2:
    print("--Пшеничная булочка--")
    if kotl == 1:
        print("--Свиная котлета--")
    if kotl == 2:
        print("--Куриная котлета--")
    if kotl == 3:
        print("--Говяжья котлета--")
    if kol == 1:
        print("  1 штука ")
        print("https://kartinkinaden.ru/uploads/posts/2021-03/thumbs/1617150490_1-p-burger-krasivo-1.jpg")
    if kol == 2:
        print("  2 штуки ")
        print("https://pm1.narvii.com/7268/8581f1f554942531488739ad5ead56042b7bb005r1-1800-1350v2_hq.jpg")
    if kol == 3:
        print("  3 штуки ")
        print('https://myuspehlife.ru/wp-content/uploads/2019/02/super.ua-1539794668.jpg')
if h == 3:
    print("--Тостовый хлеб--")
if ov == 1:
    print("--Салатик--")
if ov == 2:
    print("--Помидорчик--")
if ov == 3:
    print("--Огурчик--")
if ov == 4:
    print("--Все овощи сразу и скидка 5%--")
if so == 1:
    print("--Сырный соус--")
if so == 2:
    print("--Соус Барбекю--")
if so == 3:
    print("--Соус Терияки--")
if so == 4:
    print("--Горчичный соус--")
print("Приятного аппетита!!")
