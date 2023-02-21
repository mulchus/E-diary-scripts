import random

from datacenter.models import Schoolkid, Subject, Lesson, Mark, Chastisement, Commendation


COMMENDATION = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
]

CHASTISEMENT = [
    'Болтал!',
    'Вел себя плохо!',
    'Играл в карты!',
    'Списывал!',
    'Отвлекал других!',
    'Ругался матом!',
    'Опоздал!',
    'Прогулял!',
    'Вышел и не вернулся!',
    'Пользовался шпалгалками!',
]


def checking_schoolkids_full_name(schoolkid_full_name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_full_name).get()
    except Schoolkid.DoesNotExist:
        print('Такой ученик не найден')
    except Schoolkid.MultipleObjectsReturned:
        print(f'По запросу найдено несколько учеников: {schoolkid_full_name}\n Уточните ФИО ученика')
    else:
        return schoolkid


def checking_subject_title(schoolkid_year_of_study, subject_title):
    try:
        subject = Subject.objects.filter(title=subject_title, year_of_study=schoolkid_year_of_study).get()
    except Subject.DoesNotExist:
        print(f'Предмета {subject_title} в расписании нет\n Уточните название предмета')
    else:
        return subject


def create_commendation(schoolkid_full_name, subject_title):
    schoolkid = checking_schoolkids_full_name(schoolkid_full_name)
    if not schoolkid:
        return
    subject = checking_subject_title(schoolkid.year_of_study, subject_title)
    if not subject:
        return
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                   subject=subject).order_by('date').last()
    Commendation.objects.create(text=random.choice(COMMENDATION), created=lesson.date, schoolkid=schoolkid,
                                subject=lesson.subject, teacher=lesson.teacher)


def create_chastisement(schoolkid_full_name, subject_title):
    schoolkid = checking_schoolkids_full_name(schoolkid_full_name)
    if not schoolkid:
        return
    subject = checking_subject_title(schoolkid.year_of_study, subject_title)
    if not subject:
        return
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                   subject=subject).order_by('date').last()
    Chastisement.objects.create(text=random.choice(CHASTISEMENT), created=lesson.date, schoolkid=schoolkid,
                                subject=lesson.subject, teacher=lesson.teacher)


def fix_marks(schoolkid_full_name, subject_title):
    schoolkid = checking_schoolkids_full_name(schoolkid_full_name)
    if not schoolkid:
        return
    subject = checking_subject_title(schoolkid.year_of_study, subject_title)
    if not subject:
        return
    Mark.objects.filter(schoolkid=schoolkid, subject=subject, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid_full_name, subject_title):
    schoolkid = checking_schoolkids_full_name(schoolkid_full_name)
    if not schoolkid:
        return
    subject = checking_subject_title(schoolkid.year_of_study, subject_title)
    if not subject:
        return
    Chastisement.objects.filter(schoolkid=schoolkid, subject=subject).delete()


def remove_commendation(schoolkid_full_name, subject_title):
    schoolkid = checking_schoolkids_full_name(schoolkid_full_name)
    if not schoolkid:
        return
    subject = checking_subject_title(schoolkid.year_of_study, subject_title)
    if not subject:
        return
    Commendation.objects.filter(schoolkid=schoolkid, subject=subject).delete()
