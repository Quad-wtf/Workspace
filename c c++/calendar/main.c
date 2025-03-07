#include <stdio.h>

#define TRUE 1
#define FALSE 0

int days_in_month[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
char *months[]=
{
    " ",
    "\n\n\nJanuary",
    "\n\n\nFebruary",
    "\n\n\nMarch",
    "\n\n\nApril",
    "\n\n\nMay",
    "\n\n\nJune",
    "\n\n\nJuly",
    "\n\n\nAugust",
    "\n\n\nSeptember",
    "\n\n\nOctober",
    "\n\n\nNovember",
    "\n\n\nDecember"
};
int inputYear(void)
{
    int year;
    printf("Enter the year: ");
    scanf("%d",&year);
    return year;
}

int determineLeapYear(int year)
{
    if(year% 4 == FALSE && year %100 != FALSE || year %400 == FALSE)
    {
        days_in_month[2] = 29;
        return TRUE;
    }
    else
    {
        days_in_month[2] = 2;
        return FALSE;
    }
}

void calendar (int year, int daycode)
{
    int month, day;
    for(month = 1; month <= 12; month++)
    {
        printf("%s",months[month]);
        printf("\n\n Sun Mon Tue Wed Thu Fri Sat\n");

        // correct the position for the first date
        for(day = 1 ; day <= 1 + daycode * 5;day++)
        {
            printf(" ");
        };
        // print all the dates for once month
        for(day = 1; day <= days_in_month[month]; day++)
        {
            printf("%2d", day);
            // is day before dat? else start next line sun.
            if((day + daycode) % 7 > 0)
            printf("  ");
            else
            printf("\n ");
        }
        //set position for next month
        daycode = (daycode + days_in_month[month] ) %7;
    }
}
int main(void)
{
    int year, daycode, leapyear;
    year = inputYear();
    daycode = determineLeapYear(year);
    determineLeapYear(year);
    calendar(year, daycode);
    printf("\n");

}
