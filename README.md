# dj4-vue3-integrate

- [dj4-vue3-integrate](#dj4-vue3-integrate)
  - [Background](#background)
    - [Fronend](#fronend)
    - [Backend](#backend)
    - [Custom setup process](#custom-setup-process)
      - [For using other frontend framework (Optional)](#for-using-other-frontend-framework-optional)
  - [Install](#install)
  - [Setup development environment](#setup-development-environment)
    - [Makefile](#makefile)
    - [In local development](#in-local-development)
    - [Dev environment in docker](#dev-environment-in-docker)
    - [Build it for the first time](#build-it-for-the-first-time)
    - [Start the environment](#start-the-environment)
    - [Tear everything down](#tear-everything-down)
  - [VScode guide](#vscode-guide)
    - [VScode guide - debug](#vscode-guide---debug)
    - [VScode guide - tasks](#vscode-guide---tasks)

---

## Background

`Dj4-vue3-integrate` is a project scaffolding integrating `django` version `4` and `vue` version `3`.

### Fronend

- Used `vue3`, `typescript`, and `quasar` framework to build project.
  ( Detailed about `quasar`, please visit [quasar](https://quasar.dev/). )

### Backend

- Used `django4`.
- New feature
  - Use native `redis` to cache user session
  - Use `drf-spectacular` to build REST-ful api

### Custom setup process

- Use `make` command to execute `Makefile` to setup everything
- We setup the default `axios` error handler, `axios` interceptor, `vue-router` and `vuex` store.
- There's an example page for you to build your own project faster.

#### For using other frontend framework (Optional)

1. remove `frontend` folder
2. add your own frontend framework

> ⭐️ **NOTICE**
>
> - fix build out path in `backed/dist`
> - make assertDir = `static`

## Install

Make sure dependencies and installation.
Go check them out by following command if you don't have them locally installed.

```sh
sudo apt-get install libpq-dev python3-dev make
```

This project uses `pipenv` control python version, so make sure your python version is up to 3.10.
If not, You can install `pyenv`, `pipenv` or other virtualenv for python.

Install requirement library in `Pipfile`.

## Setup development environment

### Makefile

In order to make it easier, we use `make`, look up more commands in `Makefile` file.

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

### Dev environment in docker

Need to prepare `sqlite` or `postgresql` database, and `redis` for cache in local.

In order to make it more convenient for developing in different environment, we use `docker`.

Files description:

- `docker-compose.yml` is for all in one development environment
- `docker-compose-db.yml` is for part of database environment
- `docker-compose-redis.yml` is for part of redis environment

Files above provide setup `postgresql` and `redis` database for you to focus on your project.

> ⭐️ **NOTICE** : For `Redis`, you need to copy `redis.conf.example` to `redis.conf` and then change settings.

You can use `make up` command to preview prod environment, it will use `docker-compose.yml` to setup environment.

> ⭐️ **NOTICE** : There are three developing environments : `dev`, `docker`, `prod`.
> There are three corresponding `.env.*.example` files in the root directory, you can copy it and rename to `.env` and change your environment variable.

### Build it for the first time

Use following command to build the project without cache.

```sh
make cleanbuild
```

### Start the environment

Use following command to start the environment.

```sh
make up
```

### Tear everything down

Use following command if something is wrong and you want to destroy everything.

```sh
make down
```

Only the DB service would use the created volume for the database data (`/var/lib/postgresql/data/`) in this setup.

For other containers, you can edit the files on the host, and the server running inside the container would update and reflect those edited files.

Major mount points would be as below :

- `backend/`
- `package.json`
- `package-lock.json`
- `Pipfile`
- `Pipfile.lock`
- `uwsgi.ini`

## VScode guide

### VScode guide - debug

Currently, microsoft support `vscode` debug for `django` and `vue` projects.

1. Install `vscode` extension `Python` and `Debugger for Chrome`.
2. Create `.vscode/launch.json` file, then copy the following content.

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

### VScode guide - tasks

This is good way to clean up all data and restart new environment when you develope locally.

- Create `settings.json` file in your `.vscode` folder. Then insert following context.
- Replace python path by you own.

```json
{
  "python.pythonPath": "path/to/your/python/bin/activate"
}
```

- Create `tasks.json` file in your `.vscode` folder. Then run `Init django` task, it will automatically run all tasks.

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
