from homework7.model import run_action
from homework7.view import select_action


def run_prog():
    action = select_action()
    run_action(action)
