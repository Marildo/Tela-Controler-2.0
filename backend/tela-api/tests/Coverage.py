import coverage

import unittest

try:
    import sys
    import os

    current_dir = os.path.dirname(__file__)
    source_path = os.path.abspath(os.path.join(current_dir, '../src/'))
    sys.path.append(source_path)
except:
    raise

cov = coverage.Coverage()
cov.start()

from endpoints import *
unittest.main(verbosity=2)

cov.stop()
cov.save()

cov.report()