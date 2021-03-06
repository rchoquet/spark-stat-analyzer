import os
from datetime import datetime
from analyzers import token_stat, users_sql, error_stats, requests_calls,  coverage_stop_areas
from itertools import chain, islice


def analyzer_value(value):
    analyzers = {
        "token_stats": token_stat.AnalyzeToken,
        "users": users_sql.AnalyseUsersSql,
        "requests_calls": requests_calls.AnalyzeRequest,
        "error_stats": error_stats.AnalyzeErrors,
        "coverage_stop_areas": coverage_stop_areas.AnalyzeCoverageStopAreas
    }
    lower_value = value.lower()
    if lower_value not in analyzers:
        error = "The {} argument must be in list {}, you gave {}".\
            format(value, str(analyzers.keys()), value)
        raise ValueError(error)
    return analyzers[lower_value]


def check_and_get_path(path):
    if not os.path.exists(path):
        raise NotImplementedError('Path not exist, you give {path}'.format(path=path))
    return path


def date_format(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError as e:
        raise ValueError("Unable to parse date, {}".format(e))


def sub_iterable(iterable, size, format=tuple):
    it = iter(iterable)
    while True:
        yield format(chain((next(it),), islice(it, size - 1)))
