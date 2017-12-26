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

/* Colors
 * W  = '\033[0m'  # white (normal)
 * R  = '\033[31m' # red
 * G  = '\033[32m' # green
 * O  = '\033[33m' # orange
 * B  = '\033[1m'  # bold
 * RR = '\033[3m'  # greencolor
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
void reconSection(void); //Reconnaissance tools
 void infoga(void);
 void redhawk(void);
 void set(void);
 void urlcrazy(void);
 void weeman(void);
 void dnsmap(void);
 void automater(void);
 void angryfuzzer(void);
 void metagoofil_remote(void);
 void metagoofil_local(void);
 void theharvester(void);
 void reconhelp(void);
void scanSection(void); //Scanning tools
 void dtect(void);
 void dsss(void);
 void ciscoauditingtool(void);
 void scanhelp(void);
void crackSection(void); //Encryption and Password Cracking tools
void exploitSection(void); //Exploitation tools
void dosSection(void); //Denial-of-Service tools
void hijackSection(void); //Session Hijacking tools
void instdeps(void); //Install Dependencies function
void prn_help(void); //Help function 

void clr(void)  //Clear and set color function
{
    system("echo -e \033[32m"); //Sets terminal color to green.
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
    prn_logo();
    printf("\nDo you really want to quit?\nAnswer (y/n) : \n");
    scanf(" %c", &confirm);
    if (confirm == 'y' || confirm == 'Y')
    {
        clr();
        error_value = 0;
        printf("\nExiting...\n");
	system("echo -e \033[0m""");
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
    prn_logo();
    printf("\nERROR: Under Construction!\n");
}

//prn_logo(); Function
void prn_logo(void)
{
        //In the future, it needs to be standalone!
        //which means it doesn't need any third-party tools!
    system("figlet -f shadow Shadow Suite");
    printf("\n\"Ethical Hacking Toolkit\"\n");
}

void infoga(void)
{
    clr();
    prn_logo();
    printf("\n==INFOGA (RECONNAISSANCE)==\n\n---------------------------------\n\n");
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
    prn_logo();
    printf("\n==RECONNAISSANCE TOOLS HELP==\n\n---------------------------------\n\n");
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
    prn_logo();
    printf("\n==RECONNAISSACE TOOLS==\n\n---------------------------------\n\n");
    printf("\n[1] Infoga\n[2] Red Hawk\n[3] Social Engineer Toolkit\t\t[!] ROOT REQUIRED\n[4] URLCrazy\n[5] Weeman\n[6] DNSMap\n[7] Automater\n[8] Angry Fuzz3r\n[9] Metagoofil (Remote)\n[10] Metagoofil (Local)\n[11] The Harvester\n\n[98] Help\n[99] Back\n");
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
		readline(); //This is temporary while my device is not rooted.
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
		break;

	default:
		prn_invalidinput();
		break;
    }
}

void dtect(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/scanning/dtect && python2 d-tect.py");
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

void scanhelp(void)
{
    clr();
    prn_logo();
    printf("\n==SCANNING TOOLS HELP==\n\n---------------------------------\n\n");
    printf("D-Tect: provides multiple features and detection features which gather target information and finds different flaws in it.\n\n");
    printf("DSSS: A fully functional SQLi Scanner\n\n");
    printf("\nPress enter to continue...\n\n");
    readline();
}

void scanSection(void)
{
    int scanSectionInput;

    clr();
    prn_logo();
    printf("\n==SCANNING TOOLS==\n\n---------------------------------\n\n");
    printf("[1] D-Tect\n[2] DSSS\n[3] Cisco Auditing Tool\n\n[98] Help\n[99] Back\n");
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

        case 98:
		scanhelp();
		break;

	case 99:
		break;

	default:
		prn_invalidinput();
		break;
    }
}

void crackSection(void)
{
    clr();
    prn_logo();
    printf("\n==ENCRYPTION AND PASSWORD CRACKING TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void exploitSection(void)
{
    clr();
    prn_logo();
    printf("\n==EXPLOITATION TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void dosSection(void)
{
    clr();
    prn_logo();
    printf("\n==DENIAL-OF-SERVICE TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void hijackSection(void)
{
    clr();
    prn_logo();
    printf("\n==SESSION HIJACKING TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void instdeps(void)
{
    int batch = 4;
    clr();
    prn_logo();
    printf("\n==INSTALL DEPENDENCIES==\n\n---------------------------------\n\n");
    printf("\nInstalling dependencies...\n");
    system("apt update -y");
    system("apt install apache2 apache2-dev bash bash-completion bash-dev binutils  binutils-dev bsdtar busybox command-not-found coreutils cowsay curl debianutils dialog diffutils dnsutils figlet findutils git gnupg gnupg2 inetutils iperf3 less lftp lighttpd neofetch net-tools netcat nginx nmap openssh openssl openssl-dev openssl-tool perl php php-apache php-dev php-pgsql postgresql privoxy proxychains-ng python python-dev python2 python2-dev radare2 radare2-dev readline readline-dev ruby ruby-dev sl sslscan tar tor torsocks tracepath tree util-linux vim w3m wget zip");
    system("pip install requests urllib3 shodan");
    printf("\nInstalling dependencies... Done!\n");
    printf("Press any key to continue...");
    readline();
}

void prn_help(void)
{
    clr();
    prn_logo();
    system("less MANUAL");
}

//Main Function
int main(void)
{
    char justarandomone = 'x';
    int section;

    while (justarandomone == 'x')
    {
    clr();
    //Prints the logo of Shadow Framework..
    prn_logo();
    printf("\n==TOOLS==\n\n---------------------------------\n\n");
    printf("\n[1] Reconnaissance\n[2] Scanning\n[3] Encryption and Password Cracking\n");
    printf("[4] Exploitation\n[5] Denial-of-Service\n[6] Session Hijacking\n");
    printf("\n[97] Help\n[98] Install Dependencies\n[99] Exit\n");

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
    return 1; //Program must not go here!!!
}
