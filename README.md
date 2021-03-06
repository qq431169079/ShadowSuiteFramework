# Shadow Suite Framework 0.1.2.4: Ethical Hacking Toolkit and Framework
## Copyright (C) 2017-2018: Shadow Team <Public.ShadowTeam@gmail.com>
[Shadow Suite Framework](https://gitlab.com/Catayao56/ShadowSuiteFramework.git) is an Ethical Hacking Toolkit and Framework.
It was created on Thursday, Dec 7 2:44:37 PM, 2017.
It provides many tools that you can use,
written mainly in Python, BASH, PHP, etc.
Tools that you need for reconnaissance, scanning,
exploitation, encryption, password cracking, and more!
Shadow Suite Framework is the main project of Shadow Team.

## What's new?
+ ATTENTION: We just moved to GitLab, people!
      -https://gitlab.com/Catayao56/ShadowSuiteFramework.git

## Full Feature List
+ Open Source
      -Shadow Suite is protected by the GNU General Public License, means
       that you can freely download, modify, and distribute the software.
       Just give "creds" to us and the developers that made the awesome
       tools)

+ Create Custom Modules from template
      -Do you know Python? Do you know how to code in Python? Do you want
       to create your own module that can penetration test a Class A network
       in just three seconds? (exagerrated) Shadow Suite Framework provides
       a module template to help you start creating your custom module. It also
       provides an Application Programming Interface (API) to help you on
       the integration of Shadow Suite Framework and your custom module.

       You can also submit your custom module to us to make it pre-installed!

+ Pre-installed modules
      -It's okay if you don't know how to program. Shadow Suite Framework has an
       arsenal! It provides you tools written in different languages. Python,
       Ruby, Perl, PHP, and many more!

+ Services
      -Its too bad if you need to open multiple instances of SSF just to do other
       tasks... So services just've come! Start those services such as servers,
       background hash crackers, and many more!

+ Secrets
      -We know this is not really necessary, But its fun to look at the code to
       see SSF secrets!

## TO-DO List
+ Issues
[ ] #0001: Some modules are not found when running on popular linux systems, such as Ubuntu and Kali.
[ ] #0002: modules lower than v7 doesn't use the "global variables" and doesn't check if the user has changed the "MODULE PATH" variable.
[ ] #0003: Readline bug, when 'scrolling' through the recently entered *long* commands, the prompt disappears and the UI goes bezerk!P
[ ] #0004: Readline bug, it does not read the command history properly.
[ ] #0005: Notepad bug fixes... BUGGY!
[ ] #0006: Python requirements has no info if it is python 2 or 3.
[ ] #0007: On termux, (but maybe also in other systems) try to run vim via 'run vim [FILENAME]' and go to another app. When you go back, a very buggy UI will show.

+ Maintenance
[ ] #0001: Fix update algorithms. (*ONGOING; Testing needed*)
[ ] #0002: Module fixes.
[ ] #0003: Module API support.
[ ] #0004: Update FL00D, BRAT, and Deception.
[ ] #0005: API arguments as dict.
[ ] #0006: Installation of modules using a number of archive formats (for modules with subdirectories) or optional/online install mode.
[ ] #0007: More logging verbosity.

+ Feature Requests
[ ] #0001: Metasploit Framework, MultiTool, Aeneas Of Troy's PortScaner, PassHunt, Encrypted IM client (If available).
[ ] #0002: less for python 3
[ ] #0003: List tools by category.

## License and Copying

+ This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

+ See LICENSE file.

## Credits

	###Shadow Suite Framework Contributors
	Project Lead: Catayao56
	Project co-lead: Sh4d0wH4X0R

	==Modules==
	NMap Team: for creating NMap Network Mapper.
	R3D#@0R_2H1N A.K.A Tuhinshubhra: for creating Red Hawk.
	TekDefense: for creating Automater.
	Filip Waeytens: for creating the original DNSEnum DNS Enumeration tool.
	Stephan van de Kerkhof: for creating LANScan and for encouraging us.
	Christian Martorella: for creating Metagoofil and The Harvester.
	g0ne [null0]: for creating Cisco Auditing Tool.
	Nemesis: for creating Cisco Global Exploiter.
	SecTester: for creating DotDotPwn.
	DedSecTL, AndroSec1337, Catayao56: for creating Fl00d DoS Tool; Catayao56 for porting Fl00d to Python 3.
	Shawar Khan: for creating D-TECT.
	NullArray: for creating Shell Shocker.
	Ultimate Hackers: for creating Striker and Hash Buster.
	Miroslav Stampar: for creating Damn Small SQLi Scanner (DSSS) and SQLMap.
	Zion3R: for creating Hash Identifier.
	Shadow Team: for creating ShadowCrack.
	DedSecTL: for creating Black Hydra.
	Muris Kurgas aka j0rgan: for creating Common User Passwords Profiler.
	Pentura Labs: for creating Linux Exploit Suggester.
	Marcin Bury (lucyoa) & Mariusz Kupidura (fwkz): for creating RouterSploit.
	Robin Wood: for creating Pipal.
	Social Engineer Development Team: for creating Social Engineer Toolkit.
	Andrew Horton: for creating URLCrazy.
	Hypsurus: for creating Weeman.

		Whoever you are, thank you for creating:
		-DNSMap
		-DNSrecon
		-Angry Fuzz3r
		-Slowloris

	==Others==
        Offensive Security: for creating Kali Linux, Kali NetHunter,
	                    and Exploit Database.
        Linus Torvalds and contributors: for creating the Linux Operating System.
	Termux Developers: for creating an amazing terminal emulator for Android.

	[i] More contributors in program; Type 'module info [MODULE NAME]' on SSF Console.

## Requirements
+ Tested Operating Systems are Kali, Mint, Ubuntu, Termux Terminal Emulator for Android, and Cygwin Terminal Emulator for Windows
	
+ Not yet tested for Windows Operating Systems...

+ Worked on your operating system but not listed here? Please contact us and we'll be happy to include it here!

+ Internet Connection. (for performing remote attacks and/or updating)
+ Python Interpreter version 2 and 3.
+ Dependencies
	-Dependencies can be installed automatically in the program. (Needs Internet Connection)
	-To manually install, type "sudo python3 core/update.py" and "bash instdeps.bash".


## Installing & Running
------------------------
1.Installing and Running
      -Enter these commands in your terminal:

      $ sudo apt update && apt upgrade -y [1]
      $ sudo apt install python git [2]
      $ git clone https://gitlab.com/Catayao56/ShadowSuiteFramework.git [3]
      $ cd ShadowSuiteFramework/src && chmod 755 SSF.py [4]
      $ ./SSF.py [5]
      [Shadow] $ full update [6]
      [Shadow] $ help [7]

      [1] Update repository package list/s.
      [2] Install Python interpreter and Git client.
      [3] Clone Shadow Suite Framework from Catayao56's Github repository.
      [4] Changes directory to ShadowSuiteFramework/src and changes file mode to executable.
      [5] Run 'SSF.py'.
      [6] Type 'full update' on Shadow Suite's console to update
          the program and dependencies.
      [7] Type 'help' on Shadow Suite's console to see the help menu.

      -To see more installation guides, see MANUAL file.

2.Questions? Feature requests? Bugs?
      
      -Just contact us and we'll respond as soon as possible. You can also create a pull request on https://gitlab.com/Catayao56/ShadowSuiteFramework.git
