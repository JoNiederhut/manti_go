# manti_go

The best game of 2022.

![Python application](https://github.com/JoNiederhut/manti_go/workflows/Tests_for_mantigo/badge.svg)

## About

This is the project result from our cohort "naive bayleaves" of the "software engineering" week during the data science bootcamp at [Spiced Academy](https://www.spiced-academy.com/de/program/data-science) in Berlin from July to October 2022.

<img alt="manti_go GUI" src="https://github.com/JoNiederhut/manti_go/blob/main/docs/game.png" width="800">

## Goal

The aim was to develop a game using software engineering methods.

## How to setup (Linux/Mac)

Clone the repo:

`git clone https://github.com/JoNiederhut/manti_go.git`

Go inside:

`cd manti_go`

Requirements:

`pip install -r requirements.txt`

Setup:

`pip install —editable .`

Then resize the terminal window as big as you can.

Run:

`python mantigo/main.py`

Enjoy the game.

## How to play

**Be delicious**

The goal of the game is to collect as many [manti](https://en.wikipedia.org/wiki/Manti_(food)) as you can at the which represent your number of lifes. All this takes place at the inspiring [Kotti](https://de.wikipedia.org/wiki/Kottbusser_Tor). Use your arrow keys to move the player.

**Be careful**

But be careful, there are enemies that can hit you and steal your manti.

**Be quick**

The *manti timer* is running limiting your time to have fun! But don't worry, you can always re-start the game :)

## Technical background

The game is based on [pygame](https://www.pygame.org/).

The game was developed following these steps:

1. Plan

- Backlog: prioritize features

2. Code

- Create a prototype
- Create a class diagram
- Use logging
- Use pair program

3. Quality checks

- Make code review together
- Make tests using Pytest
- Continuous Integration (CI)

4. Maintain

- Use version control Git
- setup.py
- Analyze code statically with pylint
- Refactoring

## Outlook

See issues.
