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

void instdeps(void)
{
    clr();
    color_green();
    prn_logo();
    //DEV0002: Update this if a new dependency is needed.
    printf("\n==INSTALL DEPENDENCIES==\n\n---------------------------------\n\n");
    printf("\nInstalling dependencies...\n\n\n");
    //Updates the package information from APT.
    system("apt update -y");
    //Installs dependencies from apt_requirements.
    system("bash inst_deps.bash");
    //Installs python modules from python_requirements
    system("pip install -r python_requirements");
    system("pip3 install -r python_requirements");
    //Installs perl modules.
    system("cpan LWP::UserAgent");
    system("cpan Net::Telnet");
    system("cpan Net::IP");
    system("cpan Net::DNS");
    system("cpan IO::Socket::SSL");
    system("cpan Term::ANSIColor");
    system("cpan Getopt::Long");
    system("cpan IO::File");
    system("cpan Net::IP");
    system("cpan Net::DNS");
    system("cpan Net::Netmask");
    system("cpan XML::Writer");
    system("cpan Config");
    system("cpan Socket");
    system("cpan String::Random");
    system("cpan DotDotPwn::TraversalEngine");
    system("cpan DotDotPwn::HTTP");
    system("cpan DotDotPwn::HTTP_Url");
    system("cpan DotDotPwn::FTP");
    system("cpan DotDotPwn::TFTP");
    system("cpan DotDotPwn::Payload");
    system("cpan DotDotPwn::STDOUT");
    system("cpan DotDotPwn::Fingerprint");
    system("cpan DotDotPwn::BisectionAlgorithm");
    system("cpan GetOpt:Std");
    printf("\n\n\nInstalling dependencies... Done!\n");
    printf("Press any key to continue...");
    readline();
}
