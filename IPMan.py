import ipinfo
import sys
import json
import time
from pyfiglet import Figlet

#Initial Banner and other text
custom_fig = Figlet(font='cyberlarge')
print(custom_fig.renderText("IPMan"))

print("\n")


print("Welcome to IPMan bulk IP Checker. Your output will be saved to a file called 'WingChun.jpg if you haven't provided an output filename")

print("\n")

#Deciding on filenames based on command line parameters
if(len(sys.argv)==1):
    print("Please enter input file name\n")
    exit()
elif(len(sys.argv)==2):
    filename = sys.argv[1]
    outfile = "wingchun.json"
elif(len(sys.argv)==3):
    filename = sys.argv[1]
    outfile = sys.argv[2]
else:
    print("Too many parameters")


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


        #Code used to append data to list to make it feasible to paste directly into excel
        if('city' in details.all.keys()):
            ip.append(details.all['ip'])
            city.append(details.all['city'])
            region.append(details.all['region'])
            country.append(details.all['country'])
            loc.append(details.all['loc'])
            if('org' in details.all.keys()):
                org.append(details.all['org'])
            else:
                org.append('Unknown')
                
            if('postal' in details.all.keys()):
                postal.append(details.all['postal'])
            else:
                postal.append('Unknown')    
            
            timezone.append(details.all['timezone'])
            country_name.append(details.all['country_name'])
            latitude.append(details.all['latitude'])
            longitude.append(details.all['longitude'])
    print('\n')

    #Writing to output file
    with open(outfile, 'w') as fp:
            json.dump(output_list, fp,indent=4)
    print('Done')
    print("Greet what arrives, escort what leaves and rush upon loss of contact -IP Man\n")



#Function Call
IPMan(filename)


#Display data in format that can be copy pasted to excel column wise


# for z in ip:
#     print(z)
    
# for z in city:
#     print(z)
    
# for z in region:
#     print(z)
    
# for z in country:
#     print(z)
    
# for z in loc:
#     print(z)

# for z in org:
#     print(z)  
    
# for z in postal:
#     print(z)
    
# for z in timezone:
#     print(z)
    
# for z in country_name:
#     print(z)
    
# for z in latitude:
#     print(z)
    
# for z in longitude:
#     print(z)

