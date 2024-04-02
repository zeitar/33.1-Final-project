# 33.1-Final-project
Final project 20 autotests
В связи с тем что не все требования в документации осуществимы на сегодняшний день, ввиду отсутствия прописанных элементов в действительности, тесты подобраны такие, чтобы максимально покрыть поставленные требования.
Инструменты: pyTest; Selenium
PyTest использовался для упрощения запуска и настройки тестов на стенде. Selenium использовался как знакомый в процессе обучения инструмент для манипулирования драйвером веб-браузера в автоматическом режиме. В нем также активно использовалась методика явных ожиданий.

Для запуска всех тестов используется команда: python -m pytest -v --driver Chrome --driver-path chromedriver-win64/chromedriver.exe

Для запуска тестов отдельных модулей сайта РосТелеком используются следующие команды:

-Модуль Ростелеком КЛЮЧ
python -m pytest -v --driver Chrome --driver-path chromedriver-win64/chromedriver.exe -k test_keyrt

-Модуль Регистрация:
python -m pytest -v --driver Chrome --driver-path chromedriver-win64/chromedriver.exe -k test_reg_page

-Модуль авторизации УМНЫЙ ДОМ
python -m pytest -v --driver Chrome --driver-path chromedriver-win64/chromedriver.exe -k test_code_page 

-Ростелеком Авторизация по коду:
python -m pytest -v --driver Chrome --driver-path chromedriver-win64/chromedriver.exe -k test_code_page

Тест кейсы приложены отдельной таблицей
