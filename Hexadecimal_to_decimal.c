#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    char s[17];
    printf(" Numarul Hexa este: ");
    scanf("%s ", s);

    int i = 0;
    int suma = 0;

    for( i = strlen(s) - 1; i >= 0; i--)
        {
            if(s[i] >= '0' && s[i] <= '9')
                suma = suma + (s[i] - '0');
            else
                {
                    s[i] = tolower(s[i]);
                    
                    if( s[i] == 'a')
                        suma += 10;
                    else
                        if( s[i] == 'b')
                            suma += 11;
                        else
                            if( s[i] == 'c')
                                suma += 12;
                            else
                                if( s[i] == 'd')
                                    suma += 13;
                                else
                                    if( s[i] == 'e')
                                        suma += 14;
                                    else
                                        if( s[i] == 'f')
                                            suma += 15;
                }
        }

        printf(" \n Suma este: %d ", suma);
    return 0;
}