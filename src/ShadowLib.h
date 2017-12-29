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
 * \033[0m  ==  white (normal)
 * \033[31m ==  red
 * \033[32m ==  green
 * \033[33m ==  yellow
 * \033[1m  ==  bold
 * \033[3m  ==  italic
 *
 * Below not yet used;
 *
 * \033[34m ==  blue
 * \033[35m ==  purple
 * \033[36m ==  cyan
 * \033[37m ==  gray
 */

//Include preprocessor directives
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

//Define preprocessor directives
//#define PI 3.141326   If you ever need this, this is the value of PI.
#define MAXSTRING 100
#define MINSTRING 1
#define MAJOR_VERSION 0
#define MINOR_VERSION 0
#define BETA_VERSION 3
//WB stands for Weekly Build.
#define WB_VERSION 0
#define BUILD_TYPE "Experimental"
//BUILD_TYPE define hint:
//
//Choose between "Weekly_Build", "Unstable_Release", "Experimental", or"Stable_Release".
//Weekly_Build:   Means update of the program which is released weekly; has many bugs
//                and has tools under development.
//
//Unstable_Release: Means update of the program which has a new tool that is in
//                  first-usable stage, but still has many bugs and more features
//                  needs to implement..
//
//Experimental: Means update of the program which has a new tool and has all the features,
//              but has some bugs on it.
//
//Stable_Release: Means update of the program which is stable, and almost all bugs
//               are fixed; after this, a "maintenance/feature update" can be initialized.

//Function declarations
void error101(void); /*Error code 101 */
void clr(void); //Clears the screen.
void readline(void); //Wait for user input.
void prn_invalidinput(void); //Prints the invalid input message.
void exit_confirm(void); //Asks for exit confirmation.
void prn_construction(void); //Prints the under construction message.
void prn_logo(void); //Prints our logo.
void color_white(void); //Colors
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
 void msf(void);
 void routersploit(void);
 void shellshocker(void);
 void exploithelp(void);

void dosSection(void); //Denial-of-Service tools
//DEV0002: Functions for DoS and DDoS tools
 void fl00d(void);
 void fl00d2(void);
 void doshelp(void);
 void slowloris(void);
 void torshammer(void);

void hijackSection(void); //Session Hijacking tools
//DEV0002: Functions for Session Hijacking tools
 void a_rat(void);
 void hijackhelp(void);

void instdeps(void); //Install Dependencies function
void prn_license(void); //License function
void prn_help(void); //Help function 
