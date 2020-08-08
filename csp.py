import requests
import sys, argparse
import bcolors
import os

def banner():
    print("""
                ░█████╗░░██████╗██████╗░░░░░░░░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
                ██╔══██╗██╔════╝██╔══██╗░░░░░░██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
                ██║░░╚═╝╚█████╗░██████╔╝█████╗╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
                ██║░░██╗░╚═══██╗██╔═══╝░╚════╝░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
                ╚█████╔╝██████╔╝██║░░░░░░░░░░░██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
                ░╚════╝░╚═════╝░╚═╝░░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝                                                                         
                                                                                         Code by NG          
              """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-u'):
        try:
            input_url = sys.argv[2]
            input_location = sys.argv[2]
            if(os.path.exists(input_location) == True):
                  file = open(input_location,'r')
                  line = file.readlines()
                  for text in line:
                      lines = text.rstrip()
                      parser = argparse.ArgumentParser()
                      parser.add_argument("-u", required=True)
                      args = parser.parse_args()
                      input_header = requests.get(lines)
                      h_text = input_header.headers['content-security-policy']

                      print(bcolors.BITALIC + '\n''\n' + "Testing for Content Security Policy")
                      print('------------------------------------------------------------------------------------------------------------')
                      try:
                          print(bcolors.OKMSG + 'Content Security Policy for:' + lines, '\n' '\n' + h_text)
                      except:
                          print("CSP not possible for the given URL")
            else:
                 parser = argparse.ArgumentParser()
                 parser.add_argument("-u", required=True)
                 args = parser.parse_args()
                 print(bcolors.BITALIC + "Testing for Content Security Policy")
                 input_header = requests.get(input_url)
                 h_text = input_header.headers['content-security-policy']
                 try:
                      print(bcolors.OKMSG + 'Content Security Policy for:' + input_url ,'\n' '\n' + h_text)
                 except:
                      print("CSP not possible for the given URL")

        except:
            print('Please enter python CSP.py -u <URL>')
            print("Give Domain with http:// or https://")

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: CSP.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u Url,   --url Url')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from -u or -h, with a valid url')





