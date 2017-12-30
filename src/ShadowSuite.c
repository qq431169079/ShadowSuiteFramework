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

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *                                                                                     *
 *                        START OF THE MAIN PROGRAM FUNCTION                           *
 *                                                                                     *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

//Main Function
int main(void)
{
    char justarandomone = 'x';
    int section;

    while (justarandomone == 'x')
    {
    //Clears the screen
    clr();
    //Sets terminal color to green.
    color_green();
    //Prints the logo of Shadow Framework..
    prn_logo();
    printf("\n==TOOLS==\n\n---------------------------------\n\n");
    printf("\n[01] Reconnaissance (Information Gathering)\n[02] Scanning\n[03] Encryption and Password Cracking\n");
    printf("[04] Exploitation\n[05] Denial-of-Service (Stress Testing)\n[06] Session Hijacking\n");
    printf("\n[96] License\n[97] Manual\n[98] Install Dependencies\n[99] Exit\n");
    scanf("\n%d", &section);
    switch (section)
        {
        case 1:
		reconSection();
		break;

	case 2:
		scanSection();
		break;

	case 3:
		crackSection();
		break;

	case 4:
		exploitSection();
		break;

	case 5:
		dosSection();
		break;

	case 6:
		hijackSection();
		break;

	case 96:
		prn_license();
		break;

	case 97:
		prn_help();
		break;

	case 98:
		instdeps();
		break;

	case 99:
		exit_confirm();
		break;

	default:
    		prn_invalidinput();
    		break;
        }
    }
    error101();
    color_white();
    return 1; //Program must not go here!!!
    exit(EXIT_FAILURE);
}
