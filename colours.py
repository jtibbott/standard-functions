class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'
       
# Example usage
print(f"{fg.RED}This is red text{fg.RESET}")
print(f"{bg.YELLOW}{fg.BLUE}This is blue text on a yellow background{bg.RESET}{fg.RESET}")
print(f"{style.BRIGHT}{fg.GREEN}This is bright green text{style.RESET_ALL}")
print(f"{style.DIM}{fg.MAGENTA}This is dim magenta text{style.RESET_ALL}")
print(f"{style.NORMAL}{bg.CYAN}{fg.BLACK}This is normal black text on a cyan background{style.RESET_ALL}{bg.RESET}{fg.RESET}")