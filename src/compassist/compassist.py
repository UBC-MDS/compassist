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

def dry_calc(prob, avg_time=0):
    """Calculates probability of at least one occurence of an event given number of attempts

    Parameters
    ----------
    prob : float
        probability of occurence
    avg_time : int
        time (in seconds) per attempt on average
    
    Returns
    -------
    time : int
        average time taken for occurence
    attempts : int
        expected number of attempts required
    """

    # dummy output just for testing functions
    print('dry_calc works!!')

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


