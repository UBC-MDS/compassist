# `compassist`

## Completionist Assistant

#### Authors/ Main Contributors: Samson Bakos, Marian Agyby, Waiel Tinwala, Ashwin Babu

A set of tools to help compute task time/ probabilities for video game completionist tasks.

"Completionism" is a common goal in video games, referring to the goal of achieving every objective in a game (or individual extraneous side-objectives), as opposed to merely doing enough to win. Common examples include hunting for Shiny Pokemon, the Runescape Collection Log, World of Warcraft Achievement Log, among many others. Completionism is generally an exercise in dedication, time-commitment, and efficiency. As an example of the time scales involved, hunting a single shiny Pokemon can takes hundreds of hours, completing individual Runescape bosses can take from less than ten to many thousands of hours, and the impossible task of completing the entire collection log is estimated to be more than 500 years of play time. Small optimizations have the potential to save large amounts of time and effort, and as such completionist players are often very efficiency-oriented by necessity.

This package provides tools to help completionist players focus and analyze their goals. These tools compute and visualize expected attempts, play times, and probabilities to help players understand their goals and compare the efficiency of different methods. Current tools are developed with a focus on goals in the games Oldschool Runescape and Pokemon, but the use cases are easily generalized to other applications.

The following functions are currently available:

-   `shiny_hunt()`: Designed for hunting Shiny Pokemon. Computes the time to find a specific Shiny Pokemon based on the occurrence rate of that Pokemon in a specific region, and Pokemon generation/game.

-   `boss_completion():` A weighted permutation probability calculator that computes the expected attempts to complete a task as a function of the probabilities of all desired outcomes (i.e. expected boss kills to get all items based on all item drop rates). Includes optional arguments to also show probability of overall completion/ completing each task for a given number of attempts.

-   `dry_calc()`: Computes the probability of obtaining at least one of a specific outcome in a given number of trials based on binomial probability (i.e. probability of obtaining an item from a boss in a given number of kills). Displays a plot showing probability of obtaining a drop over a range of trial counts, indicating location of provided trials on this curve.

-   `pts_calc()`: Computes the expected attempts/ play time to cross a certain point threshold (i.e. price of an item, expected number of points per item drop) as a function of a player's points per attempt and time per attempt. When passed multiple sets of points/ times, it ranks and plots them to allow for comparison of methods.

There are some tools that perform similar functions to functions in `compassist`. For example, the `giovanni` package <https://github.com/tgsmith61591/giovanni> provides similar applications for hunting Shiny Pokemon. Users with sufficient understanding can also use mainstream statistical tools (i.e. `scipy` <https://github.com/scipy/scipy>) to replicate the basic functionalities of functions like `dry_calc`. The unique application of this package is to provide a centralized location for multiple different tools, to simplify calculation for users with less statistical understanding and tailor outputs to specific video game applications, as well as to provide additional helpful functionalities such as visualizations and rankings.

## Installation

``` bash
$ pip install compassist
```

## Usage

-   TODO

## Contributing

If you are interested in contributing to `compassist`, read the [contributing guidelines](https://github.com/UBC-MDS/compassist/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/compassist/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`compassist` was created by Samson Bakos, Waiel Tinwala, Marian Agyby and Ashwin Babu. It is licensed under the terms of the MIT license.

## Credits

`compassist` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
