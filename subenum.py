# Subdomain enumerationn tool.
'''
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# import libraries
import time
start = time.time()
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI #ext
import base64
import requests #ext
import re
import os



#banner function
def banner():
	print "                                                             "    	
	print "                                                             " 
	print "  _________    ___.        ___________                       "
	print " /   _____/__ _\_ |__      \_   _____/ ____  __ __  _____    "
	print " \_____  \|  |  \ __ \      |    __)_ /    \|  |  \/     \   "
	print " /        \  |  / \_\ \     |        \   |  \  |  /  Y Y  \""
	print "/_______  /____/|___  / /\ /_______  /___|  /____/|__|_|  /  "
	print "        \/          \/  \/         \/     \/            \/   "
	print "                        V-1.0                                "
	print "-------------------------------------------------------------"
	print "  SubEnum is a Automation-tool which enumerates subdomains   "
	print "       using Google,bing,yahoo,baidu, dnsdumpster.           "
	print "    Useful for BUGBOUNTY - INFORMATION GATHERING - OSINT     "
	print " Written By p5yph3r.Kindly share your Suggestions and Feedback"
	print " [+] you can find me here :- psypher1918@gmail.com 			"
	print "-------------------------------------------------------------"

# function for google search
def google(target):
	try:
		link = 'https://www.google.com/search?client=ubuntu&channel=fs&q=site%3A'+ target +'+-inurl%3Awww&ie=utf-8&oe=utf-8'
		request = requests.get(link)
		response =  request.text
		print "[+] Enumerating Subdomains From Google Search \n"
		name = re.findall('<cite>(.*?)</cite>', response)
		print "[*] Results :-"
		for i in range(len(name)):
			subds =  [str(name[i])]
			print subds
		print " [-] Enumeration Completed \n"
	except:
		print "Some Error Occured :("	

# function for Bing search
def bing(target):
	try:
		link = 'https://www.bing.com/search?q=site%3A+'+target+'+-inurl%3Awww&qs=n&form=QBLH&sp=-1&pq=site%3A+'+target+'+-inurl%3Awww&sc=1-30&sk=&cvid=8947285B97814EA6A012D8241B3DAD07'
		request = requests.get(link)
		response =  request.text
		print "[+] Enumerating Subdomains From Bing Search \n"
		name = re.findall('<cite>(.*?)</cite>', response)
		print "[*] Results :-"
		for i in range(len(name)):
			subds =  [str(name[i])]
			print subds
		print " [-] Enumeration Completed \n"
	except:
		print "Some Error Occured :("	

# function for Yahoo search
def yahoo(target):
	try:
		link = 'https://in.search.yahoo.com/search?p=site%3A'+target+'+-inurl%3Awww&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8'
		request = requests.get(link)
		response =  request.text
		print "[+] Enumerating Subdomains From Yahoo Search \n"
		name = re.findall('<span class=" fz-ms fw-m fc-12th wr-bw">(.*?)</span>', response)
		print "[*] Results :-"
		for i in range(len(name)):
			subds =  [str(name[i])]
			print subds
		print " [-] Enumeration Completed \n"
	except:
		print "Some Error Occured :("

# function for Baidu search
def baidu(target):
	try:
		link = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=site%3A'+target+'%20-inurl%3Awww'
		request = requests.get(link)
		response =  request.text
		print "[+] Enumerating Subdomains From Baidu Search \n"
		name = re.findall('style="text-decoration:none;">(.*?)</a>', response)
		print "[*] Results :-"
		for i in range(len(name)):
			subds =  [str(name[i])]
			print subds
		print " [-] Enumeration Completed \n"
	except:
		print "Some Error Occured :("

# function for DNS-Dumpster. Using the API.
def dumpster(target):
	try:
		domain = target
		print("\n\n\n[+] DNS Dumpster Enumeration Started ")
		print("[+] This takes some time but its worth it.")
		res = DNSDumpsterAPI(True).search(domain)
		for entry in res['dns_records']['host']:
			if entry['reverse_dns']:
				print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
			else:
				print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
		print " [+] Dns-Dumpster Enumeration Completed \n"
	except:
		print "Some Error Occured :("

def main():
	banner()
	target = raw_input(" Enter the Parent Domain (Example : test.com or google.com)\n DOMAIN > ") 
	google(target)                                                                                                                                                                                      
	bing(target)
	yahoo(target)
	baidu(target)
	dumpster(target)
	end = time.time()
	time_taken = str(end - start)
	print "*********************stats******************************************"
	print "Subdomain Enemeration completed on "+target+" Time taken = "+ time_taken
	print "---------------------------------------------------------------------"
	
if __name__ == "__main__":
	main()
