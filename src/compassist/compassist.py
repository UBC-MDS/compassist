def shiny_hunt(pokemon, game, gen, attempt_time=0):
    """Calculates optimal time, best method and location for shiny hunting any pokemon

    Parameters
    ----------
    pokemon : str
        name of pokemon_
    game : str
        initials of the name of the game
    gen : int
        integer denoting generation of pokemon
    attempt_time : int, optional
        integer denoting time (in seconds) spent on a single catch attempt

    Returns
    -------
    time : int
        average time taken to encounter a single shiny
    location : str
        best location to encounter shiny
    method : str
        best method to catch shiny
    attempt : int
        average number of attempt before encounter
    """

    # dummmy output just for testing functions
    print('shiny_hunt works!!')

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
        Probability of event occurence; a decimal between 0 and 1.
        
    n : int
        The number of attempts; a whole number greater than or equal to 0.
        
    verbose : bool, Optional
        Controls format of returned probability;
        Default (True) returns result printed in a statement; 
        False returns numerical probability as a float.
        
    plot : bool, Optional
        Controls printing of plot showing where the resulting probability lies on the binomial distribution; 
        Default is True.
    
    Returns
    -------
    str 
        String statement containing the probability of at least one occurrence of event given the number of trials as a percentage (default).

    float
        Probability of at least one occurrence of event given the number of trials as a decimal (if verbose set to False).
        
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
        result = f"There is a {p1_percent:.1f}% chance of the event occurring at least once after you play {n} attempts."
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


