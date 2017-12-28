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
 * O  = '\033[33m' # yellow
 * B  = '\033[1m'  # bold
 * RR = '\033[3m'  # italic
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
void color_white(void);
void color_red(void);
void color_green(void);
void color_yellow(void);
void color_bold(void); //I know, this is not a color!
void color_italic(void);
void reconSection(void); //Reconnaissance tools
//DEV0002: Functions for Reconnaissance tools
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
//DEV0002: Functions for Scanning tools
 void dtect(void);
 void dsss(void);
 void ciscoauditingtool(void);
 void nmap(void);
 void scanhelp(void);
void crackSection(void); //Encryption and Password Cracking tools
//DEV0002: Functions for encryption and password cracking tools
 void randompass(void);
 void shadowcrack(void);
 void blackhydra(void);
 void hashbuster(void);
 void hashidentifier(void);
 void cupp(void);
 void fbrute(void);
 void wifite(void);
 void crackhelp(void);
void exploitSection(void); //Exploitation tools
//DEV0002: Functions for exploitation tools
 void backdoor_factory(void);
 void brutal(void);
 void cge(void);
 void exploitdb(void);
 void les(void);
 void mpc(void);
 void msf(void);
 void exploithelp(void);
void dosSection(void); //Denial-of-Service tools
//DEV0002: Functions for DoS and DDoS tools
void hijackSection(void); //Session Hijacking tools
//DEV0002: Functions for Session Hijacking tools
void instdeps(void); //Install Dependencies function
void prn_license(void); //License function
void prn_help(void); //Help function 

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
    color_red();
    printf("\nERROR: Invalid Input\n");
    color_green();
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
    color_yellow();
    printf("\nDo you really want to quit?\nAnswer (y/n) : \n");
    scanf(" %c", &confirm);
    if (confirm == 'y' || confirm == 'Y')
    {
        clr();
        error_value = 0;
	color_red();
        printf("\nExiting...\n");
	color_white();
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
    color_yellow();
    printf("\nERROR: Under Construction!\n");
}

void prn_logo(void)
{
    //DEV0001: In the future, it needs to be standalone!
    //which means it doesn't need any third-party tools!
    color_green();
    system("figlet -f shadow Shadow Suite");
    printf("\n\"Ethical Hacking Toolkit\"\n");
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

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 *                                                                                     *
 *                          START OF PROGRAM FUNCTIONS                                 *
 *                                                                                     *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

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
    color_green();
    prn_logo();
    //DEV0002: This should be updated when a new reconnaissance tool is added.
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
    printf("\n==SCANNING TOOLS HELP==\n\n---------------------------------\n\n");
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
    printf("[1] D-Tect\n[2] DSSS\n[3] Cisco Auditing Tool\n[4] Nmap\n\n[98] Help\n[99] Back\n");
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
		prn_invalidinput();
		break;
    }
}

void randompass(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/randompass/src/ && bash randompass.sh");
    system("cd ../../../..");
}

void shadowcrack(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/shadowcrack/src/ && python2 ShadowCrack.py");
    readline();
    system("cd ../../../..");
}

void blackhydra(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/blackhydra/ && python2 blackhydra.py");
    //DEV0001: Uncomment the line if automatic program exit is present.
    //readline();
    system("cd ../../..");
}

void hashbuster(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/hashbuster/ && python2 hash.py");
    //DEV0001: Uncomment the line if automatic program exit is present.
    //readline();
    system("cd ../../..");
}

void hashidentifier(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/hashidentifier/ && python2 Hash_ID.py");
    system("cd ../../..");
}

void cupp(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/cupp/ && bash cupp-wrapper");
    system("cd ../../..");
}

void fbrute(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/fbrute && python2 facebook.py");
    /* DEV 0001: Uncomment the line if you confirm the automatic exit of the program. */
    //readline();
    system("cd ../../..");
}

