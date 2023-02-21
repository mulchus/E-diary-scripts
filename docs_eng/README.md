In english | [По-русски](../README.md)

# Scripts for changes to the school electronic diary
Designed to correct bad grades and delete teacher comments in an electronic diary

### How to use?
Python3 should already be installed.

If the website of the electronic diary with the database has not yet been launched, you need to download the code of the electronic diary
[by link](https://github.com/devmanorg/e-diary/tree/master ).
In the above repository in the file `README.md ` it is written how to install and launch an electronic diary.
You can download the database by following [the link](https://dvmn.org/filer/canonical/1562234129/166/)

Next, you need to download the script code `scripts.py ` [by link](https://github.com/mulchus/E-diary-scripts)


### Scripts for changes to the school electronic diary
To use them, it is necessary:
- file `scripts.py ` upload to the server in the root folder of the electronic diary (where the file ``manage.py`` is located);
- run the command line `Django shell` with the command
```
python manage.py shell
```
and import scripts in it with the command
```
from scripts import *
```

Then the following commands are entered.

Important! The student's full name can be entered partially. The script will work if it finds only one student with the specified data.
```
fix_marks('Student's full name', 'Lesson name')
```
- corrects all grades 2 and 3 by 5 for the specified student in the specified subject.


```
remove_chastisements('Student's full name', 'Lesson name')
```
- removes all the teacher's comments on the specified subject from the specified student.


```
remove_commendation('Student's full name', 'Lesson name')
```
- removes from the specified student all the teacher's praises on the specified subject.


```
create_chastisement('Student's full name', 'Lesson name`)
```
- adds the teacher's remark on the specified subject to the specified student. A comment is selected randomly from the list of comments in the **chastisement variable**


```
create_commendation('Student's full name', 'Lesson name`)
```
- adds the teacher's praise for the specified subject from the specified student. The praise is selected randomly from the list of praises in the **commendation variable**


### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
