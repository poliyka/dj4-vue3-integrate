include .env
export $(shell sed 's/=.*//' .env)

PYVENV_PREFIX=pipenv run
DOCKER_COMPOSE=docker-compose

# docker
build:
	$(DOCKER_COMPOSE) build

cleanbuild:
	$(DOCKER_COMPOSE) build --no-cache

up:
	$(DOCKER_COMPOSE) up --build

down:
	$(DOCKER_COMPOSE) down -v

# frontend
run-fe:
	cd frontend; npm run dev

build-fe:
	cd frontend; npm run build

format-fe:
	cd frontend; npm run format

lint-fe:
	cd frontend; npm run lint

install-fe:
	cd frontend; npm install $(a)

# backend
format-be:
	$(PYVENV_PREFIX) black backend
	$(PYVENV_PREFIX) isort backend

lint-be:
	$(PYVENV_PREFIX) flake8 backend

test-be:
	$(PYVENV_PREFIX) python backend/manage.py test backend/

test-be-tag:
	$(PYVENV_PREFIX) python backend/manage.py test backend/ --tag=$(t)

test-be-path:
	$(PYVENV_PREFIX) python backend/manage.py test $(p)

shell-be:
	$(PYVENV_PREFIX) python backend/manage.py shell_plus --print-sql

run-be:
	$(PYVENV_PREFIX) python backend/manage.py runserver 0.0.0.0:$(BACKEND_PORT)

create-user:
	$(PYVENV_PREFIX) python backend/manage.py createsuperuser

create-schema:
	$(PYVENV_PREFIX) python backend/manage.py createschema

schema-be:
	$(PYVENV_PREFIX) python backend/manage.py spectacular --file schema.yml

# Initialize

# none: initialize database
# -f, --force : force clear registry first
init-be:
	$(PYVENV_PREFIX) python backend/manage.py initialize $(a)

init-age:
	$(PYVENV_PREFIX) python backend/manage.py age_jcs_graph $(a)

init-neo4j:
	$(PYVENV_PREFIX) python backend/manage.py neo4j_jcs_graph $(a)

# i18n
# 更新翻譯檔
# zh_Hant: 繁體中文, zh_Hans: 簡體中文, en: 英文
build-i18n:
	cd backend; $(PYVENV_PREFIX) django-admin makemessages -l $(a)

compile-i18n:
	cd backend; $(PYVENV_PREFIX) django-admin compilemessages

# celery
run-celery:
	cd backend; $(PYVENV_PREFIX) celery -A schedule worker -l info

run-celery-beat:
	cd backend; $(PYVENV_PREFIX) celery -A schedule beat -l info

# db
migrate:
	$(PYVENV_PREFIX) python backend/manage.py migrate

makemigrations:
	$(PYVENV_PREFIX) python backend/manage.py makemigrations

pgmakemigrations:
	$(PYVENV_PREFIX) python backend/manage.py pgmakemigrations

pgpartition:
	$(PYVENV_PREFIX) python backend/manage.py pgpartition -y

collectstatic:
	$(PYVENV_PREFIX) python backend/manage.py collectstatic

inspectdb:
	$(PYVENV_PREFIX) python backend/manage.py inspectdb > ${a}

rm-migrations:
	find . -path '*/migrations/__init__.py' -exec truncate -s 0 {} + -o -path '*/migrations/*' -delete


# Schema 關係圖
# 使用前要先安裝 sudo apt install graphviz
# 否則會有 FileNotFoundError: [Errno 2] "dot" not found in path.
erd:
	$(shell $(PYVENV_PREFIX) python backend/manage.py graph_models -a > doc/erd/erd.dot && $(PYVENV_PREFIX) python backend/manage.py graph_models --pydot -a -g -o doc/erd/erd.png)
