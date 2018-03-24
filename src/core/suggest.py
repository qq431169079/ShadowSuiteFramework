#!/bin/python
# Coding=UTF-8
# Shadow Suite Linux Edition :: Ethical Hacking Toolkit
# Copyright (C) 2017-2018  Shadow Team <Public.ShadowTeam@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from core import error
from core import misc
from core import version

def api(criteria):
    criteria = criteria.lower()
    criteria = criteria.replace(',', ' ')
    print("Searching...")
    results = 0

    # Conditional Statements
    if 'automater' in criteria or 'auto' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'tekdefese' in criteria or 'python' in criteria or 'ip' in criteria or 'url' in criteria or 'hash' in criteria or 'passive' in criteria and 'analysis' in criteria:
        print(misc.cg + "Automater : IP, URL, and Hash Passive Analysis Tool.\n" + misc.cw)
        results = results + 1
    
    if 'dnsenum' in criteria or 'multithread' in criteria or 'perl' in criteria or 'enum' in criteria or 'dns' in criteria or 'info' in criteria and 'ga' in criteria or 'domain' in criteria or 'ip' in criteria or 'block' in criteria or 'filip' in criteria and 'waeytens' in criteria:
        print(misc.cg + "DNSEnum : Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.\n" + misc.cw)
        results = results + 1

    if 'dnsmap' in criteria or 'filip' in criteria and 'waeytens' in criteria or 'info' in criteria and 'ga' in criteria or 'enum' in criteria or 'sec' in criteria or 'assess' in criteria or 'dns' in criteria or 'python' in criteria:
        print(misc.cg + "DNSMap : Mainly meant to be used by pentesters during the information gathering/enumeration phase of infrastructure security assessments.\n" + misc.cw)
        results = results + 1

    if 'dnsrecon' in criteria or 'dns' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'python' in criteria:
        print(misc.cg + "DNSRecon : DNS Reconnaissance Tool.\n" + misc.cw)
        results = results + 1

    if 'lanscan' in criteria or 'stephan' in criteria and 'van' in criteria and 'de' in criteria and 'kerkhof' in criteria or 'ping' in criteria or 'tcp' in criteria or 'net' in criteria and 'scan' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'python' in criteria:
        print(misc.cg + "LANScan : System ping / TCP network scanner.\n" + misc.cw)
        results = results + 1

    if 'metagoofil' in criteria or 'christian' in criteria and 'martorella' in criteria or 'extract' in criteria or 'meta' in criteria or 'doc' in criteria or 'pdf' in criteria or 'xls' in criteria or 'ppt' in criteria or 'web' in criteria or 'python' in criteria:
        print(misc.cg + "Metagoofil : A tool for extracting metadata of public documents (pdf,doc,xls,ppt,etc) availables in the target websites.\n" + misc.cw)
        results = results + 1

    if 'nmap' in criteria or 'nwrap' in criteria or 'catayao56' in criteria or 'net' in criteria and 'map' in criteria or 'port' in criteria and 'scan' in criteria or 'ping' in criteria or 'tcp' in criteria or 'udp' in criteria or 'python' in criteria:
        print(misc.cg + "Nwrap : Wrapper script for NMap Network Mapper.\n")
        results = results + 1

    if 'red' in criteria and 'hawk' in criteria or 'r3d#@0r_2h1n' in criteria or 'tuhinshubhra' in criteria or 'info' in criteria and 'ga' in criteria or 'vuln' in criteria and 'scan' in criteria or 'wordpress' in criteria or 'wp' in criteria or 'php' in criteria:
        print(misc.cg + "Red Hawk : All in One tool for Information Gathering and Vulnerability Scanning.\n")
        results = results + 1

    if 'the' in criteria and 'harvest' in criteria or 'python' in criteria or 'christian' in criteria and 'martorella' in criteria or 'ga' in criteria or 'email' in criteria or 'acc' in criteria or 'subdomain' in criteria or 'virtual' in criteria and 'host' in criteria or 'port' in criteria or 'banner' in criteria or 'employee' in criteria and 'name' in criteria or 'search' in criteria:
        print(misc.cg + "The Harvester : A tool for gathering e-mail accounts, subdomain names, virtual hosts, open ports/banners, and employee names from different public sources (search engines, pgp key servers).\n" + misc.cw)
        results = results + 1

    if 'cisco' in criteria or 'audit' in criteria or 'g0ne' in criteria or 'null0' in criteria or 'net' in criteria:
        print(misc.cg + "Cisco Auditing Tool : A tool for auditing Cisco networks.\n" + misc.cw)
        results = results + 1

    if 'cisco' in criteria or 'exploit' in criteria or 'vuln' in criteria:
        print(misc.cg + "Cisco Global Exploiter : An advanced,simple and fast security testing tool, that is able to exploit the most dangerous vulnerabilities of Cisco systems.\n" + misc.cw)
        results = results + 1

    if 'angry' in criteria and 'fuzz' in criteria or 'info' in criteria and 'ga' in criteria or 'discover' in criteria or 'vuln' in criteria or 'fuzz' in criteria:
        print(misc.cg + "Angry Fuzz3r : A collection of tools for pentesting to gather information and discover vulnerabilities of the targets based on Fuzzedb https://github.com/fuzzdb-project/fuzzdb project.\n" + misc.cw)
        results = results + 1

    if 'dot' in criteria and 'pwn' in criteria or 'sectester' in criteria or 'intelligent' in criteria or 'fuzz' in criteria or 'discover' in criteria or 'traversal' in criteria or 'dir' in criteria or 'vuln' in criteria or 'soft' in criteria or 'http' in criteria or 'ftp' in criteria or 'tftp' in criteria or 'server' in criteria or 'web' in criteria or 'cms' in criteria or 'erp' in criteria or 'blog' in criteria or 'perl' in criteria:
        print(misc.cg + "DotDotPwn : A very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc.\n" + misc.cw)
        results = results + 1

    if 'fl00d' in criteria or 'dedsectl' in criteria or 'androsec1337' in criteria or 'catayao56' in criteria or 'simple' in criteria or 'dos' in criteria or 'denial' in criteria and 'service' in criteria or 'low' in criteria and 'security' in criteria or 'python' in criteria or 'stress' in criteria and 'test' in criteria:
        print(misc.cg + "Fl00d : A simple DoS tool for target hosts with low-level security.\n" + misc.cw)
        results = results + 1

    if 'slowloris' in criteria or 'low' in criteria and 'bandwidth' in criteria or 'stress' in criteria and 'test' in criteria or 'web' in criteria:
        print(misc.cg + "Slowloris : Low bandwidth stress test tool for websites.\n" + misc.cw)
        results = results + 1

    if 'dtect' in criteria or 'shawar' in criteria and 'khan' in criteria or 'python' in criteria or 'word' in criteria and 'press' in criteria or 'wp' in criteria or 'username' in criteria or 'enum' in criteria or 'sensitive' in criteria or 'file' in criteria or 'detect' in criteria or 'sub' in criteria and 'domain' in criteria or 'scan' in criteria or 'port' in criteria or 'cross' in criteria and 'site' in criteria and 'script' in criteria or 'xss' in criteria or 'backup' in criteria and 'grab' in criteria or 'sql' in criteria and 'inject' in criteria or 'sqli' in criteria:
        print(misc.cg + "D-Tect : An All-In-One Tool that provides multiple features and detection features which gather target information and finds different flaws in it.\n" + misc.cw)
        results = results + 1

    if 'shell' in criteria or 'shock' in criteria or 'nullarray' in criteria or 'vuln' in criteria:
        print(misc.cg + "Shellshocker : A bash script that tests [a list of] hosts for the shellshock vulnerability.\n" + misc.cw)
        results = results + 1

    if 'striker' in criteria or 'ultimate' in criteria and 'hacker' in criteria or 'offensive' in criteria or 'info' in criteria or 'vuln' in criteria or 'scan' in criteria:
        print(misc.cg + "Striker : An offensive information and vulnerability scanner.\n" + misc.cw)
        results = results + 1

    if 'damn' in criteria and 'small' in criteria and 'sqli' in criteria and 'scanner' in criteria or 'dsss' in criteria or 'sql' in criteria or 'scan' in criteria or 'python' in criteria or 'miroslav' in criteria and 'stampar' in criteria or 'database' in criteria or 'db' in criteria:
        print(misc.cg + "DSSS :: A fully functional SQL Injection vulnerability scanner (supporting GET and POST parameters) written in under 100 lines of code.\n" + misc.cw)
        results = results + 1

    if 'sql' in criteria or 'sqlmap' in criteria or 'miroslav' in criteria and 'stampar' in criteria or 'inject' in criteria or 'database' in criteria or 'db' in criteria or 'python' in criteria:
        print(misc.cg + "SQLMap :: An open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.\n" + misc.cw)
        results = results + 1

    if 'hash' in criteria or 'id' in criteria or 'zion3r' in criteria or 'type' in criteria or 'python' in criteria:
        print(misc.cg + "Hash Identifier :: Identifies hash types.\n" + misc.cw)
        results = results + 1

    if 'hash' in criteria or 'shadow' in criteria or 'crack' in criteria or 'md5' in criteria or 'sha' in criteria:
        print(misc.cg + "ShadowCrack :: A hashing tool used to encrypt strings and/or crack hashes.\n" + misc.cw)
        results = results + 1

    if 'black' in criteria or 'hydra' in criteria or 'crack' in criteria or 'dedsectl' in criteria or 'python' in criteria or 'online' in criteria:
        print(misc.cg + "Black Hydra :: A small program to shorten brute force sessions in hydra.\n" + misc.cw)
        results = results + 1

    if 'cupp' in criteria or 'j0rgan' in criteria or 'muris' in criteria and 'kurgas' in criteria or 'wordlist' in criteria or 'wl' in criteria or 'profil' in criteria:
        print(misc.cg + "CUPP :: Common user passwords profiler.\n" + misc.cw)
        results = results + 1

    if 'routersploit' in criteria or 'marcin' in criteria and 'bury' in criteria or 'router' in criteria or 'exploit' in criteria or 'framework' in criteria:
        print(misc.cg + "RouterSploit :: A Router Exploitation Framework.\n" + misc.cw)
        results = results + 1

    if 'pipal' in criteria or 'robin' in criteria and 'wood' in criteria or 'pass' in criteria or 'word' in criteria or 'analys' in criteria or 'ruby' in criteria:
        print(misc.cg + "Pipal :: Password Analyser.\n" + misc.cw)
        results = results + 1

    if 'set' in criteria or 'social' in criteria or 'engineer' in criteria or 'toolkit' in criteria or 'info' in criteria or 'ga' in criteria or 'recon' in criteria or 'python' in criteria:
        print(misc.cg + "Social Engineer Toolkit :: A tool designed to make complex social engineering tasks relatively simple for you by allowing you to utilize a robust framework for penetration tests.\n" + misc.cw)
        results = results + 1

    if 'ipify' in criteria or 'catayao56' in criteria or 'public' in criteria or 'ip' in criteria or 'external' in criteria or 'python' in criteria:
        print(misc.cg + "Ipify :: A simple Public IP Address API.\n" + misc.cw)
        results = results + 1

    if 'urlcrazy' in criteria or 'andrew' in criteria or 'horton' in criteria or 'typo' in criteria or 'hijack' in criteria or 'ruby' in criteria:
        print(misc.cg + "URLCrazy :: UrlCrazy is for the study of domainname typos and URL hijacking.\n" + misc.cw)
        results = results + 1

    # More info
    print("\n")
    results = str(results)
    if results == "0":
        print("SORRY! No tool matched your criteria... Please contact Shadow Team for Feature requests...")
    elif results == "1":
        print(results + " tool matched your criteria.")

    else:
        print(results + " tools matched your criteria!")
