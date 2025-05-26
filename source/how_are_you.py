class WrongSeasonException(Exception):
    pass


def how_are_you(season):
    if season == 'Summer':
        print('What a wonderful day!')
    else:
        raise WrongSeasonException
