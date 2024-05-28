Горчаков Роман Владимирович. Вариант 4
# Лабораторная работа 2.19. Работа с файловой системой в Python3 с использованием модуля pathlib.

Работа с файлами и взаимодействие с файловой системой важны по многим различным причинам. Простейшие случаи могут включать только чтение или запись файлов, но иногда возникают более сложные задачи. Традиционно Python представлял пути к файлам, используя обычные текстовые строки. При поддержке стандартной библиотеки os.path это было достаточно, хотя и немного громоздко (как второй пример во введении шоу). Однако, поскольку paths не являются строками, важные функции распространяются по всей стандартной библиотеке, включая такие библиотеки, как os, glob и shutil .До Python 3.4 работа с путями файловой системы осуществлялась либо с помощью методов строк (path.rsplit('\\', maxsplit=1)), либо с помощью модуля os.path (os.path.isfile(os.path.join(os.path.expanduser('~'), 'realpython.txt'))).

Модуль pathlib был введен в Python 3.4 (PEP 428) для решения этих проблем. Он объединяет необходимые функции в одном месте и делает его доступным через методы и свойства простого в использовании объекта Path. Всё, что действительно нужно знать, это класс pathlib.Path. Есть несколько разных способов создания пути. Прежде всего, существуют classmethods наподобие .cwd() (текущий рабочий каталог) и .home() (домашний каталог вашего пользователя). Путь также может быть явно создан из его строкового представления:  pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt'). Третий способ построения пути - это соединение частей пути с помощью специального оператора / . Оператор прямой косой черты используется независимо от фактического разделителя пути на платформе: pathlib.Path.home()/'python'/'scripts'/'test.py'.

Традиционно для чтения или записи файла в Python использовалась встроенная функция open(). Это все еще верно, поскольку функция open() может напрямую использовать объекты Path. Эквивалентной альтернативой является вызов .open() для объекта Path: with path.open(mode='r') as fid. Для простого чтения и записи файлов в библиотеке pathlib есть несколько удобных методов:
* .read_text(): открыть путь в текстовом режиме и вернуть содержимое в виде строки;
* .read_bytes(): открыть путь в двоичном/байтовом режиме и вернуть содержимое в виде строки байтов;
* .write_text(): открыть путь и записать в него строковые данные;
* .write_bytes(): открыть путь в двоичном/байтовом режиме и записать в него данные.

Пути также могут быть указаны как простые имена файлов, и в этом случае они интерпретируются относительно текущего рабочего каталога. Метод .resolve () найдет полный путь. Различные части пути удобно доступны как свойства. Основные примеры включают в себя:
* .name: имя файла без какого-либо каталога;
* .parent: каталог, содержащий файл, или родительский каталог, если путь является каталогом;
* .stem: имя файла без суффикса;
* .suffix: расширение файла;
* .anchor: часть пути перед каталогами.

Чтобы переместить файл, используйте .replace() . Обратите внимание, что если место назначения уже существует, .replace() перезапишет его. К сожалению, pathlib явно не поддерживает безопасное перемещение файлов. Чтобы избежать возможной перезаписи пути назначения, проще всего проверить, существует ли место назначения перед заменой. Каталоги и файлы могут быть удалены с помощью .rmdir() и .unlink() соответственно.

Есть несколько разных способов перечислить много файлов. Самым простым является метод .iterdir(), который перебирает все файлы в данном каталоге: collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()). Более гибкие списки файлов могут быть созданы с помощью методов .glob() и .rglob() (рекурсивный глоб). Например, pathlib.Path.cwd().glob('*.txt') возвращает все файлы с суффиксом .txt в текущем каталоге.

Функция tree() будет печатать визуальное дерево, представляющее иерархию файлов, с корнем в данном каталоге. Методы .iterdir(), .glob() и .rglob() ) отлично подходят для выражений генератора и понимания списка. Чтобы найти файл в каталоге, который был последний раз изменен, вы можете использовать метод .stat() для получения информации о базовых файлах.

Для создания уникального нумерованного имени файла на основе шаблона сначала укажите шаблон для имени файла с местом для счетчика. Затем проверьте существование пути к файлу, созданного путем соединения каталога и имени файла (со значением счетчика). Если он уже существует, увеличьте счетчик и попробуйте снова.