# shiny_hunt imports
import numpy as np

def shiny_hunt(gen, masuda=False, shiny_charm=False, encounter_rate=100,  attempt_time=15, hatch_time=None, verbose=False):
    """Calculates and prints number of attempts (and expected time) required to find a shiny pokemon

    Parameters
    ----------
    gen : int
        integer denoting generation of pokemon
    masuda : bool, optional
        is the player using masuda method
    shiny_charm : bool, optional
        does the player have a shiny charm
    encounter_rate : int or float
        rate of encounter of the pokemon (only for wild encounters)
    attempt_time : int, optional
        time (in seconds) representing average time taken to encounter a pokemon, or soft reset
    hatch_time : int, optional
        time (in seconds) to hatch a single pokemon egg
    verbose : bool, optional
        Controls format of returned probability. Default (True) prints results as statements, False returns a dict.

    Returns
    -------
    dict
        dictionary containing probabilities as keys and number of attempts/hrs values as tuples
    
    Examples
    --------
    >>> shiny_hunt(gen=7, encounter_rate=25, attempt_time=15, shiny_charm=True, verbose=True)
    There is a 25% chance to get a shiny encounter in 3144 encounters
    This would take an approximate of 13.1 hours.
    ================================
    There is a 50% chance to get a shiny encounter in 7568 encounters
    This would take an approximate of 31.53 hours.
    ================================
    There is a 75% chance to get a shiny encounter in 15136 encounters
    This would take an approximate of 63.07 hours.
    ================================
    There is a 90% chance to get a shiny encounter in 25144 encounters
    This would take an approximate of 104.77 hours.
    ================================
    There is a 99% chance to get a shiny encounter in 50280 encounters
    This would take an approximate of 209.5 hours.
    ================================

    output of shiny_hunt() when verbose is set to true

    >>> shiny_hunt(gen=7, encounter_rate=35, attempt_time=15, shiny_charm=True, verbose=False)
    {'25%': (1965, 8.19), '50%': (4730, 19.71), '75%': (9460, 39.42), '90%': (15715, 65.48), '99%': (31425, 130.94)}

    output of shin_hunt() when verbose is set to false

    """
    
    # make sure all inputs are legal
    if not isinstance(gen, int):
        raise TypeError("Gen must be an integer")
    if gen < 1 or gen > 9:
        raise ValueError("Gen must be in the range [1-9]")
    if not isinstance(encounter_rate, float):
        if not isinstance(encounter_rate, int):
            raise TypeError("Encounter rate must be a number")
    if encounter_rate <= 0 or encounter_rate > 100.0:
        raise ValueError("Encounter rate must be in the range [0-100]")
    if not isinstance(attempt_time, int):
        raise TypeError("Attempt time must be an integer (in seconds)")
    if attempt_time < 0:
        raise ValueError("Attempt time must be positive")
    if not isinstance(shiny_charm, bool):
        raise TypeError("Shiny charm must be a boolean")
    if shiny_charm and gen < 5:
        raise Exception("Shiny charm did not exist prior to gen 5")
    if masuda and gen < 4:
        raise Exception("Masuda method did not exist prior to gen 4")
    
    # base rate of encountering a shiny pokemon before gen 6
    base_rate = 1/8192
    
    # base rate doubles in gen 6 and above
    if gen > 5:
        base_rate *= 2    
    
    prob = base_rate
    
    # probability increases if player has shiny charm equipped
    if shiny_charm:
        prob += 2 * base_rate
        
    # probability increases further when using masuda method
    if masuda:
        prob += 4 * base_rate
        if gen > 4:
            prob += base_rate
    
    expected_values = [0.25, 0.5, 0.75, 0.9, 0.99]
    results = {}

    for value in expected_values:
        # calculate number of attempts
        n = int(np.round(np.log(1 - value) / np.log(1 - prob), 0))
        if masuda:
            if hatch_time:
                results[f'{int(value * 100)}%'] = (n, np.round(n * hatch_time / 3600, 2))
            else:
                results[f'{int(value * 100)}%'] = n
        elif encounter_rate < 100:
            avg_attempts = int(np.round(np.log(1 - 0.9) / np.log(1 - (encounter_rate / 100)), 0))
            results[f'{int(value * 100)}%'] = (n * avg_attempts, np.round(n * avg_attempts * attempt_time / 3600, 2))
        else:
            results[f'{int(value * 100)}%'] = (n, np.round(n * attempt_time / 3600, 2))

    # print the output to console if verbose is set to true
    if verbose:
        for key in results:
            if masuda:
                if hatch_time:
                    print(f'There is a {key} chance to hatch a shiny in {results[key][0]} attempts')
                    print(f'This would take an approximate of {results[key][1]} hours.')
                else:
                    print(f'There is a {key} chance to hatch a shiny in {results[key]} attempts')
            else:
                print(f'There is a {key} chance to get a shiny encounter in {results[key][0]} encounters')
                print(f'This would take an approximate of {results[key][1]} hours.')
            print('================================')

    # return dictionary otherwise
    else:
        return results
    
