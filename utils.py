from copy import deepcopy
from functools import wraps

from docopt import docopt

DOC_GLOBAL = {}


def doc(doc_param=None):
    def decorator(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            # Format the arguments for convenient use
            new_kwargs = deepcopy(kwargs)
            for (k, v) in kwargs.items():
                if k.startswith('-'):
                    new_kwargs[k.lstrip('-').replace('-', '_')] = v
            # Proceeds with the function execution
            fn(*args, **new_kwargs)
        DOC_GLOBAL[fn.__name__] = decorated
        # https://stackoverflow.com/questions/10307696/how-to-put-a-variable-into-python-docstring
        if doc_param:
            decorated.__doc__ = decorated.__doc__.format(doc_param)
        return decorated
    return decorator


def doc_lookup(fn_name, argv):
    fn = DOC_GLOBAL.get(fn_name, error_lookup)
    print(DOC_GLOBAL)
    # print(fn)
    # print(fn.__doc__)
    print(argv)
    argv.update({fn_name: True})
    print(argv)
    return fn(**docopt(fn.__doc__, argv=argv))


def error_lookup(**kwargs):
    """
Usage:
    voyager [-h | --help] [-v | --version] <module> [<args>...]

    """
    exit("%r is not a voyager command. \n%s" % (kwargs['<module>'],
                                              error_lookup.__doc__))
