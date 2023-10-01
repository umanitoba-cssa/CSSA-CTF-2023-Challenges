#include <stdio.h>
#include <string.h>
#include <stdlib.h>  

void fail() {
    printf("false\n");
    exit(0);
}

int main(int argc, char *argv[]) {
    if (strlen(argv[1]) != 26) {
        fail();
    }

    for(int i = 0; i < 26; i++) {
        if (argv[1][i] < 'A' || argv[1][i] > 'Z') {
            fail();
        }
    }

    char* space = malloc(26 * sizeof(char));
    char* res = malloc((26 * 3 + 1) * sizeof(char));

    for(int i = 0; i < 26; i++) {
        char c = argv[1][i];
        space[c - 'A'] = i;
    }

    for(int i = 0; i < 26; i++) {
        sprintf(res + i * 3, "%02d/", space[i]);
    }
    
    if (strcmp(res, "18/24/06/00/17/22/08/15/21/09/04/12/14/23/02/10/03/13/19/16/05/20/11/01/25/07/") != 0) {
        fail();
    }

    printf("true\n");

    return 0;
}