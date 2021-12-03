[![AoC 2021 total stars](https://img.shields.io/badge/2021-★_4-ffe300)](https://adventofcode.com/2021)
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

For example for day one:

```sh
. bin/run d01
```

### Tests

```sh
. bin/test                 # all tests
. bin/test tests/a_test.py # single test
```

### Linter

```sh
. bin/lint
```

### Folder structure

```sh
.
├── aoc
│   ├── dXX
│   │   ├── __init__.py
│   │   └── solution.py
│   ├── __init__.py
│   ├── file_parser.py
│   └── logger.py
├── data
│   └── dXX_input
├── tests
│   ├── dXX
│   │   ├── fixtures/
│   │   ├── __init__.py
│   │   └── test_solution.py
│   ├── __init__.py
│   └── test_file_parser.py
└── dXX.py
```


## 🗓️ Logs

| Puzzle                                                      |  Stars                                                                     | 📃             |
| ----------------------------------------------------------- | :------------------------------------------------------------------------: | :------------: |
| **[01: Sonar Sweep](https://adventofcode.com/2021/day/1)**  | [![Day 01](https://badgen.net/badge/01/%E2%98%85%E2%98%85/yellow)](#day-1) | [log](#day-1)  |
| **[02: Dive!](https://adventofcode.com/2021/day/2)**        | [![Day 02](https://badgen.net/badge/02/%E2%98%85%E2%98%85/yellow)](#day-2) | [log](#day-2)  |


### Day 1

[Solution](aoc/d01/solution.py)

There is no need to build a list of duplets or a list of triplets from the original list. If the original list is long, we will use a lot of memory for no reason. In this puzzle we can do all the operations as we slide through the original list.

**What went well:**
* I finished both puzzles
* The python setup I'm trying seems to work

**What went wrong:**
* I finished the solution fast and it was short, but then I wanted to improve it and got lost adding exception handling for file opening and integer conversion etc. as well as printing stuff on the terminal. Tomorrow I'll avoid error handling and will just solve the puzzles.
* Still have a lot to learn about functional python, feels like the refactoring left the code more unreadable.


### Day 2

[Solution](aoc/d02/solution.py)

I created a `Position` class to store the horizontal and depth coordinates and a method to calculate its product.
Then I accumulated the results of the calculations in a dictionary.
I also created an enum for the direction, although plain constants would have worked (and are less verbose).

**What went well:**
* The logic I had dismissed in day one turned out to be useful for today too so I extracted it into generic classes.
* I didn't get distracted with input validation for the new input file.

**What went wrong:**
* More python learning, not really "wrong", but I am not a fan of the python import system. In order to have a generic file parser and logger that all solutions can use, I had to move the `dXX.py` files under the root folder to avoid the "`ImportError: attempted relative import beyond top-level package`". [This SO answer](https://stackoverflow.com/a/57292232) explains the solution to my issue. I guess I am spoiled by Ruby, where you can do `require_relative '../any/where'` and it works™.
