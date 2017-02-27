# Standard Library
import getpass

# Local Django
from source.settings.base import *


if getpass.getuser() in ['root']:
    from source.settings.prod import *
elif getpass.getuser() in ['vagrant', 'ubuntu', 'kodla', 'kenan']:
    from source.settings.staging import *
else:
    from source.settings.dev import *
