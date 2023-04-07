## Вносим правки в дневник


### Установка

1. Клонируем репозиторий
2. Помещаем scripts.py рядом с вашим manage.py

### Использование

1. Переходим в папку где находится ваш manage.py
2.
    ```commandline
    python manage.py shell
    ```
3. Импортируем scripts:
    ```shell
    from scripts import get_schoolkid, get_schoolkid_lite, create_commendation, remove_chastisements, fix_marks
    ```
4.
    ```shell
    name = 'Ваше ФИО'
    title = 'Урок'
    ```
   Для копирования:
    ```shell
    schoolkid = get_schoolkid(name)
    create_commendation(schoolkid, title)
    remove_chastisements(schoolkid)
    fix_marks(schoolkid)  
    ```
   * **Пояснение**
      * `title = 'Урок'` - Название урока для которого требуется похвала. Не забываем про заглавные буквы
      * `name = 'ФИО ученика'` Фамилия Имя Отчество(Порядок важен!). Не забываем про заглавные буквы.
      * `schoolkid = get_schoolkid(name)`  Получаем карточку ученика
      * `schoolkid = get_schoolkid_lite(name)`  Если не получилось получить карточку и непонятно в чем дело(использовать вместо `get_schoolkid`)
      * `create_commendation(schoolkid, title)`  Создаем похвалу для последнего урока.  
Если похвала для этого урока уже есть ничего не произойдет.
      * `remove_chastisements(schoolkid)`  Удаляем все замечания
      * `fix_marks(schoolkid)`  Заменяем все оценки меньше 4 на пятерки


* **Notes:**
    * Надо заранее развернуть у себя сайт
    * Если у вас уже есть файл с таким названием вы можете переименовать `scripts.py` в `ДругоеНазвание.py`.
Это название также следует использовать в пункте 3 вместо `scripts`.
    * Репозиторий электронного дневника [здесь](https://github.com/devmanorg/e-diary/tree/master)


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
