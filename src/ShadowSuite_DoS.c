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

void fl00d(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/dos/fl00d/ && python2 fl00d.py");
    readline();
    system("cd ../../..");
}

void fl00d2(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/dos/fl00d/ && python2 fl00d2.py");
    readline();
    system("cd ../../..");
}

void slowloris(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/dos/slowloris/ && bash slowloris-wrapper");
    system("cd ../../..");
}

void torshammer(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/dos/torshammer/ && bash torshammer-wrapper");
    system("cd ../../..");
}

void ufonet(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/dos/ufonet/ && python2 ufonet");
    readline(); //DEV0001: Remove is program's automatic exit is absent or needs a
    system("cd ../../..");                                        //wrapper script.
}

void doshelp(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this if a new DoS or DDoS tool is added.
    printf("\n==DENIAL-OF-SERVICE TOOLS INFO ==\n\n---------------------------------\n\n");
    printf("fl00d: fl00d is a Stress testing tool to perform DoS attacks.\n\n");
    printf("fl00d 2: an enhanced version of fl00d.\n\n");
    printf("Slowloris: Low bandwidth stress test tool for websites\n\n");
    printf("Tor's Hammer: Slow POST DoS Testing Tool\n\n");
    printf("UFONet: Launch DDoS attacks against a target, using 'Open Redirect' vectors on third party web applications, like botnet\n\n");
    printf("\nPress enter to continue...\n\n");
    readline();
}

void dosSection(void)
{
    int dosSectionInput;
    clr();
    color_green();
    prn_logo();
    printf("\n==DENIAL-OF-SERVICE TOOLS==\n\n---------------------------------\n\n");
    printf("[1] Fl00d\n[2] Fl00d 2\n[3] Slowloris\n[4] Tor's Hammer\n[5] UFONet\n\n[98] Info\n[99] Back\n");
    scanf("\n%d", &dosSectionInput);
    switch (dosSectionInput)
    {
	    case 1:
		    fl00d();
		    break;

	    case 2:
		    fl00d2();
		    break;

	    case 3:
		    slowloris();
		    break;

	    case 4:
		    torshammer();
		    break;

	    case 5:
		    ufonet();
		    break;

	    case 98:
		    doshelp();
		    break;

	    case 99:
		    break;

	    default:
		    prn_invalidinput();
		    break;
    }
}
