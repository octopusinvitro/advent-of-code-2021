# Setup

Install `pyenv`:
https://github.com/pyenv/pyenv

Install the `pyenv-virtualenvwrapper` plugin:
https://github.com/pyenv/pyenv-virtualenvwrapper

Use `pyenv` to install the last version of python alongside other python versions in your system:

```sh
pyenv install 3.10.0
# adds 3.10.0 folder to $HOME/.pyenv/versions/3.10.0
pyenv local 3.10.0
# creates .python-version containing 3.10.0
```

Add an alias to your `.bash_aliases` file:

```sh
alias python="$HOME/.pyenv/shims/python"
alias pipenv="python -m pipenv"
```

In the directory where the `.python-version` file is:

```sh
python3 --version
# Python 3.8.10

python --version
# Python 3.10.0
```

Upgrade `pip` for that version of python:

```sh
python -m pip install --upgrade pip
# upgrade output

python -m pip --version
# pip 21.3.1 from $HOME/.pyenv/versions/3.10.0/lib/python3.10/site-packages/pip (python 3.10)
```

Install `pipenv` for that version of python:

```sh
python -m pip install pipenv
# install output

pipenv --version
# pipenv, version 2021.11.23
```

Use `pyenv-virtualenvwrapper` to  create a python environment for the project:

```sh
mkvirtualenv -a . advent-of-code-2021
```

Check that the environment was created and that the `.project` file points to the right place:

```sh
ls $WORKON_HOME/
# advent-of-code-2021

more $WORKON_HOME/advent-of-code-2021/.project
# /path/to/advent-of-code
```

Activate or deactivate the environment:

```sh
workon advent-of-code-2021
deactivate
```

Install dependencies:

```sh
workon advent-of-code-2021
pipenv install
```
