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
	$(PYVENV_PREFIX) python backend/manage.py shell

run-be:
	$(PYVENV_PREFIX) python backend/manage.py runserver 0.0.0.0:3002

create-user:
	$(PYVENV_PREFIX) python backend/manage.py createsuperuser

create-schema:
	$(PYVENV_PREFIX) python backend/manage.py createschema

schema-be:
	$(PYVENV_PREFIX) python backend/manage.py spectacular --file schema.yml

# none: insert demo data
# -f, --force : force clear origin data
demo-be:
	$(PYVENV_PREFIX) python backend/manage.py simulate $(a)

# none: initialize database
# -f, --force : force clear registry first
init-be:
	$(PYVENV_PREFIX) python backend/manage.py initialize $(a)

# db
migrate:
	$(PYVENV_PREFIX) python backend/manage.py migrate

makemigrations:
	$(PYVENV_PREFIX) python backend/manage.py makemigrations

collectstatic:
	$(PYVENV_PREFIX) python backend/manage.py collectstatic

rm-migrations:
	find . -path '*/migrations/__init__.py' -exec truncate -s 0 {} + -o -path '*/migrations/*' -delete


# Schema 關係圖
erd:
	$(shell $(PYVENV_PREFIX) python backend/manage.py graph_models -a > ./doc/erd/erd.dot && $(PYVENV_PREFIX) python backend/manage.py graph_models --pydot -a -g -o ./doc/erd/erd.png)
