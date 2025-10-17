# Django REST Framework Project with Docker

Этот проект представляет собой Django REST Framework (DRF) приложение, сконтейнеризированное с помощью Docker. В качестве зависимостей используются PostgreSQL в качестве базы данных, Redis в качестве брокера и бэкенда для результатов Celery, а также Celery Beat для выполнения периодических задач.

## Стек технологий

*   **Backend:** Django, Django REST Framework (DRF)
*   **Database:** PostgreSQL
*   **Queue & Cache:** Redis
*   **Async Tasks:** Celery
*   **Scheduler:** Celery Beat
*   **Containerization:** Docker, Docker Compose

## Предварительные требования

Перед началом убедитесь, что на вашей машине установлены:
*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   Создайте в корне проекта .env файл и заполните его по шаблону .env_sample

## Запуск проекта

Следуйте этим шагам, чтобы запустить проект локально.

### 1. Клонирование репозитория

```bash
git clone <your-repository-url>
cd <your-project-directory>