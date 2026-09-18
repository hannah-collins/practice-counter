from drafter import *
from dataclasses import dataclass

set_website_title("Hannah's Counter")
set_site_information(
    author="Hannah Collins",
    description="Counter with various increment options.",
    sources="",
    planning="",
    links=[""]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    return Page(state, [
        "Current count: " + str(state.count),
        Button("+1", "increment"),
        Button("-1", "decrement"),
        Button("+5", "increment5"),
        Button("+7", "increment7"),
        Button("Reset", "reset_count")
    ])

@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)


@route
def decrement(state: State) -> Page:
    if state.count != 0:
        state.count = state.count - 1
    return index(state)

@route
def increment5(state: State) -> Page:
    state.count = state.count + 5
    return index(state)

@route
def increment7(state: State) -> Page:
    state.count = state.count + 7
    return index(state)

@route
def reset_count(state: State) -> Page:
    state.count = 0
    return index(state)

assert_state(increment(State(0)), State(1))
assert_state(reset_count(State(7)), State(0))
assert_has(index(State(3)), "Current count: 3")

start_server(State(5))
