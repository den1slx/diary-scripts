from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from random import choice


PRAISE = [
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
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    kid_warnings = Chastisement.objects.filter(schoolkid=schoolkid)
    kid_warnings.delete()


def create_commendation(schoolkid, title):
    lessons = Lesson.objects.all()
    kid_lessons = lessons.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=title
    )
    if not kid_lessons:
        raise Exception(f'title {title} not found. Please check title correct.')
    lesson = kid_lessons.last()
    commendation = Commendation.objects.filter(schoolkid=schoolkid, created=lesson.date, subject__title=title)
    if not commendation:
        Commendation.objects.create(
            text=choice(PRAISE),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
        )


def get_schoolkid(name):
    kid = Schoolkid.objects.filter(full_name__contains=name).get()
    return kid
