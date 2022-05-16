# 

## Установка
```
pip install - r requirements.txt
```
## Подключение к БД Oracle (в тестовой версии оставлен sqllite)
```
1. Поменять настройки в файле settings.py в разделе DATABASE
2. В файле models.py поменять  в классе Meta у модели Employee название таблицы
```
## Запуск
```
python manage.py runserver

```
## Особенности тестового приложения
```
В настоящее время доступен только 1 работающий человек под именем Иванов Иван Иванович
являющийся тестовым персонажеv. Поэтому поиск необходимо делать по нему, все данные фейковые
Реализован как доступ через формы, напрямую по адресу http://127.0.0.1:8000/ так и сериализация данных
по адрему http://127.0.0.1:8000/api для будущей интеграции с остальными сервисами
Таким образом достигнута возможная масштабируемость проекта в будущем и уже реализована
возможность работать аналитикам в ежедневном режиме
Docker образ проекта находится в скрытом разделе на докерхабе
```
## TODO
* Добавить requirements.txt (Done)
* Написать FAQ для поключения к Oracle (Done)
* Добавить пагинацию(Done)
* Мелкие фиксы по итогам рабочей встречи 15.02.2022 (Done)
* Добавить описание настроек приложения
* Обдумать возможность добавления cors django rest framework(позволит добавлять к ответам заголовки Cross-Origin Resource Sharing (CORS). Это позволяет запросы в браузере к вашему приложению Django из других источников)