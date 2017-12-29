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
    readline();
    system("cd ../../..");
}

void hashbuster(void)
{
    clr();
    prn_logo();
    system("cd $PWD/tools/cracking/hashbuster/ && python2 hash.py");
    readline();
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
    printf("\n==ENCRYPTION AND PASSWORD CRACKING TOOLS INFO ==\n\n---------------------------------\n\n");
    printf("Random Pass: Random Password block generator\n\n");
    printf("Shadow Crack: Hashing tool\n\n");
    printf("Black Hydra: Shorten brute force sessions on hydra\n\n");
    printf("Hash Buster: use several online hash crackers to find cleartext of a hash in less than 5 seconds.\n\n");
    printf("Hash Identifier: Identify the type of a hash.\n\n");
    printf("Common User Passwords Profiler (CUPP): Common user passwords profiler.\n\n");
    printf("Facebook Cracker: Crack facebook account's passwords.\n\n");
    printf("Wifite: Wireless network auditor.\n\n");
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
    printf("[1] Random Pass\n[2] Shadow Crack\n[3] Black Hydra\n[4] Hash Buster\n[5] Hash Identifier\n[6] Common User Passwords Profiler (CUPP)\n[7] Facebook Cracker\n[8] Wifite\t\t\t[i] ROOT REQUIRED\n\n[98] Info\n[99]Back\n");
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
