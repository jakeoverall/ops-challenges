class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_fail(message):
    print(colors.FAIL)
    print(message)
    print(colors.ENDC)

def print_header(message):
    print(colors.HEADER)
    print(message)
    print(colors.ENDC)

def print_success(message):
    print(colors.GREEN)
    print(message)
    print(colors.ENDC)

def print_info(message):
    print(colors.BLUE)
    print(message)
    print(colors.ENDC)

def print_warning(message):
    print(colors.WARNING)
    print(message)
    print(colors.ENDC)

def print_bold(message):
    print(colors.BOLD)
    print(message)
    print(colors.ENDC)

def print_underline(message):
    print(colors.BOLD)
    print(message)
    print(colors.ENDC)