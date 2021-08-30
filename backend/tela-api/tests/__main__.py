import unittest

try:
    import sys
    import os

    current_dir = os.path.dirname(__file__)
    source_path = os.path.abspath(os.path.join(current_dir, '../src/'))
    print(source_path)

    sys.path.append(source_path)
except:
    raise

"""
    python -m unittest -v
    coverage run .
    coverage report --omit -i */site-packages/*
    coverage html --omit -i */site-packages/*
"""

if __name__ == "__main__":
    unittest.main(verbosity=2)
