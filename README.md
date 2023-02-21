По-русски | [In english](docs_eng/README.md)
# Скрипты изменений школьного электронного дневника
Предназначены для исправления плохих оценок и удаления замечаний учителей в электронном дневнике

### Как использовать?
Python3 должен быть уже установлен. 
Если сайт электронного дневника с базой данных еще не запущен - необходимо скачать код электронного дневника 
[по ссылке](https://github.com/devmanorg/e-diary/tree/master).
В вышеуказанном репозитории в файле ``README.md`` написано, как осуществить установку и запуск электронного дневника. 
Скачать базу данных можно по ссылке https://dvmn.org/filer/canonical/1562234129/166/
Далее необходимо скачать код скриптов ``scripts.py`` [по ссылке](https://github.com/mulchus/E-diary-scripts/):


### Скрипты изменений школьного электронного дневника
Для их использования необходимо:
- файл ``scripts.py`` залить на сервер в корневую папку электронного дневника (где лежит файл ``manage.py``);
- запустить командную строку ``Django shell`` командой 
```
python manage.py shell
```
и в ней импортировать скрипты командой 
```
from scripts import *
```

Далее вводятся нижеуказанные команды.

Важно! ФИО ученика может быть введено частично. Скрипт сработает, если найдет только одного ученика с указанными данными.
```
fix_marks('ФИО ученика', 'Название урока')
```
- исправляет у указанного ученика все оценки 2 и 3 на 5 по указанному предмету.  
  

```
remove_chastisements('ФИО ученика', 'Название урока')
```
- удаляет у указанного ученика все замечания учителя по указанному предмету.
  

```
remove_commendation('ФИО ученика', 'Название урока')
```
- удаляет у указанного ученика все похвалы учителя по указанному предмету.
  

```
create_chastisement('ФИО ученика', 'Название урока')
```
- добавляет у указанного ученика замечание учителя по указанному предмету. Замечание выбирается случайно из списка замечаний в переменной **chastisement**
  

```
create_commendation('ФИО ученика', 'Название урока')
```
- добавляет у указанного ученика похвалу учителя по указанному предмету. Похвала выбирается случайно из списка похвал в переменной **commendation**
  


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
