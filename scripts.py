import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

from datacenter.models import *


def main():
    pass


def verification_schoolkid(schoolkid_full_name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_full_name).get()
    except ObjectDoesNotExist:
        print('Такой ученик не найден')
    except MultipleObjectsReturned:
        print(f'По запросу найдено несколько учеников: {schoolkid_full_name}\n Уточните ФИО ученика')
    else:
        return schoolkid


def verification_subject(schoolkid_year_of_study, subject_title):
    try:
        subject = Subject.objects.filter(title=subject_title, year_of_study=schoolkid_year_of_study).get()
    except ObjectDoesNotExist:
        print(f'Предмета {subject_title} в расписании нет\n Уточните название предмета')
    else:
        return subject


def create_commendation(schoolkid_full_name, subject_title):
    commendation = [
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
    schoolkid = verification_schoolkid(schoolkid_full_name)
    if schoolkid:
        subject = verification_subject(schoolkid.year_of_study, subject_title)
        if subject:
            lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                           subject=subject).order_by('date').last()
            Commendation.objects.create(text=random.choice(commendation), created=lesson.date, schoolkid=schoolkid,
                                        subject=lesson.subject, teacher=lesson.teacher)


def create_chastisement(schoolkid_full_name, subject_title):
    chastisement = [
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
    schoolkid = verification_schoolkid(schoolkid_full_name)
    if schoolkid:
        subject = verification_subject(schoolkid.year_of_study, subject_title)
        if subject:
            lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                           subject=subject).order_by('date').last()
            Chastisement.objects.create(text=random.choice(chastisement), created=lesson.date, schoolkid=schoolkid,
                                        subject=lesson.subject, teacher=lesson.teacher)


def fix_marks(schoolkid_full_name, subject_title):
    schoolkid = verification_schoolkid(schoolkid_full_name)
    if schoolkid:
        subject = verification_subject(schoolkid.year_of_study, subject_title)
        if subject:
            Mark.objects.filter(schoolkid=schoolkid, subject=subject, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid_full_name, subject_title):
    schoolkid = verification_schoolkid(schoolkid_full_name)
    if schoolkid:
        subject = verification_subject(schoolkid.year_of_study, subject_title)
        if subject:
            Chastisement.objects.filter(schoolkid=schoolkid, subject=subject).delete()


def remove_commendation(schoolkid_full_name, subject_title):
    schoolkid = verification_schoolkid(schoolkid_full_name)
    if schoolkid:
        subject = verification_subject(schoolkid.year_of_study, subject_title)
        if subject:
            Commendation.objects.filter(schoolkid=schoolkid, subject=subject).delete()


if __name__ == '__main__':
    main()
