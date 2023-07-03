#Тестирование UI Prestashop.
##Требования:
- docker
- docker compose

##Порядок выполнения:
1. Скачай необходимые образы браузеров выполнив скрипт `pull_browsers.sh` из директории `/utils/scrips/`
2. Измени название файла `.env-selenoid` на `.env`
3. Запуск docker-compose `docker-compose up -d`
4. Запуск allure репорта
   1. Дожидаемся результатов тестов в папку `tests/allure_server/allure_results`. (Время выполнения тестов 3-5 мин) 
   2. Запускаем скрипт отправки результатов на контейнер с allure 
      1. Если установлен python >= 3.9 + poetry poe локально: `poetry poe allure_results`
      2. Через докер: `docker run --rm python-kotik poetry poe allure_results`
   3. По успешному окончанию скрипта получаем ссылку в консоле `ALLURE REPORT URL`
5. Готово

##Примечание
Проэкт частично покрыт тестами.
Основная задача была сделать работоспособный фреймворк с использованием Page Factory + Page Objects.

##Project Status:
- Work in Progress