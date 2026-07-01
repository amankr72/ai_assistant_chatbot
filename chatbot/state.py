current_state = None


def set_state(state):
    global current_state
    current_state = state


def get_state():
    return current_state


def clear_state():
    global current_state
    current_state = None