def answer(exercise):
    return ("", exercise[1]) if isinstance(exercise, tuple) else ("", exercise)


def question(exercise):
    return exercise[0]
