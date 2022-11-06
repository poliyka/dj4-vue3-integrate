# Django4 Vue3(quasar) integrate docker

## Setup environment

Make sure dependence and install by following command

```sh
sudo apt-get install libpq-dev python3-dev make
```

Make sure your python version is up to 3.10, If not. You can install `pyenv`, `pipenv` or other virtualenv for python, at this project we use `pipenv` control python version.

So you can find requirement library in `Pipfile`, Please install it.

---

## Setup development environment

In the local we need to prepare `sqlite` or `postgresql` database, and `redis` for cache.

To convenient for different environment, we use `docker` to setup development environment.

- `docker-compose.yml` is for all in one development environment
- `docker-compose-db.yml` is for part of database environment
- `docker-compose-redis.yml` is for part of redis environment

> There has three developing environments, `dev`, `stage`, `prod`, you can find three `.env.*.example` file in the root directory, you can copy it and rename to `.env` and fill the environment variable.

Initialize database by following command.

```sh
make migrate
make init-backend-db
```

If your need demo data.

```sh
make demo
```

## Dev environment at docker

Make sure which parts you want to be in docker. Edit [.compose-config](.compose-config), comment out the parts you don't want, leave the ones you want. For example, if you want DB, the file should look like this

```sh
dev
# django
```

## Build it for the first time

Use the following command to build without cache

```sh
make cleanbuild
```

## Start the environment

```sh
make up
```

## Tear everything down

If something went wrong and you want to destroy everything, use the following command

```sh
make down
```

## Behind the scene

I hope to ease the environment building processing, and make it diverse to meet everyone's need. This time, there are multiple configuration to docker-compose. Docker is mainly used for the ease of the development purpose, it will not be used in production.

The main docker-compose file would be `docker-compose-dev.yml`. This one contains the database setting. The other one would be `docker-compose-django.yml`, which would be the backend django server, and it depends on the database setting.

You can choose to use:

- Only DB `docker-compose-dev.yml` in the container, so you run django and parcel (npm start) locally. The Django would then connects to the DB container.
- DB + Django `docker-compose-django.yml` in the container, so you run parcel (npm start) locally. I assume this would be the default for front end developers.

How to run the docker? It is pretty easy and straightforward

```sh
docker-compose -f docker-compose-dev.yml up
```

This is the DB only scenario. If you want the DB + Django scenario, merely add another `-f` like the following:

```sh
docker-compose -f docker-compose-dev.yml -f docker-compose-django.yml up
```

In this setup, only the DB service would use the created volume for the database data (/var/lib/postgresql/data/). For the other containers, the main folders are actually a mount to the host. Therefore you can edit the files on the host, and the server running inside the container would get the update and reflect the edited files. The major mount points would be:

- `django/`
- `package.json`
- `package-lock.json`
- `Pipfile`
- `Pipfile.lock`

## Makefile

In order to make it easier, we use `make` to make the command easy. However, the `-f docker-compose-xxx.yml` is still complicated. Therefore, I worte a simple script [args.sh](args.sh). This script reads [.compose-config](.compose-config) and generate the corresponding `-f xxx` arguments for the docker-compose command.

Looking for more command at `Makefile` file.

## VScode tasks pipline example

This is good way for clean up all data and restart new environment when you development at local.

Create `settings.json` file in your `.vscode` folder. Then insert following context.

Replace python path by you own.

```json
{
  "python.pythonPath": "/home/poliyka/.pyenv/versions/3.9.7/envs/gpim/bin/activate"
}
```

Create `tasks.json` file in your `.vscode` folder. Then run `init demo data` task.

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
      "label": "Create migrations",
      "dependsOn": ["Remove migrations"],
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
      "command": "source ${config:python.pythonPath}; make init-backend-db",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    },
    {
      "label": "init demo data",
      "dependsOn": ["Init db data"],
      "type": "shell",
      "command": "source ${config:python.pythonPath}; make demo",
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```
