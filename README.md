# Spark Sandbox

This repository provides a sample Spark environment that speeds up the process of getting started developing PySpark solutions locally. It utilizes [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) which has been embellished with various extensions in order to create the optimum environment for Spark-based development.

## Pre-requisites

- [VS Code](https://code.visualstudio.com/download)
- [Docker](https://code.visualstudio.com/docs/devcontainers/containers#_installation)
- [VS Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Full instructions on how to support Dev Containers on any operating system can be found here: [Dev Containers installation](https://code.visualstudio.com/docs/devcontainers/containers#_installation).

## Installation

1. Ensure Docker is running on your machine.
    - If you're using Docker Desktop, you can check in your system tray to check whether Docker Desktop is running by looking for the docker icon.
    - Otherwise you will need to [start the Docker daemon another way](https://docs.docker.com/config/daemon/start/).
2. Clone the repo and open the root `spark-sandbox` folder in VS Code. 
3. VS Code should detect the existence of the [.devcontainer](/.devcontainer) configuration and provide a popup to reopen the folder within the Dev Container. Select "Reopen in container".
    - If you don't see this popup, hit `Ctrl + Shift + P` to open the command pallete and type in `Dev Containers: Open Folder in Container`.
4. This should start building the container in the background.
    - Clicking the "Starting Dev Container (show log)" popup will show the progress of the container build
5. The Dev Container build should complete in 5 minutes or so on first load. After this it should be cached by Docker so subsequent loads are incremental should anything have been changed.
    - Sometimes a popup will appear after the container finishes building indicating that some of the Dev Container VS Code extensions can't be activated. This seems to be some sort of race condition depending on the load order of the various extensions. Clicking "Reload Window" invariably fixes this issue.

## Repository components

### Dev Container configuration

In the [.devcontainer](.devcontainer) folder you'll find the [devcontainer.json](.devcontainer/devcontainer.json) config file and the corresponding [Dockerfile](.devcontainer/Dockerfile).

The [devcontainer.json](.devcontainer/devcontainer.json) is fairly simple. It references the [Dockerfile](.devcontainer/Dockerfile) passing in configurable arguments, includes a handful of VS Code extensions and a few other properties such as a `postCreateCommand` to trigger the `poetry install` (see `poetry` description further below).

The [Dockerfile](.devcontainer/Dockerfile) inherits its base (linux) image from [Microsoft's python-3 Dev Container base file](https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/.devcontainer/base.Dockerfile), and adds a few elements on top of this:

- [Spark](https://spark.apache.org/downloads.html) (including [Java SDK](https://packages.debian.org/sid/openjdk-11-jre))
- [poetry](https://python-poetry.org/docs/) - for dependency management and packaging
- [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/install-debian?view=powershell-7.3) - common Microsoft scripting language

### Poetry

Poetry is an environment management, dependency management and packaging tool for Python. It's closest alternative is probably `pipenv`, with some additional functionality (like publishing of packages without requiring supplementary file/packages (like `pipenv` requires `setup.py`)). It provides a powerful CLI and simplifies the ALM of Python
apps.



### Other components

- [Sample Github Action Workflow](.github/workflows/python-app.yml)
- [flake8 linting configuration file](.flake8)
- 