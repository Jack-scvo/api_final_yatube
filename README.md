### Описание проекта:

Проект представляет из себя API для платформы для блогов,
позволяет соронним приложениям взаимодействовать с проектом YaTube.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Jack-scvo/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

Получить список всех постов, начиная с 4-ого, по 4 поста на странице:

```
GET /api/v1/posts/?limit=4&offset=3
```

Получить список всех подписок пользователя:

```
GET /api/v1/follow/
```

Поиск среди подписок пользователя:

```
GET /api/v1/follow?search=leo
```

Редактирование комментария автором:

```
PATCH /api/v1/posts/1/comments/2/
``` 
