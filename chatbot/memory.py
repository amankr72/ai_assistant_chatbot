params = {
    "area": None,
    "price": None,
    "stars": None,
    "name": None
}


def update_params(entities):

    for key, value in entities.items():

        if key in params:
            params[key] = value

    return params


def clear_params():

    for key in params:
        params[key] = None

def missing_params():

    missing = []

    for key, value in params.items():

        if value is None:
            missing.append(key)

    return missing   

