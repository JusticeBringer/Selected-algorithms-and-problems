#include <stdio.h>
#include <string.h>

int main()
{
    FILE* fisier = fopen("fisier.txt", "r");

    char c;
    int frev[200] = {0};
    //char delim [10] = {'\0','\n',' ', ' ', '.'};

    while((c = fgetc(fisier)) != EOF)
    {
        if(c != '\0' && c != '\n' && c != ' ' )
          {
              c = tolower(c);
              frev[c - 'a'] = frev[c - 'a'] + 1;  
          }
    }

    int i = 0;
    int max = 0;

    for( i = 0; i < 26; i++)
        if( frev[i] > max)
            max = frev[i];

    //if !=0
    printf("%d ", max);

    fclose(fisier);

    return 0;
}