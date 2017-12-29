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

void infoga(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/infoga/ && bash infoga_wrapper.sh");
    system("cd ../../..");
}

void redhawk(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/redhawk/ && php rhawk.php");
    system("cd ../../..");
}

void set(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/set/ && python2 set");
    system("cd ../../..");
}

void urlcrazy(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/urlcrazy/ && chmod +x urlcrazy-wrapper && ./urlcrazy-wrapper");
    system("cd ../../..");
}

void weeman(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/weeman/ && python2 weeman.py");
    system("cd ../../..");
}

void dnsmap(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/dnsmap/ && python2 dnsmap.py");
    system("cd ../../..");
    readline();
}

void automater(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/automater/ && bash automater-wrapper");
    system("cd ../../..");
}

void angryfuzzer(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/angryfuzzer/ && bash angryfuzzer-wrapper");
    system("cd ../../..");
}

void metagoofil_remote(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/metagoofil/ && bash metagoofil-wrapper-remote");
    system("cd ../../..");
}

void metagoofil_local(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/metagoofil/ && bash metagoofil-wrapper-local");
    system("cd ../../..");
}

void theharvester(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/reconnaissance/theharvester && bash theharvester-wrapper");
    system("cd ../../..");
}

void reconhelp(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: This should be updated when a new reconnaissance tool is added.
    printf("\n==RECONNAISSANCE TOOLS INFO==\n\n---------------------------------\n\n");
    printf("Infoga: Email Information Gathering tool\n\n");
    printf("Red Hawk: Website Information Gathering tool\n\n");
    printf("Social Engineer Toolkit: Social Engineering tool\t\t[i] ROOT REQUIRED\n\n");
    printf("URLCrazy: study domainname typos and URL hijacking\n\n");
    printf("Weeman: HTTP Server for phishing.\n\n");
    printf("DNSMap: discover the target company's IP netblocks, domain names, phone numbers, etc.\n\n");
    printf("Automater: Automate the OSINT analysis of IP Addresses.\n\n");
    printf("Angry Fuzz3r: collection of tools for pentesting to gather information and discover vulnerabilities of the targets based on Fuzzedb\n\n");
    printf("Metagoofil: metadata extractor\n\n");
    printf("The Harvester: tool for gathering target details.\n\n");
    printf("\nPress enter to continue...\n");
    readline();
}

void reconSection(void)
{
    int reconSectionInput;

    clr();
    color_green();
    prn_logo();
    //DEV0002: This should be updated when a new reconnaissance tool is added.
    printf("\n==RECONNAISSACE TOOLS==\n\n---------------------------------\n\n");
    printf("\n[1] Infoga\n[2] Red Hawk\n[3] Social Engineer Toolkit\t\t[!] ROOT REQUIRED\n[4] URLCrazy\n[5] Weeman\n[6] DNSMap\n[7] Automater\n[8] Angry Fuzz3r\n[9] Metagoofil (Remote)\n[10] Metagoofil (Local)\n[11] The Harvester\n\n[98] Info\n[99] Back\n");
    scanf("\n%d", &reconSectionInput);
    switch (reconSectionInput)
    {
        case 1:
		infoga();
		break;

	case 2:
		redhawk();
		break;

	case 3:
		set();
		readline(); //DEV0001: This is temporary while my device is not rooted.
		break;

	case 4:
		urlcrazy();
		break;

	case 5:
		weeman();
		break;

	case 6:
		dnsmap();
		break;

	case 7:
		automater();
		break;

	case 8:
		angryfuzzer();
		break;

	case 9:
		metagoofil_remote();
		break;

	case 10:
		metagoofil_local();
		break;

	case 11:
		theharvester();
		break;

	case 98:
		reconhelp();
		break;

	case 99:
		//Blank statement; Oh, there's a statement... The 'break;' statement.
		break;

	default:
		//If none of the above met, 'prn_invalidinput();' function will be called.
		prn_invalidinput();
		break;
    }
}