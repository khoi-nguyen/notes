from pkgutil import iter_modules


def answer(exercise):
    return ("", exercise[1]) if isinstance(exercise, tuple) else ("", exercise)


def question(exercise):
    return exercise[0]


def context_from_pkg(package):
    context = {}
    for module_name in [name for _, name, _ in iter_modules([package])]:
        if module_name not in ["exercise", "helpers", "server"]:
            module_import = __import__(f"{package}.{module_name}")
            module = getattr(module_import, module_name)
            context.update(
                {
                    f: getattr(module, f)
                    for f in dir(module)
                    if not f.startswith("_") and f not in ["context"]
                }
            )
    return context
