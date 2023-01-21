from compassist.compassist import *

# imports for shiny_hunt tests
import numpy as np

# dry_calc unit tests
def test_dry_calc_value():
    """Test dry_calc outputs correct values."""
    n = 5
    p = 0.2
    result = dry_calc(p, n, verbose=False, plot=False)
    expected = 1 - 0.32768  # binom result
    assert round(result, 5) == round(
        expected, 5
    ), "The probability output is not correct!"


def test_dry_calc_range():
    """Test dry_calc output is in correct range."""
    n = 10
    p = 0.5
    result = dry_calc(p, n, verbose=False, plot=False)
    expected = 1 - 0.0009765625  # binom result
    assert round(result, 5) == round(
        expected, 5
    ), "The probability output is not correct!"
    assert 0 <= result <= 1, "The output probability must be between 0 and 1!"


def test_dry_calc_type():
    """Test dry_calc output is the correct data type."""
    n = 15
    p = 0.4
    assert (
        type(dry_calc(p, n, verbose=False, plot=False)) == float
    ), "The output is not a decimal! Something strange has happened."
    assert (
        type(dry_calc(p, n, verbose=True, plot=False)) == str
    ), "The output is not a string! Something strange has happened."


# shiny_hunt unit tests
def test_shiny_hunt_value_wild():
    """Test shiny_hunt outputs correct values for wild encounters"""
    gen = 6
    encounter_rate = 60
    attempt_time = 20
    expected = {
        "25%": (1179, 6.55),
        "50%": (2838, 15.77),
        "75%": (5676, 31.53),
        "90%": (9429, 52.38),
        "99%": (18855, 104.75),
    }
    assert (
        shiny_hunt(
            gen=gen,
            encounter_rate=encounter_rate,
            attempt_time=attempt_time,
            shiny_charm=True,
            verbose=False,
        )
        == expected
    ), "Inncorrect output dictionary"


def test_shiny_hunt_value_value():
    """Test shiny_hunt outputs correct values for egg hatches"""
    gen = 6
    encounter_rate = 60
    attempt_time = 20
    expected = {"25%": 196, "50%": 473, "75%": 946, "90%": 1571, "99%": 3141}
    assert (
        shiny_hunt(
            gen=gen,
            encounter_rate=encounter_rate,
            attempt_time=attempt_time,
            masuda=True,
            verbose=False,
        )
        == expected
    ), "Incorrect output dictionary."


def test_shiny_hunt_type():
    """Test shin_hunt outputs correct data types"""
    test_wild = shiny_hunt(6, attempt_time=15, verbose=False)
    test_wild_key = list(test_wild.keys())[0]
    test_wild_value = list(test_wild.values())[0]
    test_egg = shiny_hunt(6, attempt_time=15, verbose=False, masuda=True)
    test_egg_key = list(test_egg.keys())[0]
    test_egg_value = list(test_egg.values())[0]
    assert type(test_wild_key) == str, "dictionary keys are not strings"
    assert (
        type(test_wild_value) == tuple
    ), "dictionary vakues for wild encounters are not tuples"
    assert type(test_egg_key) == str, "dictionary keys are not strings"
    assert type(test_egg_value) == int, "dictionary values for eggs are not integers"


# boss completion unit tests


def test_boss_completion():

    # Baseline expected behavior. This case is the original case that inspired the function as a general solution. Expected completion at 673 attempts (63.24%)
    # first value should always be 1.0 for a successful convergence
    assert boss_completion(
        rates=[7 / 24, 7 / 24, 3 / 24, 2 / 24, 2 / 24, 2 / 24, 1 / 24],
        base_rate=1 / 20,
        attempts=673,
        verbose=False,
    ) == (1.0, 673, 63.24)

    # Test if the above still returns correct results when not also asked to return a probability
    assert boss_completion(
        rates=[7 / 24, 7 / 24, 3 / 24, 2 / 24, 2 / 24, 2 / 24, 1 / 24],
        base_rate=1 / 20,
        verbose=False,
    ) == (1.0, 673)

    # Expected behavior for no base rate (this is number of drops required in initial problem, not number of attempts)
    assert boss_completion(
        rates=[7 / 24, 7 / 24, 3 / 24, 2 / 24, 2 / 24, 2 / 24, 1 / 24], verbose=False
    ) == (1.0, 33)

    # Test case where rates do not converge for a base rate case
    assert boss_completion(rates=[1, 1, 1], base_rate=1 / 2) == None

    # Test 0 probability for less attempts than items desired
    assert (
        boss_completion(
            rates=[1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5], attempts=3, verbose=False
        )[2]
        == 0
    )

    # Test for a rate > 1
    assert (
        boss_completion(
            rates=[2, 1 / 5, 1 / 5, 1 / 5, 1 / 5], attempts=3, verbose=False
        )
        == None
    )

    # Test for a rate < 0
    assert (
        boss_completion(
            rates=[-1 / 5, 1 / 5, 1 / 5, 1 / 5, 1 / 5], attempts=3, verbose=False
        )
        == None
    )