void wifite(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/wifite2 && python2 Wifite.py");
    readline(); //DEV0001: This is temporary while my device isn't rooted.
                //But if automatic exit of the program is present, leave it here.
    system("cd ../../..");
}

void crackhelp(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this if a new cracking/encryption tool is added.
    printf("\n==ENCRYPTION AND PASSWORD CRACKING TOOLS HELP==\n\n---------------------------------\n\n");
    printf("Random Pass: Random Password block generator\n\n");
    printf("Shadow Crack: Hashing tool\n\n");
    printf("Black Hydra: Shorten brute force sessions on hydra\n\n");
    printf("Hash Buster: use several online hash crackers to find cleartext of a hash in less than 5 seconds.\n\n");
    printf("Hash Identifier: Identify the type of a hash.\n\n");
    printf("Common User Passwords Profiler (CUPP): Common user passwords profiler.\n\n");
    printf("Facebook Cracker: Crack facebook account's passwords.");
    printf("\nPress enter to continue...\n\n");
    readline();
}

void crackSection(void)
{
    int crackSectionInput;

    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this if a new cracking/encryption tool is added.
    printf("\n==ENCRYPTION AND PASSWORD CRACKING TOOLS==\n\n---------------------------------\n\n");
    printf("[1] Random Pass\n[2] Shadow Crack\n[3] Black Hydra\n[4] Hash Buster\n[5] Hash Identifier\n[6] Common User Passwords Profiler (CUPP)\n[7] Facebook Cracker\n[8] Wifite\t\t\t[i] ROOT REQUIRED\n\n[98] Help\n[99]Back\n");
    scanf("\n%d", &crackSectionInput);
    switch (crackSectionInput)
    {
        case 1:
		randompass();
		break;

	case 2:
		shadowcrack();
		break;

	case 3:
		blackhydra();
		break;

	case 4:
		hashbuster();
		break;

	case 5:
		hashidentifier();
		break;

	case 6:
		cupp();
		break;

	case 7:
		fbrute();
		break;

	case 8:
		wifite();
		break;

	case 98:
		crackhelp();
		break;

	case 99:
		break;

	default:
		prn_invalidinput();
		break;
    }
}

void backdoor_factory(void)
{
    clr();
    prn_logo();
    //DEV0001: Code the wrapper script!
    system("cd $PWD/tools/exploitation/backdoorfactory && bash backdoorfactory-wrapper");
    system("cd ../../..");
}

void brutal(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/brutal && bash Brutal.sh");
    system("cd ../../..");
}

void cge(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/cge && perl cge.pl");
    readline(); //DEV0001: Remove this if automatic exit of program is absent.
    system("cd ../../..");
}

void exploitdb(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/exploitdb && python2 exploitdb.py");
    readline(); //DEV0001: Remove if automatic exit of progran is absent.
    system("cd ../../..");
}

void les(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/les && bash les-wrapper");
    system("cd ../../..");
}

void mpc(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/mpc && bash msfpc.sh");
    readline(); //DEV0001: Delete if automatic exit of program is absent.
    system("cd ../../..");
}

void msf(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/exploitation/msf && ruby msfconsole");
    readline(); //DEV0001: Remove if automatic exit of program is absent.
    system("cd ,./../..");
}

void exploithelp(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this when a new explpitation tool is added.
    printf("\n==EXPLOITATION TOOLS==\n\n---------------------------------\n\n");
    printf("Backdoor Factory: Patch executable binaries with user desired shellcode and continue normal execution of the prepatched state.\n\n");
    printf("Brutal: Toolkit to quickly create various payload, powershell attack, virus attack and launch listener for a Human Interface Device.\n\n");
    printf("Cisco Global Exploiter: Exploit the most dangerous vulnerabilities of Cisco systems.\n\n");
    printf("Exploit Database: Search exploit-db.com exploits.");
    printf("\nPress enter to continue...\n\n");
}

