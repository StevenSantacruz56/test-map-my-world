# test-map-my-world

## Install make

### Install make Linux

For Debian based distributions like Ubuntu

```bash
sudo apt-get install make
```

For RPM based distributions like CentOS

```bash
sudo yum install make
```

### Install make MAC

```bash
brew install make
```

## Install poetry

```bash
pip install poetry
```

## Deploy localhost

para crear el entorno virtual:

```bash
make create_venv
```

Una vez creado el entrono virtual para ejecutarlo correctamente se debe ejecutar

```bash
make run_env
```

Ejecuta un contenedor Docker utilizando el script 'localhost.yml'.

```bash
make run_docker
```

para ejecutar la aplicacion. Antes de ejecutar la aplicación, se asegura de que el entorno virtual esté creado (make create_venv) y que este dentro del entorno (make run_env).

```bash
make deploy
```

Para contruir una imagen Docker.

```bash
make build_image
```

Valida el estilo de código del módulo 'map_my_world' utilizando flake8.

```bash
make validate_pep8
```
