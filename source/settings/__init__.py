# Standard Library
import getpass

# Local Django
from source.settings.base import *


if getpass.getuser() in ['root']:
    from source.settings.production import *
else:
    from source.settings.staging import *
