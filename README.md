[![Python version](https://badgen.net/badge/python/3.10/yellow)](Pipfile)
[![License](https://img.shields.io/github/license/octopusinvitro/advent-of-code-2021)](https://github.com/octopusinvitro/advent-of-code-2021/blob/main/LICENSE)
[![Maintainability](https://api.codeclimate.com/v1/badges/f298667c6c0acac2ef70/maintainability)](https://codeclimate.com/github/octopusinvitro/advent-of-code-2021/maintainability)
[![Build status](https://gitlab.com/octopusinvitro/advent-of-code-2021/badges/main/pipeline.svg)](https://gitlab.com/octopusinvitro/advent-of-code-2021/commits/main)


![AoC2021 logo](header.png)

This year I am going to use python for the challenges, as I feel I need more practice with that language.

Can't promise that I will do the puzzles every day.


## 🛠️ Local development

### Setup

For this project I want to take a look at a setup with `pyenv`, `pyenv-virtualenvwrapper` and `pipenv`, which seems the most similar to an "out of the box" setup with Ruby. If this combination works, the idea is to use it in future python projects.

Check out the [setup](setup.md) instructions.

### Run

See the Log section to see how to run the solution for each day.

### Tests

```sh
pipenv run python -m unittest discover
```

### Linter

```sh
pipenv run flake8
```

