__author__ = 'Gregor von Laszewski'

import iso8601

def isodate(self, datestr):
    """Parse time from ISO 8601 format"""
    try:
        return iso8601.parse_date(datestr)
    except iso8601.ParseError as e:
        raise ValueError(e.message)
    except TypeError as e:
        raise ValueError(e.message)
