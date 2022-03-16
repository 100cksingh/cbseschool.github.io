# 
# Example file for parsing and processing JSON

from itertools import count
import urllib.request
import json
def printResults(data):
    theJSON=json.loads(data)
    
    if"title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    count=theJSON["metadata"]["count"]
    print(str(count)+"events recorded ")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("---------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"]>=4.0:
            print("%2.1lf"%i["properties"]["mag"],i["properties"]["place"])
    print("---------\n")


    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports=i["properties"]["felt"]
        if feltReports!=None:
            if feltReports>0:
                print("%2.1f"%i["properties"]["mag"],i["properties"]["place"],
                "reported"+str(feltReports)+"times")


  


def main():
    # This feed lists all earthquakes for the last day larger than Mag 2.5

    urlData="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
    webUrl=urllib.request.urlopen(urlData)
    print("result code:"+str(webUrl.getcode()))
    if(webUrl.getcode()==200):
        data=webUrl.read()
        printResults(data)
    else:
        print("Received error,can not parse results")



if __name__=="__main__":
    main()

