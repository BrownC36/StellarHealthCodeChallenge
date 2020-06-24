from dateutil.parser import parse
import logging as Logger

def is_date(input, fuzzy=False) :
    try:
        parse(input, fuzzy=fuzzy)
        return True
    
    except ValueError:
        return False


def remove_date_info(date):
    try:
        year = date[:4]
        new_date = "X/X/" + year
        return new_date
    
    except ValueError:
        Logger.error('Unable to parse date')