#include <pcre.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv) {

    const char pattern[] = "^(GET|POST)$";
    const char* error;
    int erroroffset;
    
    pcre* re = pcre_compile(pattern, 0, &error, &erroroffset, NULL);
    if (re == NULL) {
        printf("Can`t compile RE, error: %s, offset: %d", error, erroroffset);
        return EXIT_FAILURE;
    }
    
    pcre_free(re);
    return EXIT_SUCCESS;
}
