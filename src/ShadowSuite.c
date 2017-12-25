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
void reconSection(void); //Reconnaissance section
 void infoga(void);
void scanSection(void); //Scanning section
void crackSection(void); //Encryption and Password Cracking section
void exploitSection(void); //Exploitation section
void dosSection(void); //Denial-of-Service section
void hijackSection(void); //Session Hijacking section
void instdeps(void); //Install Dependencies function
void prn_help(void); //Help function 

void clr(void)  //Clear function
{
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
    system("cd $PWD/sections/reconnaissance/infoga/ && bash infoga_wrapper.sh");
    system("cd ../../..");
}

void redhawk(void)
{
    clr();
    system("cd $PWD/sections/reconnaissance/redhawk/ && php rhawk.php");
    system("cd ../../..");
}

void set(void)
{
    clr();
    system("cd $PWD/sections/reconnaissance/set/ && python2 set");
    system("cd ../../..");
}

void urlcrazy(void)
{
    clr();
    system("cd $PWD/sections/reconnaissance/urlcrazy/ && chmod +x urlcrazy-wrapper && ./urlcrazy-wrapper");
    system("cd ../../..");
}

void weeman(void)
{
    clr();
    system("cd $PWD/sections/reconnaissance/weeman/ && python2 weeman.py");
    system("cd ../../..");
}

void reconSection(void)
{
    int reconSectionInput;

    clr();
    prn_logo();
    printf("\n==RECONNAISSACE SECTION==\n\n---------------------------------\n\n");
    printf("\n[1] Infoga\n[2] Red Hawk\n[3] Social Engineer Toolkit [!] ROOT REQUIRED\n[4] URLCrazy\n[5] Weeman\n\n[99] Back\n");
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
		break;

	case 4:
		urlcrazy();
		break;

	case 5:
		weeman();
		break;

	case 99:
		main();
		break;

	default:
		prn_invalidinput();
		break;
    }
}

void scanSection(void)
{
    clr();
    prn_logo();
    printf("\n==SCANNING SECTION==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void crackSection(void)
{
    clr();
    prn_logo();
    printf("\n==ENCRYPTION AND PASSWORD CRACKING SECTION==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void exploitSection(void)
{
    clr();
    prn_logo();
    printf("\n==EXPLOITATION SECTION==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void dosSection(void)
{
    clr();
    prn_logo();
    printf("\n==DENIAL-OF-SERVICE SECTION==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void hijackSection(void)
{
    clr();
    prn_logo();
    printf("\n==SESSION HIJACKING SECTION==\n\n---------------------------------\n\n");
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
    printf("\n==MODULES==\n\n---------------------------------\n\n");
    printf("\n[1] Reconnaissance\n[2] Scanning\n[3] Encryption and Password Cracking\n");
    printf("[4] Exploitation\n[5] Denial-of-Service\n[6] Session Hijacking\n");
    printf("\n[98] Install Dependencies\n[99] Exit\n");

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
