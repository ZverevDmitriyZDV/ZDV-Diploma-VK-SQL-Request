# VkBotLikeTinder
```
Файл запуска программы main.py
``` 
Реализация на Python3.8
## Requirements:
    * DateTime==4.3
    * pprintpp==0.4.0
    * SQLAlchemy==1.4.23
    * vk-api==11.9.4

## Description:
```
Программа является ботом для приложения Vk.com. 

Бот подгружается к сообществу, где в случае обращения пользователя к сообществу через личное сообщение, произойдет дальнейшее общение пользователя и бота.

Бот предложит передать пользователю результат клика по автоматически сформированной ссылки, являющейся строкой обращением для получению токена

ТОКЕН ПОЛЬЗОВАТЕЛЯ НЕ СОХРАНЯЕТСЯ В ПРОГРАММЕ, НО МОЖЕТ ОСТАТЬСЯ В ПЕРЕПИСКЕ.

Далее бот предложит несколько ваариантов выполнения скрита: поиск по умолчанию или запрос
    * поиск по умолчанию берет за основу данные пользователя и ищет противоположный пол со схожими данными
    * поиск по запросу должен быть заполнен в строгом порядке пол/возраст/статус соответсвующий vk/город
    
Следующим шагом бот начнет либо поиск уже сформированных записей в БД либо начнет создавать запросы через API Vk, результаты запросов будут внесены в БД

Пользователю будут предложены 3 персоны, удовлетворяющие требованиям запроса. Результат запроса будет содержать 3 лучших фотографии, ссылку на акаунт, ФИО персоны.
в дополнении к запросу учитвается наличие фото,закрытость аккаунта и проверятся дополнительно город нахождения персоны.
Персоны уже предложенные не попадут в повторный запрос, так как в БД создастся отношение между клиентом и персоной

Для получению следуюущих 3-х записей пользователь должен ввести "Далее" либо "Выход для прекращения получения запросов"
Далее может повторятся до бесонечности, в случае превышения записей в БД, будет сформирован новый запрос через API vk

В случае возобновления работы бота, необходимо повторить все описанные шаги повторно
```
## Запуск:
    * Пройти все пункты в графе "Перед запуском необходимо"
    * Запустить файл main.py
    * На главной странице группы, которую вы создали выбираем пункт "Написать сообщение", введите любое слово
    * Следуем указаниям бота
    * Завершаем программу, вручную прерывая процесс    


## Перед запуском необходимо:

    * Создать БД
        * Для работы с БД установить приложения  БД (Любую. В проекте используется PostgreSQL).
        * Создать БД в приложении
        * Создать пользователя с правами записи в эту БД.
        * Передать данные ключа и пароля использования БД в файл settings.py в значение sql_name. Подробнее смотри ниже
        * В соответствии с кодом из файла: sql_database_template.sql создать таблицы и взаимосвязи. Подробнее смотри ниже
    * В приложении Vk.com получить токен для бота:
        * рекомендуется создать новую vk группу для пробного теста
        * в Настройках сообщества выбрать пункт Работа с API, далее в закладке Ключи доступа, необходимо нажать Создать ключ
        * после указания определенных галочек доступа приложения, необходимо скопировать 85 значный код, 
          для этого необходимо нажать на кнопку Показать
        * полученный код скопировать в файл settings.py в значение sql_name.
        * настройку дополнительных параметров смотри по ссылке: https://github.com/netology-code/py-advanced-diplom/blob/new_diplom/group_settings.md
    * В приложении Vk.com передать Id приложения для автоматического создания ссылки на получение токена пользователя
        * на главной странице своего аккаунка слева найти закладку "Управление"
        * во вкладке "Мои приложения" нажимаем "создать приложение"
        * выбираем "Standalone-приложение" и нажимаем кнопку "Подключить приложение"
        * следующим шагом выбираем сообщество к которому привяжем приложение
        * после сохранения необходимо выцепить id приложения в адрессной строке и передать это значение в settings.py в значение bot_id
        * возможно зайти в настройки приложения и скопировать id Из соответствующей ячейки
```shell
sql_name = 'postgresql://{user}:{user_password}@localhost:5432/{data_base_name}'

{user} - имя созданного пользователя с правом доступа
{user_password} - пароль созданного пользователя с правом доступа
{data_base_name} - название БД,к которой у пользователя есть право доступа
```
#### Пример передачи id приложения:
```shell
https://vk.com/editapp?id=0000000&section=info

передаем 0000000

```
#### Структура взаимосвязей таблиц:

![схема БД](https://github.com/ZverevDmitriyZDV/DIPLOME-2/blob/main/%D0%91%D0%94%20%D1%81%D1%85%D0%B5%D0%BC%D0%B0.PNG)


#### Код необходимый для создания соответсвующей структуры БД
```shell
CREATE TABLE IF NOT EXISTS Client(
	Id INTEGER NOT NULL UNIQUE,
	LastName VARCHAR(60) NOT NULL,
	FirstName VARCHAR(60) NOT NULL,
	PersonUrl VARCHAR(60) NOT NULL,
	Age INTEGER NOT NULL,
	Sex INTEGER NOT NULL,
	City VARCHAR(60) NOT NULL,
	Relation INTEGER NOT NULL,
	PhotosUrl TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Person(
	Id INTEGER NOT NULL UNIQUE,
	LastName VARCHAR(60) NOT NULL,
	FirstName VARCHAR(60) NOT NULL,
	PersonUrl VARCHAR(60) NOT NULL,
	Age INTEGER NOT NULL,
	Sex INTEGER NOT NULL,
	City VARCHAR(60) NOT NULL,
	Relation INTEGER NOT NULL,
	PhotosUrl TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS UsersConnect(
	ClientId INTEGER REFERENCES Client(Id) NOT NULL,
	PersonId INTEGER REFERENCES Person(Id) NOT NULL
);	
```



