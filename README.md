# Simulate the "Iterated Prisoner's Dilemma" with Python

This repository hosts a simple Python framework to simulate the iterated version of the Prisoner's Dilemma. The Prisoner's Dilemma is a classic game theory scenario where two players must decide whether to cooperate or betray each other. The framework allows you to test different strategies and analyze the outcomes of the game.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Running/Testing](#runningtesting)
    - [Implementing new strategies](#implementing-new-strategies)

## Installation
> Tested with Python 3.11.6

To get the environment ready, create a new virtual environment first. For example:
```shell
python3.11 -m venv .venv
```

Activate the environment in the shell:
```shell
source .venv/bin/activate
```

Then, run the following command to install required dependencies:
```shell
pip install -r requirements.txt
```

## Usage

### Running/Testing
1. Go to `main.py`
2. Select two strategies
3. Initialize game with first moves (e.g. "C", "C") or leave it blank to get random first moves for both players
4. Select number of games to be played (`rounds`), whether a plot of the resulting average payoffs should be displayed (and saved) or not (e.g. `game.end_game(plot_results=True, average_lines=False, save_fig=True, fig_name=None, fig_dpi=300)`)

### Implementing new strategies
Write a new class and inherit from `strategies.Strategy` to get strated.
