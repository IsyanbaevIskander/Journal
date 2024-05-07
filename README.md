# Курс Backend Django
В данном репозитории находятся домашние задания и проект


# Список запросов и QuerySetов

## 1
In [3]: models.Student.objects.all()
Out[3]: <QuerySet [<Student: Иванесса Иванова>, <Student: Тимур Кунакбаев>, <Student: Ан
тип Антипин>, <Student: Амир Тимерханов>, <Student: Тимур Русланов>, <Student: Мия Мирон
ова>, <Student: Рамиль Кунакбаев>, <Student: Понтий Пилат>, <Student: Родион Равиоллев>,
 <Student: Тор Одинсон>, <Student: Локи Одинсон>, <Student: Владимир Путин>]>


## 2
In [4]: models.Teacher.objects.all()
Out[4]: <QuerySet [<Teacher: Голованов Артём Дмитриевич>, <Teacher: Пономарёв Илья Ильич>,
<Teacher: Крузо Робинзон Пятницович>, <Teacher: Фаттахов Арсен Мирославович>, <Teache
r: Химикова Химичка Химиковна>, <Teacher: Преподов Препод Преподович>, <Teacher: Воллейб
олов Физрук Мячикович>, <Teacher: Тансыккужина Миляуша Артуровна>]>


## 3
In [6]: models.Parent.objects.all()
Out[6]: <QuerySet [<Parent: Иванов Иван Сергеевич>, <Parent: Иванова Мария Владимировна>
, <Parent: Кунакбаев Вилюр Фаритович>, <Parent: Кунакбаева Гульчатай Амировна>, <Parent:
 Антипин Виталий Родионович>, <Parent: Тимерханова Мария Сергеевна>, <Parent: Русланов И
скандер Айнурович>, <Parent: Миронова Анна Алексеевна>, <Parent: Булгаков Мастер Маргари
тович>, <Parent: Равиоллева Алия Саитовна>, <Parent: Одинсон Один Ктотович>, <Parent: Пу
тин Владимир Юрьевич>]>

## 4
In [7]: models.Subject.objects.all()
Out[7]: <QuerySet [<Subject: Математика>, <Subject: Русский язык>, <Subject: Окружающий 
мир>, <Subject: Физическая культура>, <Subject: Литература>, <Subject: Английский язык>,
 <Subject: Немецкий язык>, <Subject: Физика>, <Subject: Химия>, <Subject: ОБЖ>, <Subject
: Алгебра>, <Subject: Геометрия>, <Subject: История>, <Subject: Обществознание>, <Subjec
t: Информатика>, <Subject: География>]>

## 5
In [8]: models.Group.objects.all()
Out[8]: <QuerySet [<Group: 3 А класс>, <Group: 9 Б класс>, <Group: 11 А класс>, <Group: 
5 В класс>]>

## 6
In [10]: models.Parent.objects.order_by("surname")
Out[10]: <QuerySet [<Parent: Антипин Виталий Родионович>, <Parent: Булгаков Мастер Марга
ритович>, <Parent: Иванов Иван Сергеевич>, <Parent: Иванова Мария Владимировна>, <Parent
: Кунакбаев Вилюр Фаритович>, <Parent: Кунакбаева Гульчатай Амировна>, <Parent: Миронова
 Анна Алексеевна>, <Parent: Одинсон Один Ктотович>, <Parent: Путин Владимир Юрьевич>, <P
arent: Равиоллева Алия Саитовна>, <Parent: Русланов Искандер Айнурович>, <Parent: Тимерх
анова Мария Сергеевна>]>

## 7
In [11]: models.Group.objects.order_by("number")
Out[11]: <QuerySet [<Group: 3 А класс>, <Group: 5 В класс>, <Group: 9 Б класс>, <Group: 
11 А класс>]>

## 8
In [13]: models.Teacher.objects.order_by("date_of_birth")
Out[13]: <QuerySet [<Teacher: Тансыккужина Миляуша Артуровна>, <Teacher: Фаттахов Арсен 
Мирославович>, <Teacher: Голованов Артём Дмитриевич>, <Teacher: Преподов Препод Преподов
ич>, <Teacher: Крузо Робинзон Пятницович>, <Teacher: Воллейболов Физрук Мячикович>, <Tea
cher: Пономарёв Илья Ильич>, <Teacher: Химикова Химичка Химиковна>]>

## 9
In [14]: models.Student.objects.order_by("-date_of_birth")
Out[14]: <QuerySet [<Student: Понтий Пилат>, <Student: Тимур Кунакбаев>, <Student: Рамил
ь Кунакбаев>, <Student: Иванесса Иванова>, <Student: Родион Равиоллев>, <Student: Мия Ми
ронова>, <Student: Амир Тимерханов>, <Student: Тимур Русланов>, <Student: Антип Антипин>
, <Student: Локи Одинсон>, <Student: Тор Одинсон>, <Student: Владимир Путин>]>

## 10
In [15]: models.Student.objects.filter(sex__contains="Ж")
Out[15]: <QuerySet [<Student: Иванесса Иванова>, <Student: Мия Миронова>]>

## 11
In [16]: models.Student.objects.filter(surname__exact="Кунакбаев")
Out[16]: <QuerySet [<Student: Тимур Кунакбаев>, <Student: Рамиль Кунакбаев>]>

