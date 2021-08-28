import unittest

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise


"""
    python -m unittest -v
    coverage run .
    coverage report --omit */site-packages/*
    coverage html --omit */site-packages/*
"""

if __name__ == "__main__":
    from endpoints import *
    unittest.main(verbosity=2)
