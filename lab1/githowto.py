# Составлено по GitHowTo (уроки 1–14)
# (каждая команда — строка с комментарием и следующей за ней самой командой)

# Установка Git (Linux)
# yum install git-core
# apt-get install git-core
# zypper in git-core

# Установка Git (Mac)
# brew install git

# Установка Git (Windows)
# (см. Git for Windows: git-for-windows.github.io)

# установка имени пользователя для Git
# git config --global user.name "Your Name"

# установка электронной почты для Git
# git config --global user.email "your_email@whatever.com"

# задать имя ветки по умолчанию (например, main)
# git config --global init.defaultBranch main

# корректная обработка окончаний строк (Unix/Mac)
# git config --global core.autocrlf input
# git config --global core.safecrlf warn

# корректная обработка окончаний строк (Windows)
# git config --global core.autocrlf true
# git config --global core.safecrlf warn

# создание рабочей директории проекта
# mkdir work

# переход в директорию проекта
# cd work

# создание файла (пример)
# touch hello.html

# инициализация Git-репозитория в папке
# git init

# добавление одного файла в индекс (staging area)
# git add hello.html

# добавление всех изменений / всех файлов в индекс
# git add .

# первоначальный коммит с комментарием
# git commit -m "Initial commit"

# коммит (открывает редактор для ввода сообщения, если не указан -m)
# git commit

# проверка состояния репозитория / рабочей директории
# git status

# переименование ветки master в main (если нужно)
# git branch -m master main

# просмотр истории коммитов
# git log

# сокращённый вывод истории (одной строкой)
# git log --oneline

# с ограничением количества записей в логе
# git log --oneline --max-count=2

# показать коммиты за последний промежуток времени
# git log --oneline --since="5 minutes ago"
# git log --oneline --until="5 minutes ago"

# показать коммиты по автору
# git log --oneline --author="Your Name"

# показать все ветки в графическом виде (варианты)
# git log --all --graph

# показ последнего коммита
# git log --max-count=1

# изменение файлов в рабочей директории (пример: добавить тег h1 в hello.html)
# (редактирование файла происходит в любом текстовом редакторе)

# отмена локальных изменений в рабочем каталоге (сброс к последнему коммиту)
# git restore hello.html

# показ содержимого файла (оболочка)
# cat hello.html

# индексирование изменений (подготовка к коммиту)
# git add hello.html

# снятие индексации (удалить из staging area)
# git restore --staged <file>
# git restore --staged hello.html

# отмена проиндексированных изменений и восстановление рабочего каталога
# git restore hello.html

# альтернативы / подсказки, выводимые git status при действиях:
# (use "git add <file>..." to update what will be committed)
# (use "git restore <file>..." to discard changes in working directory)
# (use "git restore --staged <file>..." to unstage)

# Примечание: некоторые примеры используют shell-команды для работы с файлами:
# mv hello.html index.html
# ls -C .git/objects/09
# cat .git/config

# --------------------
# Тема 14. Создание и переключение веток
# --------------------

# показать список веток
# git branch

# создать новую ветку (например, 'experiment')
# git branch experiment

# переключиться на ветку experiment
# git switch experiment

# альтернатива (старый способ переключения)
# git checkout experiment

# создать новую ветку и сразу переключиться на неё
# git switch -c experiment

# вернуться на основную ветку main
# git switch main
