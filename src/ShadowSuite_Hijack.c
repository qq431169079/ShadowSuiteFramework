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

void a_rat(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/hijacking/a-rat && python2 A-Rat.py");
    system("cd ../../..");
}

void hijackhelp(void)
{
    clr();
    color_green();
    prn_logo();
    printf("\n==SESSION HIJACKING TOOLS INFO==\n\n---------------------------------\n\n");
    printf("A-Rat: Remote Administration Tool; Bassed Reverse Shell\n\n");
    printf("\nPress enter to continue...\n\n");
    readline();
}

void hijackSection(void)
{
    int hijackSectionInput;

    clr();
    color_green();
    prn_logo();
    printf("\n==SESSION HIJACKING TOOLS==\n\n---------------------------------\n\n");
    printf("[01] A-Rat\n\n[98] Info\n[99] Back\n");
    scanf("\n%d", &hijackSectionInput);
    switch (hijackSectionInput)
    {
        case 1:
		a_rat();
		break;

	case 98:
		hijackhelp();
		break;

	case 99:
		break;

	default:
		prn_invalidinput();
		break;
    }
}
