[![AoC 2021 total stars](https://img.shields.io/badge/2021-★_36-ffe300)](https://adventofcode.com/2021)
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
. bin/run 01
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
└── run.py
```


## 🗓️ Logs

| Puzzle                                                                  |  Stars                                                                      | 📃             |
| ----------------------------------------------------------------------- | :-------------------------------------------------------------------------: | :------------: |
| **[01: Sonar Sweep](https://adventofcode.com/2021/day/1)**              | [![Day 01](https://badgen.net/badge/01/%E2%98%85%E2%98%85/yellow)](#day-01) | [log](#day-01) |
| **[02: Dive!](https://adventofcode.com/2021/day/2)**                    | [![Day 02](https://badgen.net/badge/02/%E2%98%85%E2%98%85/yellow)](#day-02) | [log](#day-02) |
| **[03: Binary Diagnostic](https://adventofcode.com/2021/day/3)**        | [![Day 03](https://badgen.net/badge/03/%E2%98%85%E2%98%85/yellow)](#day-03) | [log](#day-03) |
| **[04: Giant Squid](https://adventofcode.com/2021/day/4)**              | [![Day 04](https://badgen.net/badge/04/%E2%98%85%E2%98%85/yellow)](#day-04) | [log](#day-04) |
| **[05: Hydrothermal Venture](https://adventofcode.com/2021/day/5)**     | [![Day 05](https://badgen.net/badge/05/%E2%98%85%E2%98%85/yellow)](#day-05) | [log](#day-05) |
| **[06: Lanternfish](https://adventofcode.com/2021/day/6)**              | [![Day 06](https://badgen.net/badge/06/%E2%98%85%E2%98%85/yellow)](#day-06) | [log](#day-06) |
| **[07: The Treachery of Whales](https://adventofcode.com/2021/day/7)**  | [![Day 07](https://badgen.net/badge/07/%E2%98%85%E2%98%85/yellow)](#day-07) | [log](#day-07) |
| **[08: Seven Segment Search](https://adventofcode.com/2021/day/8)**     | [![Day 08](https://badgen.net/badge/08/%E2%98%85%E2%98%85/yellow)](#day-08) | [log](#day-08) |
| **[09: Smoke Basin](https://adventofcode.com/2021/day/9)**              | [![Day 09](https://badgen.net/badge/09/%E2%98%85%E2%98%85/yellow)](#day-09) | [log](#day-09) |
| **[10: Syntax Scoring](https://adventofcode.com/2021/day/10)**          | [![Day 10](https://badgen.net/badge/10/%E2%98%85%E2%98%85/yellow)](#day-10) | [log](#day-10) |
| **[11: Dumbo Octopus](https://adventofcode.com/2021/day/11)**           | [![Day 11](https://badgen.net/badge/11/%E2%98%85%E2%98%85/yellow)](#day-11) | [log](#day-11) |
| **[12: Passage Pathing](https://adventofcode.com/2021/day/12)**         | [![Day 12](https://badgen.net/badge/12/%E2%98%85%E2%98%85/yellow)](#day-12) | [log](#day-12) |
| **[13: Transparent Origami](https://adventofcode.com/2021/day/13)**     | [![Day 13](https://badgen.net/badge/13/%E2%98%85%E2%98%85/yellow)](#day-13) | [log](#day-13) |
| **[14: Extended Polymerization](https://adventofcode.com/2021/day/14)** | [![Day 14](https://badgen.net/badge/14/%E2%98%85%E2%98%85/yellow)](#day-14) | [log](#day-14) |
| **[15: Chiton](https://adventofcode.com/2021/day/15)**                  | [![Day 15](https://badgen.net/badge/15/%E2%98%85%E2%98%85/yellow)](#day-15) | [log](#day-15) |
| **[16: Packet Decoder](https://adventofcode.com/2021/day/16)**          | [![Day 16](https://badgen.net/badge/16/%E2%98%85%E2%98%85/yellow)](#day-16) | [log](#day-16) |
| **[17: Trick Shot](https://adventofcode.com/2021/day/17)**              | [![Day 17](https://badgen.net/badge/17/%E2%98%85%E2%98%85/yellow)](#day-17) | [log](#day-17) |
| **[18: Snailfish](https://adventofcode.com/2021/day/18)**               | [![Day 18](https://badgen.net/badge/18/%E2%98%85%E2%98%85/yellow)](#day-18) | [log](#day-18) |


### Day 01

[Solution](aoc/d01/solution.py)

There is no need to build a list of duplets or a list of triplets from the original list. If the original list is long, we will use a lot of memory for no reason. In this puzzle we can do all the operations as we slide through the original list.

**What went well:**
* I finished both puzzles
* The python setup I'm trying seems to work

**What went wrong:**
* I finished the solution fast and it was short, but then I wanted to improve it and got lost adding exception handling for file opening and integer conversion etc. as well as printing stuff on the terminal. Tomorrow I'll avoid error handling and will just solve the puzzles.
* Still have a lot to learn about functional python, feels like the refactoring left the code more unreadable.


### Day 02

[Solution](aoc/d02/solution.py)

I created a `Position` class to store the horizontal and depth coordinates and a method to calculate its product.
Then I accumulated the results of the calculations in a dictionary.
I also created an enum for the direction, although plain constants would have worked (and are less verbose).

I liked [this Typescript solution](https://github.com/pmareke/advent-of-code/blob/main/src/2021/day_02/submarine.ts) from @pmareke.

**What went well:**
* The logic I had dismissed in day one turned out to be useful for today too so I extracted it into generic classes.
* I didn't get distracted with input validation for the new input file.

**What went wrong:**
* More python learning, not really "wrong", but I am not a fan of the python import system. In order to have a generic file parser and logger that all solutions can use, I had to move the `dXX.py` files under the root folder to avoid the "`ImportError: attempted relative import beyond top-level package`". [This SO answer](https://stackoverflow.com/a/57292232) explains the solution to my issue. I guess I am spoiled by Ruby, where you can do `require_relative '../any/where'` and it works™.


### Day 03

[Solution](aoc/d03/solution.py)

The selection logic smelled of recursion, but I managed to do it with a simple while and I think it's more readable.

For performance I am looping through the report just once, as opposed to other solutions that loop through the bits first, and then through the whole report for every bit (12 times!).

**What went well:**
* It's the first day that I like my solution more than others

**What went wrong:**
* Still don't know enough functional python, which would have helped in simplifying those loops.


### Day 04

[Solution](aoc/d04/solution.py)

Octopus plays against squid. He he.

I created a board to check for wins and a bingo parser to get the numbers and the boards as board objects. To find the last winner board I compare the index of the winners in the previous loop with the current loop.

**What went well:**
* It was kind of like doing a tic tac toe which I've done a looooot of times

**What went wrong:**
* Because it's similar to tic tac toe I thought I will do it faster but I spend most of the time fighting with Python.


### Day 05

[Solution](aoc/d05/solution.py)

I created a `Line` class to calculate the points and check if a line is a diagonal. We don't need the whole grid for this, just a hash to store the sums for points in each line as they come.

**What went well:**
* Today was easier than the previous days! :D

**What went wrong:**
* At first I had a method to pass a line to a line and calculate its intersection points, but hashes are always more performant.


### Day 06

[Solution](aoc/d06/solution.py)

Today everyone tripped in the second part with an OOM, while finishing part one in like 15 minutes :D

I too used an array and brute force for the first part; the description of the problem kind of tricks you into thinking in fish rather than thinking in days. Then you realize this is just a cycle that repeats, and you model the problem in the right way to avoid the memory explosion. After that, I got better execution times:

Part 1: `0.10 ms`  
Part 2: `0.22 ms`

With a solution based in days rather than fish, there is no need to calculate the population generated by each fish separately and then sum it up, you can calculate the population for any amount of initial fish all at once.

**What went well:**
* It took some time to find the answer to part 2, but it wasn't too difficult. I almost got distracted by the idea of bits and bytes, since the period is 7 days and then it asks for 256 days. Thankfully I didn't go down that path. It's probably just a number carefully chosen by the author to explode our computers :D

**What went wrong:**
* The memory explosion surprise :D


### Day 07

[Solution](aoc/d07/solution.py)

Graphic description of today's puzzle:  
:octopus::bangbang: ....... :zap::whale::zap: ........:gun: :crab::crab::crab::crab::crab::crab: :bomb:

Jokes aside, today's solution could totally be done by brute force, calculating the sums of all differences and then finding the minimum sum. However, day 6 left me too scared to do that :D

When I read about optimizing differences it reminded me of linear regressions and the least squares method, and then the crab positions sounded like a histogram. When modelling the problem this way, and remembering a bit of statistics from uni, I thought the concept of median may work here, as it is the value right in the middle of a distribution.

For part two I remembered from uni that the quadratic formula `(n + 1) * n / 2` is the sum of a linear progression of n numbers, so I saved a loop there!. In this case we have to calculate the mean, but this worked only for the input, and not for the sample :thinking:. It's been a while since I did these kind of maths so I'm a bit rusty, and I didn't want to spend too much time on it so I did the brute-force method as well. But I will like to come back later to it because I am sure there is a simple solution using maths.

P.S. Someone wrote [a paper on this puzzle](https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/) :D


### Day 08

[Solution](aoc/d08/solution.py)

**What went well:**
* I really enjoyed working on this one!

**What went wrong:**
* First I got it wrong thinking the scrambled patterns could be mapped directly, until I noticed there were several 5 configurations for the same entry. Then I couldn't make the correct implementation work, so I surrendered to brute-forcing it by calculating all the 5000 permutations of `abcdefg` and using them to find the correct mappings. Not proud, but this puzzle was taking too much time :sweat_smile::sweat_drops:.


### Day 09

[Solution](aoc/d09/solution.py)

Today's puzzle reminded me of the "game of life", which I have solved many times. However once I started working on it, it was a bit different.

I solved the second part using recursion. I created a `Location` class for all location-related stuff like finding neighbours or keeping track of visited locations. Then I created a `Heightmap` class, with all the operations related with the actual values of height, like finding the basins.

**What went well:**
* It wasn't too difficult and I used a bit of the experience gained solving "game of life".

**What went wrong:**
* I solved the second part using the neighbours with recursion, but it didn't work for a while because I had a `return` in the wrong place and that drove me crazy. Also, puzzles are starting to take longer to solve, not because they are difficult but because there's more code to write. **So from now on I may not be able to do a puzzle a day.**


### Day 10

[Solution](aoc/d10/solution.py)

This one was easy and took less time in comparison with the previous.

I scan a line and keep track of the opening characters. When I find a closing character, I pop the last opening character. If it doesn't correspond, it's a corrupt line, if it does, it's an incomplete line.

The file is parsed once, and the illegal characters and closing sequences collected. Then they are passed to a sorting class that knows how to sort each.

**What went well:**
* It was short and fast to do!

**What went wrong:**
* Nothing.


### Day 11

[Solution](aoc/d11/solution.py)

Another example that can be solved with recursion. Also, **dumbo octopus**! Like the one I have in my Github presentation :D

This one was visualization material! I'm as skilled as I'd like to but some people did some nice ones like [this](https://www.youtube.com/watch?v=GsSI8O_w33Q), and [this](https://imgur.com/a/xhPgdGX).

**What went well:**
* I could reuse my location class from day 9, and learned how to make a deep copy of an array in python.

**What went wrong:**
* At first I wasn't getting the right result on the second part, but the tests were passing. The only difference between running the solution and running the tests was that the lines were read only once in the solution. That gave me the idea to deepcopy the array instead of just assigning it.


### Day 12

[Solution](aoc/d12/solution.py)

Wow this one was time consuming! I got it working after filling in 6 or 7 pages of manual recursion and `ipdb` is on fire :fire: :D

At first I thought about [the Dijkstra algorithm](https://en.wikipedia.org/wiki/Dijkstra's_algorithm) which we had to implement at work, but it's used to find the shortest path and here we want to find all the paths. So I ended up with a more manual solution using recursion. If I had more time I would have given it a go.

**What went well:**
* One of the problems I had was that after coming back from a recursion stack into the previous for loop when finishing a path, the changes done to the path and the visited caves had to be undone back to that point. I remembered that solving an unbeatable tic tac toe with a minimax algorithm presents the same problem, and it is solved by creating a deep copy of the data structure and making the changes to the copy, then passing the copy to the next recursion stack. It worked here too!

* Also, I had to perform the same operation (deep copy plus appending a new item) in both the path list and the visited set, so I wanted to extract this common logic, but lists and sets don't have any common methods to add items. That's how I learned about `itertools.chain`! I then just have to cast it to list or set.

**What went wrong:**
* These problems are not necessarily difficult or complex, but they are very time consuming. I wish I knew a way to not have to sit and manually follow the loops both with pen and paper and with `ipdb` in the CLI in order to debug it.


### Day 13

[Solution](aoc/d13/solution.py)

I loved today's puzzle, it wasn't too time consuming and it could be solved just with sets and using geometry, without making a grid until the very end, when you need to visualize it to read the code.

For the vertical fold, the cell index doesn't change, and the the row index is unchanged too from zero to the folding coordinate. Beyond the folding coordinate, we have to swap the rows and bring them up, so the conversion is twice the row index minus the folding coordinate: `2 * (row - coordinate)` or `2 * coordinate - row`:

```py
def _fold_row(self, row, coordinate):
    return row if row <= coordinate else 2 * coordinate - row
```

For the horizontal fold, the row index doesn't change, and the cell index has to be swapped from zero to the folding coordinate, and beyond the folding coordinate it has to be moved to the left. The swapped cell indexes can be calculated as the coordinate minus the cell index minus one, while the ones beyond the folding point would be the cell index minus the coordinate minus one. In other words, we can take the absolute value of that difference:

```py
def _fold_cell(self, cell, coordinate):
    return cell if cell == coordinate else abs(cell - coordinate) - 1
```

This is the code I got!

```
 #  # #  #  ##     #  ### ####  ### ##
 #  #  # # #  #    # #  # #    #  # #
 ####   ##    #    #  ###  #   #  # #
 #  #  # # ## #    # #  #   #   ### #
 #  #  # # #  #    # #  #    #  # # #  #
 #  # #  # ###  ####  ### #### #  #  ##
```

It's mirrored! I changed the display logic to reverse it and space the cells:

```
    # #   # # #     # # # #   # # #     #           # #     #     #   #     #
      #   #     #         #   #     #   #         #     #   #   #     #     #
      #   #     #       #     # # #     #         #         # #       # # # #
      #   # # #       #       #     #   #         #   # #   #   #     #     #
#     #   #   #     #         #     #   #         #     #   #   #     #     #
  # #     #     #   # # # #   # # #     # # # #     # # #   #     #   #     #
```

It's now easy to see that my code is `JRZBLGKH` :D
What was your code?


### Day 14

[Solution](aoc/d14/solution.py)

As someone pointed out, this puzzle was very similar to that on day 6! First part solved easily, second part explodes laptop and you need to model the problem differently.

I stored the counts of the new insertions but also the counts of the new pairs formed in every step, so that I could use them in the next iteration.

This one took a lot of pen and pencil again, to figure out the right algorithm! At first I had the pairs in a "visited" set, but the trick was that at some point the pairs repeat as well, which is why you need to keep track of their counts too, so that you can count the elements properly.


### Day 15

[Solution](aoc/d15/solution.py)

This puzzle was an opportunity to implement the Dijkstra algorithm, which searches for the shortest path between two points in a graph.

I decided to read a bit about it and found [this article](https://www.redblobgames.com/pathfinding/a-star/introduction.html) shared online, which is really nice and has cool animations. I went for an implementation that includes a heuristic in the weight assigned to each node, since we have specific start and end nodes and this can speed up the search.


### Day 16

[Solution](aoc/d16/solution.py)

This puzzle brought back [very, very old memories from my thesis](http://octopusinvitro.gitlab.io/blog/code-and-tech/magnetic-tapes-and-octal-dump-3/), where I had to read list mode files in a similar way to this puzzle. They were stored in magnetic tapes and written using a system called GOOSY developed at GSI. There are still several [very](http://www.khschmidts-nuclear-web.eu/Work_data/Ghelp/Goosydata.htm) [old](https://www-win.gsi.de/frs/technical/daq/frs-unpacking-goosy.asp) pages online about it! And even [the GOOSY buffer documentation](http://web-docs.gsi.de/~go4/goosy/GM_BUFFER.pdf) where the structure of the headers, events and subevents is described (for example, in page 12).

The difference is that back then I had just events with subevents, while here I have packets with subpackets with subpackets, etc. In GOOSY you had short words that were one octal size, so we processed the input in octals rather than hexadecimal. And finally, I am implementing this in python instead of C++, and have (hopefully) come a long way in my coding since then! :D

In this case I used recursion to find all the packets inside the packets and also applied a design pattern called "[composite](https://refactoring.guru/design-patterns/composite)", which is good for when you have tree structures where the trees and the leaves have the same API but the trees can contain leaves inside.

To fully make it a composite it would be good to create a packet class for every type to encapsulate the knowledge of how to calculate the different values. But I was lazy and just created a `Calculator` class to do all the calculations :D


### Day 17

[Solution](aoc/d17/solution.py)

In today's puzzle we could solve the first part with maths from day 7, and I am sure the second part could also be solved without using brute force, sadly I didn't figure out how. This will be another puzzle to take a look at again after AoC is over!

We shoot a probe. The `x` component of the velocity always decreases by one unit in every step, until it gets stuck at zero forever. The `y` component always decreases by one unit forever. This means that the `x` component of the position always increases, slower every time, until it saturates at a value when the `x` component of the velocity reaches zero. The `y` component of the position may or may not go up at first and then it always decreases.

The initial value of the `y` component of the velocity is the maximum it will ever have, then it decreases by one in every step. When the `y` velocity becomes zero, the `y` position is at its maximum, then both velocity and position decrease. That means when we go up from zero we are adding to the `y` position `Vy`, plus `Vy - 1` plus `Vy - 2` etc., until `Vy = 0`. This allows us to use the formula `(n + 1) * n / 2` from day 7 to calculate the distance from 0 to the maximum height. What to use as `n` to get the maximum height? Well, when the position hits the X axis again at `y = 0`, the value of the `y` velocity is the initial value, but negative. In the next step, the position will have exactly this value. So the best value for `n` is the absolute value of the target's minimum `y`, if we pass that, the position in the step after `y = 0` would be out of bounds.

For the second part I used brute force, calculating all the velocities that make the probe end in the target area. The search window goes from 0 to the target's maximum `x` horizontally, and from the target's minimum `y` to the value of the speed that made it go to the maximum height in part one: the absolute value of the target's minimum `y`.


### Day 18

[Solution](aoc/d18/solution.py)

Day 15 took me long, but day 18 took me 3 days :D

There were a lot of tiny winy things to take into account for all the tests to pass...

Although I saw many people use tree hierarchies to solve this puzzle my approach was to parse it character by character like day 10... would it have taken me less if I had done a tree? Who knows!

Today is day 25 of December (merry Xmas!) and I suspect the next puzzles are going to be worse, so I am leaving it here. I may solve the other puzzles later or next year though!
