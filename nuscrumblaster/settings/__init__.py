# This is a simple settings file that just imports local.py,
# which should be a symlink to an actual settings file.

try:
    from local import *
except ImportError:
    import sys
    print 'Error importing settings/local.py. Did you forget to symlink your local settings?'
    raise
    sys.exit(1)
