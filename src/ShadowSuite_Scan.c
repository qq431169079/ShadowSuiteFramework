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

void dtect(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/scanning/dtect && python2 d-tect.py");
    readline();
    system("cd ../../..");
}

void dsss(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/scanning/dsss && bash dsss-wrapper");
    system("cd ../../..");
}

void ciscoauditingtool(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/scanning/cisco-auditing-tool && bash cat-wrapper");
    system("cd ../../..");
}

void nmap(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/scanning/nmap/ && bash nmap-wrapper");
    system("cd ../../..");
}

void scanhelp(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this when a new scanning tool is added.
    printf("\n==SCANNING TOOLS INFO==\n\n---------------------------------\n\n");
    printf("D-Tect: provides multiple features and detection features which gather target information and finds different flaws in it.\n\n");
    printf("DSSS: A fully functional SQLi Scanner\n\n");
    printf("Cisco Auditing Tool: Scans cisco routers for common vulnerabilities.\n\n");
    printf("Nmap: Network exploration tool and security / port scanner\n\n");
    printf("\nPress enter to continue...\n\n");
    readline();
}

void scanSection(void)
{
    int scanSectionInput;

    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this when a new scanning tool is added.
    printf("\n==SCANNING TOOLS==\n\n---------------------------------\n\n");
    printf("[1] D-Tect\n[2] DSSS\n[3] Cisco Auditing Tool\n[4] Nmap\n\n[98] Info\n[99] Back\n");
    scanf("\n%d", &scanSectionInput);
    switch (scanSectionInput)
    {
	case 1:
		dtect();
		break;

	case 2:
		dsss();
		break;

	case 3:
		ciscoauditingtool();
		break;

	case 4:
		nmap();
		break;

        case 98:
		scanhelp();
		break;

	case 99:
		break;

	default:
		//If none of the above met, the prn_invalidinput(); will be called.
		prn_invalidinput();
		break;
    }
}