## 12
In [19]: models.Group.objects.filter(number__gte=9)
Out[19]: <QuerySet [<Group: 9 Б класс>, <Group: 11 А класс>]>

## 13
In [20]: models.Group.objects.filter(number__gt=9)
Out[20]: <QuerySet [<Group: 11 А класс>]>

## 14
In [21]: models.Student.objects.dates("date_of_birth", "day")
Out[21]: <QuerySet [datetime.date(1940, 6, 8), datetime.date(1986, 1, 1), datetime.date(
1991, 2, 2), datetime.date(2006, 5, 7), datetime.date(2006, 10, 2), datetime.date(2007, 
4, 8), datetime.date(2007, 11, 23), datetime.date(2011, 2, 23), datetime.date(2014, 5, 7
), datetime.date(2014, 7, 24), datetime.date(2014, 11, 30)]>

## 15
In [22]: models.Teacher.objects.dates("date_of_birth", "day").reverse()
Out[22]: <QuerySet [datetime.date(2020, 1, 1), datetime.date(1999, 5, 7), datetime.date(
1989, 12, 31), datetime.date(1987, 2, 7), datetime.date(1984, 5, 7), datetime.date(1968,
 2, 15), datetime.date(1964, 5, 8), datetime.date(1960, 7, 7)]>

## 16
In [28]: models.Teacher.objects.exclude(surname__contains="а")
Out[28]: <QuerySet [<Teacher: Крузо Робинзон Пятницович>, <Teacher: Преподов Препод Преп
одович>, <Teacher: Воллейболов Физрук Мячикович>]>

## 17
In [2]: models.Teacher.objects.values("name", "sex")
Out[2]: <QuerySet [{'name': 'Артём', 'sex': 'М'}, {'name': 'Илья', 'sex': 'М'}, {'name':
 'Робинзон', 'sex': 'М'}, {'name': 'Арсен', 'sex': 'М'}, {'name': 'Химичка', 'sex': 'Ж'}
, {'name': 'Препод', 'sex': 'М'}, {'name': 'Физрук', 'sex': 'М'}, {'name': 'Миляуша', 's
ex': 'Ж'}]>

## 18
In [3]: models.Teacher.objects.values("name", "sex").exclude(sex__contains="Ж")
Out[3]: <QuerySet [{'name': 'Артём', 'sex': 'М'}, {'name': 'Илья', 'sex': 'М'}, {'name':
 'Робинзон', 'sex': 'М'}, {'name': 'Арсен', 'sex': 'М'}, {'name': 'Препод', 'sex': 'М'},
 {'name': 'Физрук', 'sex': 'М'}]>

## 19
In [9]: models.Student.objects.all().exclude(middlename__exact="Владимирович")
Out[9]: <QuerySet [<Student: Иванесса Иванова>, <Student: Тимур Кунакбаев>, <Student: Ан
тип Антипин>, <Student: Амир Тимерханов>, <Student: Тимур Русланов>, <Student: Мия Мирон
ова>, <Student: Рамиль Кунакбаев>, <Student: Понтий Пилат>, <Student: Родион Равиоллев>,
 <Student: Тор Одинсон>, <Student: Локи Одинсон>]>

## 20
In [11]: models.Group.objects.exclude(number__lt=3)
Out[11]: <QuerySet [<Group: 3 А класс>, <Group: 9 Б класс>, <Group: 11 А класс>, <Group:
 5 В класс>]>

## 21
In [12]: models.Subject.objects.filter(name__contains="я").reverse()
Out[12]: <QuerySet [<Subject: Русский язык>, <Subject: Физическая культура>, <Subject: А
нглийский язык>, <Subject: Немецкий язык>, <Subject: Химия>, <Subject: Геометрия>, <Subj
ect: История>, <Subject: География>]>

## 22
In [13]: models.Subject.objects.exclude(name__contains="я")
Out[13]: <QuerySet [<Subject: Математика>, <Subject: Окружающий мир>, <Subject: Литерату
ра>, <Subject: Физика>, <Subject: ОБЖ>, <Subject: Алгебра>, <Subject: Обществознание>, <
Subject: Информатика>]>

## 23
In [14]: models.Student.objects.order_by("group")
Out[14]: <QuerySet [<Student: Тимур Кунакбаев>, <Student: Рамиль Кунакбаев>, <Student: П
онтий Пилат>, <Student: Тор Одинсон>, <Student: Локи Одинсон>, <Student: Антип Антипин>,
 <Student: Амир Тимерханов>, <Student: Тимур Русланов>, <Student: Мия Миронова>, <Studen
t: Иванесса Иванова>, <Student: Родион Равиоллев>, <Student: Владимир Путин>]>

## 24
In [17]: models.Student.objects.filter(sex__contains="М").order_by("date_of_birth")     
Out[17]: <QuerySet [<Student: Владимир Путин>, <Student: Тор Одинсон>, <Student: Локи Од
инсон>, <Student: Антип Антипин>, <Student: Тимур Русланов>, <Student: Амир Тимерханов>,
 <Student: Родион Равиоллев>, <Student: Тимур Кунакбаев>, <Student: Рамиль Кунакбаев>, <
Student: Понтий Пилат>]>

## 25
In [19]: models.Parent.objects.order_by("surname").filter(surname__contains="Иван")     
Out[19]: <QuerySet [<Parent: Иванов Иван Сергеевич>, <Parent: Иванова Мария Владимировна>]>
