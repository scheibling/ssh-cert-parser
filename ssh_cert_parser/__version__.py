"""Module information."""
import os

# The title and description of the package
__title__ = 'ssh-cert-parser'
__description__ = 'A python module for parsing OpenSSH certificates'

# The version and build number
# Without specifying a unique number, you cannot overwrite packages in the PyPi repo
__version__ = f"0.1-{os.getenv('GITHUB_RUN_ID', 'dev')}"

# Author and license information
__author__ = 'Lars Scheibling'
__author_email__ = 'lars@scheibling.se'
__license__ = 'GnuPG 3.0'

# URL to the project
__url__ = f"https://github.com/scheibling/{__title__}"
