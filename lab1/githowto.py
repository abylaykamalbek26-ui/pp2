# # задать имя пользователя
# git config --global user.name "Your Name"

# # задать email пользователя
# git config --global user.email "your_email@whatever.com"

# # установить main веткой по умолчанию
# git config --global init.defaultBranch main

# # настройка переноса строк (Unix/Mac)
# git config --global core.autocrlf input
# git config --global core.safecrlf warn

# # создание рабочей папки
# mkdir work

# # переход в папку
# cd work

# # создать файл hello.html
# touch hello.html

# # инициализация репозитория
# git init

# # добавить файл в индекс
# git add hello.html

# # первый коммит
# git commit -m "Initial Commit"

# # проверить статус
# git status

# # редактирование файла (пример)
# <h1>Hello, World!</h1>

# # снова добавить файл
# git add hello.html

# # проверить статус
# git status

# # добавить несколько файлов
# git add a.html
# git add b.html

# # закоммитить изменения
# git commit -m "Changes for a and b"

# # добавить другой файл
# git add c.html

# # отдельный коммит для него
# git commit -m "Unrelated change to c"

# # показать журнал коммитов
# git log

# # журнал в одну строку
# git log --pretty=oneline
# git log --oneline --max-count=2
# git log --oneline --since="5 minutes ago"
# git log --oneline --until="5 minutes ago"
# git log --oneline --author="Your Name"
# git log --oneline --all
# git log --all --pretty=format:"%h %cd %s (%an)" --since="7 days ago"

# # переключиться на основную ветку
# git switch main

# # добавить файл в индекс
# git add hello.html

# # проверить состояние
# git status   # показывает, что изменилось

# # добавить все файлы
# git add .    # индексирует все изменения сразу

# # сделать коммит
# git commit -m "message"

# # отправить изменения на GitHub
# git push
