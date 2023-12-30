import pkgutil

def __init__():
    # stackoverflow be like
    for l, m, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(m)
        _module = loader.find_module(m).load_module(m)
        globals()[m] = _module
