 Проект "Ростелеком".
 
 Данный проект является Финальным заданием для курса школы Skillfactory - тестировщик-автоматизатор на Python.
 
 Оъект тестирования: Стартовая страница - Личный кабинет компании "Ростелеком".
 
 Для реализация проекта были разработаны UI-тесты с помощью Selenium по принципу Page Object. Во всех тестах применена параметрезация с помощью библиотеки Pytest. Для параметризации были применены различные техники тест-дизайна: классы эквивалентности, техника граничных значений, причино-следственный анализ, попарное тестирование(в данных тестах не использовался pairwise так, как даже с его использованием для полного покрытия получалось очень большое колличество тестов, поэтому в данном проекте были применены наиболее часто встречаемые ошибки).
 
 Файлы:
- pages: base_page, base_elements, page_site.
- test
- conftest
- settings

Все валидные и некоторые невалидные переменные реализваны с помощью файла .env, который является скрытым и позволяет настраивать отдельные переменные вашей среды. Описание переменных гаходится в файле setting.
  
Необходимые библиотеки для запуска тестов:
- pytest
- selenium
- termcolor
- load_dotenv

Для запуска тестов:
- установите необходимые библиотеки;
- создайте и заполните файл .env.
- запустите теcты через терминал с помощью команды: python3 -m pytest -v --driver Chrome --driver-path *tests или через 'run' в файле test в PyCharm.
