# Проект по DRF(django rest framework)

### Структура проекта:

project_root/  
├── materials/ 
│   ├── migrations/  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── forms.py  
│   ├── apps.py  
│   ├── models.py  
│   ├── serializers.py  
│   ├── urls.py  
│   └── views.py  
├── config/  
├── .gitignore  
├── .env.sample  
├── manage.py  
├── README.md  
├── poetry.lock    
└── pyproject.toml   

**materials/** - приложение, содержащее модели lesson и course

**users/** - приложение для аутентификации пользователя

**сonfig/** - пакет, содержащий настройки фреймворка django

**manage.py** - скрипт, точка входа, запускает сервер на локалхосте

**pyproject.toml** - файл с зависимостями