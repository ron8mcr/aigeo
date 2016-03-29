# Тестовое задание от [Айгео](http://aigeo.ru)

### Адресный поиск
C результатом можно ознакомиться на [heroku](https://aigeo.herokuapp.com/)

#### Задание
Разработать обертку адресного поиска с использованием минимум 2 внешних сервисов, один из которых - от Енисей-ГИС, API вложен, вторичный например от Яндекс Карт. Можно добавить еще несколько (гугл, 2гис, ...) - необязательно. Оформить как простейший веб-сервис, написать на python. Логика - на входе строка, ищем сервисом Енисей-ГИС. Если не нашли - вторичными сервисами. Выдаем результат в виде координаты и названия сервиса. Цель - найти 1 точку для адреса.
Клиент - страничка с картой например OSM, на движке leaflet. Вверху - поле для ввода адреса и кнопка Искать. При нажатии - отправляем запрос к своему сервису. Если что-то было найдено - показываем маркером на карте с хинтом в виде названия сервиса, которым нашли.
