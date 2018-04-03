#include <pcre.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char** argv) {
    
    printf("PCRE Version: %s\n", pcre_version());

    const char* pattern = "^.*(GET|POST).*$";
    const char* error;
    int erroroffset;

    pcre* re = pcre_compile(pattern, 0, &error, &erroroffset, NULL);
    if (re == NULL) {
        printf("Can`t compile RE, error: %s, offset: %d\n", error, erroroffset);
        return EXIT_FAILURE;
    }
    printf("RE compiled\n");


    int res;

    const char* sample_not_found = "PUT http://example.org/index.html";
    res = pcre_exec(re, NULL, sample_not_found, strlen(sample_not_found), 0, 0, NULL, 0);
    if (res != PCRE_ERROR_NOMATCH) {
        printf("Failed check not match string, res: %d\n", res);
        pcre_free(re);
        return EXIT_FAILURE;
    }
    printf("Test not match string OK\n");


    int mvec[32] = {0};
    const char* sample_found = "123POST http://example.org/index.html";
    res = pcre_exec(re, NULL, sample_found, strlen(sample_found), 0, 0, mvec, sizeof(mvec)/sizeof(mvec[0]));
    if (res <= 0) {
        printf("Failed check match string, res: %d\n", res);
        pcre_free(re);
        return EXIT_FAILURE;
    }
    printf("Test match string OK\n");
    printf("Match offset: %d, mvec[0]: %d, mvec[1]: %d, mvec[2]: %d, mvec[3]: %d\n", res, mvec[0], mvec[1], mvec[2], mvec[3]);

    pcre_free(re);
    return EXIT_SUCCESS;
}
