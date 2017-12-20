/*
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/.
 */

/* This header file contains functions that can be used in any
 * console programs. This header file is meantly built for Linux.
 * If you want to use this header file on windows, please get a
 * copy of 'CatayaoLibWin.h' on Catayao56's GitHub repository. */

//Include preprocessor directives
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Function declarations
void clr(void); //Clears the screen.
void readline(void); //Wait for user input.
void prn_invalidinput(void); //Prints the invalid input message.
void exit_confirm(void); //Asks for exit confirmation.
void prn_construction(void); //Prints the under construction message.

void clr(void)  //Clear function
{
    system("clear"); //Actual command that clears the screen
}

void readline(void)
{
    system("read temporary"); //Command lets user input any word, even
                              //a line break.
}

void prn_invalidinput(void)
{
    clr();
    printf("ERROR: Invalid Input\n");
    readline();
}

void exit_confirm(void)
{
    char confirm;
    int error_value = 1;

    while (error_value == 1)
    {
    clr();
    printf("Do you really want to quit?\nAnswer (y/n) : \n");
    scanf(" %c", &confirm);
    if (confirm == 'y' || confirm == 'Y')
    {
        clr();
        error_value = 0;
        printf("Exiting...\n");
        exit(EXIT_SUCCESS);
    }
    if (confirm == 'n' || confirm == 'N')
    {
        error_value = 0;
        clr();
    }
    else
    {
            error_value = 1;
        prn_invalidinput();
    }
    }
}

void prn_construction(void)
{
    clr();
    printf("ERROR: Under Construction!");
    readline();
}