void exploitSection(void)
{
    int exploitSectionInput;

    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this when a new exploitation tool is added.
    printf("\n==EXPLOITATION TOOLS==\n\n---------------------------------\n\n");
    printf("[1] Backdoor Factory\n[2] Brutal\n[3] Cisco Global Exploiter\n[4] Exploit Database\n[5] Linux Exploit Suggester\n[6] Metasploit Payload Creator\n[7] Metasploit Framework\n[8] RouterSploit\n[9] ShellShocker\n[10] WebDav\n\n[98] Help\n[99] Back\n");
    scanf("\n%d", &exploitSectionInput);
    switch (exploitSectionInput)
    {
        case 1:
		backdoor_factory();
		break;

	case 2:
		brutal();
		break;

	case 3:
		cge();
		break;

	case 4:
		exploitdb();
		break;

	case 5:
		les();
		break;

	case 6:
		mpc();
		break;

	case 7:
		msf();
		break;

	case 8:
		//routersploit();
		break;

	case 9:
		//shellshocker();
		break;

	case 10:
		//webdav();
		break;

	case 98:
		exploithelp();
		break;

	case 99:
		break;

	default:
		prn_invalidinput();
		break;
    }
}

void dosSection(void)
{
    clr();
    color_green();
    prn_logo();
    printf("\n==DENIAL-OF-SERVICE TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void hijackSection(void)
{
    clr();
    color_green();
    prn_logo();
    printf("\n==SESSION HIJACKING TOOLS==\n\n---------------------------------\n\n");
    prn_construction();
    readline();
}

void instdeps(void)
{
    int batch = 4;
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this if a new dependency is needed.
    printf("\n==INSTALL DEPENDENCIES==\n\n---------------------------------\n\n");
    printf("\nInstalling dependencies...\n");
    system("apt update -y");
    system("apt install apache2 apache2-dev bash bash-completion bash-dev binutils  binutils-dev bsdtar busybox command-not-found coreutils cowsay curl debianutils dialog diffutils dnsutils figlet findutils git gnupg gnupg2 inetutils iperf3 less lftp lighttpd neofetch net-tools netcat nginx nmap openssh openssl openssl-dev openssl-tool perl php php-apache php-dev php-pgsql postgresql privoxy proxychains-ng python python-dev python2 python2-dev radare2 radare2-dev readline readline-dev ruby ruby-dev sl sslscan tar tor torsocks tracepath tree util-linux vim w3m wget zip");
    system("pip install requests urllib3 shodan netaddr pefile simplejson pycurl");
    system("cpan LWP::UserAgent");
    system("cpan Net::Telnet");
    system("cpan Net::IP");
    system("cpan Net::DNS");
    system("cpan IO::Socket::SSL");
    printf("\nInstalling dependencies... Done!\n");
    printf("Press any key to continue...");
    readline();
}

void prn_license(void)
{
    clr();
    color_green();
    prn_logo();
    //Opens the LICENSE file.
    system("less LICENSE");
}

void prn_help(void)
{
    clr();
    color_green();
    prn_logo();
    //Opens the MANUAL file.
    system("less MANUAL");
}

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
    printf("\n[1] Reconnaissance (Information Gathering)\n[2] Scanning\n[3] Encryption and Password Cracking\n");
    printf("[4] Exploitation\n[5] Denial-of-Service (Stress Testing)\n[6] Session Hijacking\n");
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
    clr();
    color_red();
    printf("OH NO! PROGRAM MUST NOT GO HERE!\n\n");
    printf("This might be a bug, so please contact Shadow Team.\n");
    printf("Tell us what you had done and send it to any of thenfollowing::\n\n");
    printf("Public.ShadowTeam@gmail.com\nCatayao56@gmail.com\n");
    printf("\nPress any key to exit...\n");
    readline();
    return 1; //Program must not go here!!!
    exit(EXIT_FAILURE);
}
