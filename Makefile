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

# backend
migrate:
	$(PYVENV_PREFIX) python backend/manage.py migrate

makemigrations:
	$(PYVENV_PREFIX) python backend/manage.py makemigrations

collection:
	$(PYVENV_PREFIX) python backend/manage.py collectstatic

rm-migrations:
	find . -path '*/migrations/__init__.py' -exec truncate -s 0 {} + -o -path '*/migrations/*' -delete

format:
	$(PYVENV_PREFIX) black backend
	$(PYVENV_PREFIX) isort backend

lint:
	$(PYVENV_PREFIX) flake8 backend

test-backend:
	$(PYVENV_PREFIX) python backend/manage.py test backend/

test-backend-tag:
	$(PYVENV_PREFIX) python backend/manage.py test backend/ --tag=$(t)

test-backend-path:
	$(PYVENV_PREFIX) python backend/manage.py test $(p)

shell:
	$(PYVENV_PREFIX) python backend/manage.py shell

run-backend:
	$(PYVENV_PREFIX) python backend/manage.py runserver 0.0.0.0:3002

create-user:
	$(PYVENV_PREFIX) python backend/manage.py createsuperuser

schema:
	$(PYVENV_PREFIX) python backend/manage.py spectacular --file schema.yml

# none: initialize database
# -f, --force : force clear registry first
demo:
	$(PYVENV_PREFIX) python backend/manage.py simulate $(a)

# none: initialize database
# -f, --force : force clear registry first
init-backend-db:
	$(PYVENV_PREFIX) python backend/manage.py initialize $(a)

# Schema 關係圖
erd:
	$(shell $(PYVENV_PREFIX) python backend/manage.py graph_models -a > ./doc/erd/erd.dot && $(PYVENV_PREFIX) python backend/manage.py graph_models --pydot -a -g -o ./doc/erd/erd.png)