def boss_completion(probs, run_time=0):
    """Calculates expected wins/finishes required to obtain/complete a specific task

    Parameters
    ----------
    probs : float or array of float
        probabilities of all individual item drops
    run_time : int, optional
        integer denoting time (in seconds) spent on a single catch attempt

    Returns
    -------
    time : int
        average time taken for completion
    wins : int
        expected number of wins required to achieve goal
    """

    # dummy outpu just for testing functions
    print('boss_completion works!!')

# dry_calc imports
import math 
import matplotlib.pyplot as plt

# dry_calc function
def dry_calc(p, n, verbose=True, plot=True):
    """Calculates probability of at least one occurence of an event given the number of attempts.
    
    Parameters
    ----------
    p : float
        Probability of event occurence.
        
    n : int
        The number of attempts.
        
    verbose : bool, Optional
        Controls format of returned probability. Default (True) returns result as a statement, False returns a float.
        
    plot : bool, Optional
        Controls return of plot showing where the resulting probability lies on the binomial distribution. Default is True.
    
    Returns
    -------
    str 
        String containing the probability of at least one occurrence of event given the number of trials as a percentage (default).

    float
        Probability of at least one occurrence of event given the number of trials as a decimal (if verbose set to False).
        
        
    matplotlib.container.BarContainer
        Bar plot showing where the resulting probability lies on the probability distribution.
        
    Examples
    --------
    >>> dry_calc(0.2, 5, verbose=False, plot=False)
    0.6723199999999999
    
    >>> dry_calc(0.2, 5, verbose=True, plot=False)
    'There is a 67.2% chance of the event occurring at least once after you play 5 attempts.'
    """
    # check probability input is a float between 0 and 1
    if not (0 <= p <= 1):
        raise ValueError("Probability, p, should be a decimal between 0 and 1!")
        
    # check n input is a positive integer       
    if not isinstance(n, int) or not (n >= 0):
        raise ValueError("Number of attempts, n, should be an integer greater than or equal to 0!")
    
    # calculate p(0): binomial probability of the event occurring 0 times given n trials and probability p
    x = 0
    n_choose_x = math.factorial(n) / (math.factorial(x) * math.factorial((n - x)))
    p0 = n_choose_x * (p ** x) * ((1 - p) ** (n - x))
    
    # calculate probability of at least 1 occurrence: 1 - p(0)
    p1 = 1 - p0
    p1_percent = p1 * 100
    
    # show plot if requested
    if plot:
        pn = 0
        pp = dry_calc(p, pn, verbose=False, plot=False)
        
        # initiate x and y lists
        px = [pn]
        py = [pp]
    
        while pp <= 0.99:
            pn += 1
            pp = dry_calc(p, pn, verbose=False, plot=False)
            px.append(pn)
            py.append(pp)
    
        plt.bar(px, py)
        plt.plot(n, p1, marker="X", ms=15, mfc="red", label=round(p1, 3))
        plt.xlabel("Number of attempts")
        plt.ylabel("Probability")
        plt.legend()
        plt.show()
    
    # check verbose argument to return correct output
    if verbose:
        result = f"There is a {p1_percent:.1f}% chance of the event occurring at least once after you play 5 attempts."
        return result
    
    else:
        return p1    


def pts_calc(points_attempt, time_attempt):
    """Calculates the time required to achieve certain number of points in the most efficient manner

    Parameters
    ----------
    points_attempt : float or array of float
        number of points obtained per successful attempt
    time_attempt : int
        time (in seconds) per attempt on average
    
    Returns
    -------
    time : int or array of int
        time required for completion (in ranked ascending order for arrays)
    attempts : int
        number of attempts required (in ranked order of time)
    """

    # dummy output just for testing functions
    print('pts_calc works!!')


