[![AoC 2021 total stars](https://img.shields.io/badge/2021-★_2-ffe300)](https://adventofcode.com/2021)
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

## 🗓️ Logs

| Puzzle                                                      |  Stars                                                                     | 📃                    |
| ----------------------------------------------------------- | :------------------------------------------------------------------------: | :-------------------: |
| **[01: Sonar Sweep](https://adventofcode.com/2021/day/1)**  | [![Day 01](https://badgen.net/badge/01/%E2%98%85%E2%98%85/yellow)](#day01) | [log](#day-1)         |


### Day 1

[Solution](aoc/d01/solution.py)

To run:

```sh
pipenv run python aoc/d01.py data/d01_input
```

There is no need to build an list of duplets or a list of triplets from the original list. If the original list is long, we will use a lot of memory for no reason. In this puzzle we can do all the operations as we slide through the original list.

**What went well:**
* I finished both puzzles
* The python setup I'm trying seems to work

**What went wrong:**
* I finished the solution fast and it was short, but then I wanted to improve it and got lost adding exception handling for file opening and integer conversion etc. as well as printing stuff on the terminal. Tomorrow I'll avoid error handling and will just solve the puzzles.
* Still have a lot to learn about functional python, feels like the refactoring left the code more unreadable.
