/* Shadow Framework :: Ethical Hacking Toolkit Framework
 * Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

//Include preprocessor directives
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Define preprocessor directives

//Function declarations
void clr(void); //Clears the screen.
void readline(void); //Wait for user input.
void prn_invalidinput(void); //Prints the invalid input message.
void exit_confirm(void); //Asks for exit confirmation.
void prn_construction(void); //Prints the under construction message.
void prn_logo(void); //Prints our logo.

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
    printf("\nERROR: Invalid Input\n");
    readline();
}

void exit_confirm(void)
{
    char confirm;
    int error_value = 1;

    while (error_value == 1)
    {
    clr();
    printf("\nDo you really want to quit?\nAnswer (y/n) : \n");
    scanf(" %c", &confirm);
    if (confirm == 'y' || confirm == 'Y')
    {
        clr();
        error_value = 0;
        printf("\nExiting...\n");
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
    printf("\nERROR: Under Construction!\n");
    readline();
}

//prn_logo(); Function
void prn_logo(void)
{
        //In the future, it needs to be standalone!
        //which means it doesn't need any third-party tools!
    system("figlet -f shadow Shadow Framework");
}

//Main Function
int main(void)
{
    char command[100];

    clr();
    //Prints the logo of Shadow Framework..
    prn_logo();
    printf("\nEthical Hacking Toolkit Framework\n\n\n");
    printf("$: ");
    scanf("%s", &command);
    //Command query; If variable 'command' matcher one of here,
    //then the statement is executed.
    if (command == "help")
    {
        printf("help called.");
    }

    else if (command == "settings")
    {
        printf("settings called.");
    }

    else if (command == "exit")
    {
        exit_confirm();
    }

    else
    {
        prn_invalidinput();
    }
    main();
}
