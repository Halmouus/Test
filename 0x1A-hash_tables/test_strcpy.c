#include <stdio.h>
#include <string.h>

int main() {
    char word1[] = "allawakba";
    char word2[] = "zonda";
    strcpy(word1, word2);
    printf("%s", word1);
    return (0);
}