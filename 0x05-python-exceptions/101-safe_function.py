#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        r = fct(*args)
    except Exception as e:
        print("Exception: {:s}".format(str(e)), file=stderr)
        return None
    else:
        return (r)
