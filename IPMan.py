import ipinfo
import sys
import json
import time
import pandas
from pyfiglet import Figlet

#Initial Banner and other text
custom_fig = Figlet(font='cyberlarge')
print(custom_fig.renderText("IPMan"))

print("\n")


print("Welcome to IPMan bulk IP Checker. Your output will be saved to files called 'WingChun' if you haven't provided an output filename")

print("\n")

#Deciding on filenames based on command line parameters
if(len(sys.argv)==1):
    print("Please enter input file name\n")
    exit()
elif(len(sys.argv)==2):
    filename = sys.argv[1]
    outfile = "wingchun.json"
    csv_filename = "wingchun.csv"
elif(len(sys.argv)==3):
    filename = sys.argv[1]
    outfile = sys.argv[2]


else:
    print("Too many parameters")

if('.txt' in filename):
    print("\n")
else:
    filename = filename + '.txt'

if('.json' in outfile):
    setting = 1
elif('.csv' in outfile):
    setting = 2
    csv_filename = outfile
else:
    setting = 3
    csv_filename = outfile+'.csv'
    outfile = outfile+'.json'



#API Access token settings
access_token = 'eb97eb6d5140fc'
handler = ipinfo.getHandler(access_token)

#Data Structure Declaration
ip = []
city = []
region = []
country = []
loc = []
org = []
postal = []
timezone = []
country_name = []
latitude = []
longitude = []
output_list = []

#IP Checker Function
def IPMan(filename):

    #Add File Name/Path here
    hand = open(filename,'r')
    
    iplist = []

    for i in hand:
        val = str(i).replace('\n','')
        if(val in iplist):
            continue
        else:
            iplist.append(val)



    print("Total Number of Unique IPs:",len(iplist),'\n')


    for ip_address in iplist: 

        
        try:
            details = handler.getDetails(ip_address)
            
        except:
            print("Error! >.<")


        print(details.all,'\n')


        output_list.append(dict(details.all))

    print('\n')

    
    if(setting==1):   
        #Writing to output JSON File
        JsonOutput(output_list)
    elif(setting==2):
        #Writing to output CSV File
        CsvOutput(output_list)
    else:
        JsonOutput(output_list)
        CsvOutput(output_list)



    

    print('Done')
    print("Greet what arrives, escort what leaves and rush upon loss of contact -IP Man\n")


def JsonOutput(output_list):
    with open(outfile, 'w') as fp:
                json.dump(output_list, fp,indent=4)

def CsvOutput(output_list):        
    y = json.dumps(output_list)
    x = pandas.read_json(y)
    x.to_csv(csv_filename)


#Function Call
IPMan(filename)


