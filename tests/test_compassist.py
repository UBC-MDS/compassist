from compassist.compassist import dry_calc, shiny_hunt

# imports for shiny_hunt tests
import numpy as np

# imports for dry_calc tests
from scipy.stats import binom

# dry_calc unit tests
def test_dry_calc_value():
    """Test dry_calc outputs correct values."""
    n = 5
    p = 0.2
    result = dry_calc(p, n, verbose=False, plot=False)
    expected = 1 - binom.pmf(0, n, p)
    assert round(result, 5) == round(expected, 5), "The probability output is not correct!"

def test_dry_calc_range():
    """Test dry_calc output is in correct range."""
    n = 10
    p = 0.5
    result = dry_calc(p, n, verbose=False, plot=False)
    expected = 1 - binom.pmf(0, n, p)
    assert round(result, 5) == round(expected, 5), "The probability output is not correct!"
    assert 0 <= result <= 1, "The output probability must be between 0 and 1!"

def test_dry_calc_type():
    """Test dry_calc output is the correct data type."""
    n = 15
    p = 0.4
    assert type(dry_calc(p, n, verbose=False, plot=False)) == float, "The output is not a decimal! Something strange has happened."
    assert type(dry_calc(p, n, verbose=True, plot=False)) == str, "The output is not a string! Something strange has happened."

# shiny_hunt unit tests
def test_shiny_hunt_value_wild():
    """Test shiny_hunt outputs correct values for wild encounters"""
    gen = 6
    encounter_rate = 60
    attempt_time = 20
    expected = {'25%': (1179, 6.55), '50%': (2838, 15.77), '75%': (5676, 31.53), '90%': (9429, 52.38), '99%': (18855, 104.75)}
    assert shiny_hunt(gen=gen, encounter_rate=encounter_rate, attempt_time=attempt_time, shiny_charm=True, verbose=False) == expected, "Inncorrect output dictionary"

def test_shiny_hunt_value_value():
    """Test shiny_hunt outputs correct values for egg hatches"""
    gen = 6
    encounter_rate = 60
    attempt_time = 20
    expected = {'25%': 196, '50%': 473, '75%': 946, '90%': 1571, '99%': 3141}
    assert shiny_hunt(gen=gen, encounter_rate=encounter_rate, attempt_time=attempt_time, masuda=True, verbose=False) == expected, "Incorrect output dictionary."

def test_shiny_hunt_type():
    """Test shin_hunt outputs correct data types"""
    test_wild = shiny_hunt(6, attempt_time=15, verbose=False)
    test_wild_key = list(test_wild.keys())[0]
    test_wild_value = list(test_wild.values())[0]
    test_egg = shiny_hunt(6, attempt_time=15, verbose=False, masuda=True)
    test_egg_key = list(test_egg.keys())[0]
    test_egg_value = list(test_egg.values())[0]
    assert type(test_wild_key) == str, "dictionary keys are not strings"
    assert type(test_wild_value) == tuple, "dictionary vakues for wild encounters are not tuples"
    assert type(test_egg_key) == str, "dictionary keys are not strings"
    assert type(test_egg_value) == int, "dictionary values for eggs are not integers"