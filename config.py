import os

# Configure colors for printing messages
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Configure YakPro packages path (use full path and ensure it's correct)
# Use a string instead of a list for YAKPRO, just pointing to the executable path
YAKPRO = os.path.expanduser("/home/mnestorov/PythonProjects/php-obfuscator/yakpro-po/yakpro-po.php")

# Log filename
log_filename = 'app.log'
