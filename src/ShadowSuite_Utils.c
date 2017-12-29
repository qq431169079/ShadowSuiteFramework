/* Shadow Suite :: Ethical Hacking Toolkit
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
 
#include "ShadowLib.h"

void error101(void)
{
clr();
color_red();
printf("OH NO! THIS PROGRAM MUST NOT GO HERE!\n\n");
printf("This might be a bug, so please contact Shadow Team.\n");
printf("Tell us what you had done and send it to any of the following:\n\n");
printf("Public.ShadowTeam@gmail.com\nCatayao56@gmail.com\nCristineAnn.DG.Santos@gmail.com\n");
printf("\nPress any key to exit...\n");
readline();
}

void clr(void)  //Clear and set color function
{
    color_green(); //Sets terminal color to green.
    system("clear"); //Actual command that clears the screen
}

void readline(void)
{
    system("read dummy"); //Command lets user input any word, even
                         //a line break.
}

void prn_invalidinput(void)
{
    clr();
    prn_logo();
    color_red();                        //Sets the terminal color to red...
    printf("\nERROR: Invalid Input\n"); //...Then prints this message...
    color_green();                      //...And lastly, sets the terminal color
    readline();                         //back to green.
}

void exit_confirm(void)
{
    char confirm;
    int error_value = 1;

    //If user enters a character except for y, Y, n, and N, the variable 'error_value'
    //will still have the value '1', which causes the loop to start again from the top.
    while (error_value == 1)
    {
    clr();
    prn_logo();
    color_yellow();
    printf("\nDo you really want to quit?\nAnswer (y/n) : \n");
    scanf(" %c", &confirm);
    if (confirm == 'y' || confirm == 'Y')
    {
        clr();
        error_value = 0; //Assigns variable 'error_value' to have the value 0, to get
	color_red();                                               //out of the loop.
        printf("\nExiting...\n");
	color_white(); //Sets the terminal color back to normal.
        exit(EXIT_SUCCESS);
    }
    if (confirm == 'n' || confirm == 'N')
    {
        error_value = 0; //Assigns variable 'error_value' to have the value 0, to get
        clr();                                                     //out of the loop.
    }
    else
    {
        error_value = 1; //If none of the conditions above met, then the program will
        prn_invalidinput();                //call the 'prn_invalidinput();' function.
    }
    }
}

void prn_construction(void)
{
    prn_logo();
    color_yellow();                           //Sets the terminal color to yellow...
    printf("\nERROR: Under Construction!\n"); //...Then prints this message.
}

void color_white(void)
{
    system("echo -e \033[0m"); //Sets terminal color to white.
}

void color_red(void)
{
    system("echo -e \033[31m"); //Sets terminal color to red.
}

void color_green(void)
{
    system("echo -e \033[32m"); //Sets terminal color to green.
}

void color_yellow(void)
{
    system("echo -e \033[33m"); //Sets terminal color to yellow.
}

void color_bold(void)
{
    system("echo -e \033[1m"); //Sets terminal font to bold.
}

void color_italic(void)
{
    system("echo -e \033[3m"); //Sets terminal font to italic.
}
