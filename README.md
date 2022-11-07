# dj4-vue3-integrate

## What is dj4-vue3-integrate?

This is integrate `django` version `4` and `vue` version `3` project scaffolding

In backend `django4` new feature like native `redis` to cache user session, `drf-spectacular` to build REST-ful api etc. And then custom setup process, there are all command in `Makefile` just need to use `make` command then you can setup everything.

In frontend `vue3` used `typescript` and `quasar` framework to build project, If you want to know more about `quasar` please visit [quasar](https://quasar.dev/). We setup the default `axios` error handler, `axios` interceptor, `vue-router` and `vuex` store. And then we leave the example page for you to build your own project faster.

> If you wish to use other frontend framework, you can remove `frontend` folder and then add your own frontend framework. Just notice that you need to fix build out path in `backed/dist` and assertDir = `static`.

## Setup environment

### Make sure dependence and install by following command

```sh
sudo apt-get install libpq-dev python3-dev make
```

Make sure your python version is up to 3.10, If not. You can install `pyenv`, `pipenv` or other virtualenv for python, at this project we use `pipenv` control python version.

So you can find requirement library in `Pipfile`, Please install it.

---

## Setup development environment

### In local development

Initialize database by following command.

```sh
make createschema # not need todo if you use sqlite
make makemigrations
make migrate
make init-be # setup superuser
make collectstatic # need on prod env
make run-be # run up server
```

Initialize frontend by following command.

```sh
make install-fe # install package
make build-fe # build frontend
make run-fe # run up frontend dev server
```

## Dev environment at docker

In the local we need to prepare `sqlite` or `postgresql` database, and `redis` for cache.

To convenient for developing different environment, we use `docker` to setup development environment.

- `docker-compose.yml` is for all in one development environment
- `docker-compose-db.yml` is for part of database environment
- `docker-compose-redis.yml` is for part of redis environment

It provide setup `postgresql` and `redis` database. And then you can focus on your project.

> For `Redis`, you need to copy `redis.conf.example` to `redis.conf` and then change settings.

Or you can use `make up` command to preview prod environment, it will use `docker-compose.yml` to setup environment.

> There has three developing environments, `dev`, `docker`, `prod`, you can find each `.env.*.example` file in the root directory, you can copy it and rename to `.env` and fill the environment variable.

### Build it for the first time

Use the following command to build without cache

```sh
make cleanbuild
```

### Start the environment

```sh
make up
```

### Tear everything down

If something went wrong and you want to destroy everything, use the following command

```sh
make down
```

In this setup, only the DB service would use the created volume for the database data (/var/lib/postgresql/data/). For the other containers, the main folders are actually a mount to the host. Therefore you can edit the files on the host, and the server running inside the container would get the update and reflect the edited files. The major mount points would be:

- `backend/`
- `package.json`
- `package-lock.json`
- `Pipfile`
- `Pipfile.lock`
- `uwsgi.ini`

## Makefile

In order to make it easier, we use `make` to make the command easy.

Looking for more command at `Makefile` file.

---

## Vscode debug guide

Currently, microsoft support `vscode` debug for `django` and `vue` project.

First, you need to install `vscode` extension `Python` and `Debugger for Chrome`.

Second, you need to create `.vscode/launch.json` file, and then copy the following content.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/backend/manage.py",
      "python": "${command:python.interpreterPath}",
      "args": ["runserver", "0.0.0.0:3002"],
      "django": true,
      "justMyCode": true
    },
    {
      "type": "chrome",
      "request": "launch",
      "name": "Quasar App: chrome",
      "url": "http://localhost:9000",
      "webRoot": "${workspaceFolder}/frontend/src",
      "breakOnLoad": true,
      "sourceMapPathOverrides": {
        "webpack://package-name/./src/*": "${webRoot}/*"
      }
    }
  ]
}
```

## VScode tasks guide

This is good way for clean up all data and restart new environment when you development at local.

Create `settings.json` file in your `.vscode` folder. Then insert following context.

Replace python path by you own.

```json
{
  "python.pythonPath": "path/to/your/python/bin/activate"
}
```

Create `tasks.json` file in your `.vscode` folder. Then run `Init django` task.

Then it will automatically run all tasks.

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Remove migrations",
      "type": "shell",
      "command": "make",
      "args": ["rm-migrations"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Create db schema",
      "dependsOn": ["Remove migrations"],
      "type": "shell",
      "command": "source ${config:python.pythonPath}; make createschema",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Create migrations",
      "dependsOn": ["Create db schema"],
      "type": "shell",
      "command": "source ${config:python.pythonPath}; make makemigrations",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Migrate DB",
      "dependsOn": ["Create migrations"],
      "type": "shell",
      "command": "source ${config:python.pythonPath}; make migrate",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "Init db data",
      "dependsOn": ["Migrate DB"],
      "type": "shell",
      "command": "source ${config:python.pythonPath}; make init-be",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
    {
      "label": "Init django",
      "dependsOn": ["Init db data"],
      "type": "shell",
      "command": "echo 'init django task down'",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```
