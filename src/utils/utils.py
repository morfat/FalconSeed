
from datetime import datetime
import jsonschema
import falcon

import time

def current_date_time():
	return str(datetime.now())

def unix_timestamp():
    t=time.time()
    return str(t).split('.')[0]


def validate_jsonschema(schema,data):
    try:
        jsonschema.validate(data, schema, format_checker=jsonschema.FormatChecker())
        return data
    except jsonschema.ValidationError as e:
        raise falcon.HTTPBadRequest('Data validation failed',description=e.message)
