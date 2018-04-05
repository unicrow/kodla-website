# Standard Library
import getpass

# Local Django
from kodla.settings.base import *


if getpass.getuser() in ['root']:
    from kodla.settings.production import *
else:
    from kodla.settings.staging import *
