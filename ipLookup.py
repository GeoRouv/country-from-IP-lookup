#!/usr/bin/env python3

import argparse
import requests

## Argument Parser
parser = argparse.ArgumentParser(description='Process some args')
parser.add_argument('ip',type = str, help = 'Name of the ip address')
args = parser.parse_args()

def main():
    URL = "http://www.geoplugin.net/json.gp?ip=" + args.ip 
    
    res = requests.get(URL)
    data =res.json()
        
    print("\nLocation of ip address: " + data["geoplugin_countryName"] + "\n")
 
if __name__== "__main__":
    main()




