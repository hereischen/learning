#include <stdio.h>
#define MAXLINE 1000

int mygetline(char line[], int maxline);
void copy(char to[], char from[]);

int main()
{
    int len;
    int max;
    char line[MAXLINE];
    char longest[MAXLINE];

    max = 0;
    while ((len = mygetline(line, MAXLINE)) >0 )
        if (len > max) {
            max = len;
            printf("line > %s",line);
            copy(longest,line);
            printf("longest > %s", longest);
        }
    if (max > 0)
        printf("%s", longest);
    return 0;
}

int mygetline(char line[], int maxline)
{
    int c,i;

    for (i=0; i < maxline-1 && (c=getchar())!=EOF && c!='\n'; ++i)
        line[i] = c;
    if ( c =='\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

void copy(char to[], char from[])
{
    int i;

    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}
