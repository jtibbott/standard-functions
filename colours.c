#include <stdio.h>

// Foreground color codes
#define FG_BLACK   "\033[30m"
#define FG_RED     "\033[31m"
#define FG_GREEN   "\033[32m"
#define FG_YELLOW  "\033[33m"
#define FG_BLUE    "\033[34m"
#define FG_MAGENTA "\033[35m"
#define FG_CYAN    "\033[36m"
#define FG_WHITE   "\033[37m"
#define FG_RESET   "\033[39m"

// Background color codes
#define BG_BLACK   "\033[40m"
#define BG_RED     "\033[41m"
#define BG_GREEN   "\033[42m"
#define BG_YELLOW  "\033[43m"
#define BG_BLUE    "\033[44m"
#define BG_MAGENTA "\033[45m"
#define BG_CYAN    "\033[46m"
#define BG_WHITE   "\033[47m"
#define BG_RESET   "\033[49m"

// Style codes
#define STYLE_BRIGHT    "\033[1m"
#define STYLE_DIM       "\033[2m"
#define STYLE_NORMAL    "\033[22m"
#define STYLE_RESET_ALL "\033[0m"

int main() {
    // Example usage
    printf("%sThis is red text%s\n", FG_RED, FG_RESET);
    printf("%s%sThis is blue text on a yellow background%s%s\n", BG_YELLOW, FG_BLUE, BG_RESET, FG_RESET);
    printf("%s%sThis is bright green text%s\n", STYLE_BRIGHT, FG_GREEN, STYLE_RESET_ALL);
    printf("%s%sThis is dim magenta text%s\n", STYLE_DIM, FG_MAGENTA, STYLE_RESET_ALL);
    printf("%s%s%sThis is normal black text on a cyan background%s%s%s\n", STYLE_NORMAL, BG_CYAN, FG_BLACK, STYLE_RESET_ALL, BG_RESET, FG_RESET);

    getchar();

    return 0;
}
