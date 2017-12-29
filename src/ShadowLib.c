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

void prn_logo(void)
{
    //DEV0001: In the future, it needs to be standalone!
    //which means it doesn't need any third-party tools!
    color_green();
    system("figlet -f shadow Shadow Suite");
    printf("\n\"Ethical Hacking Toolkit\"\n");
    //Prints the program's version.
    printf("v%d.%d.%d.%d -- %s\n", MAJOR_VERSION, MINOR_VERSION, BETA_VERSION, WB_VERSION, BUILD_TYPE);
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
