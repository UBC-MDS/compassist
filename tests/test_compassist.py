from compassist.compassist import dry_calc

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