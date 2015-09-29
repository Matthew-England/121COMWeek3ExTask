# Contains function to fecth data from the Quandl API

def readJsonUrl(url):
    """This reads the contents of a URL.  Works for json data and Python 3"""
    #####################################################################
    # In this block of code:
    # - Python opens the url
    # - reads the data
    # - stores it as a string
    # - closes the url
    import urllib.request
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("There was an error opening the URL (description below).")
        print(e)
        print("Ask for help?")
        return(None)
    data_bytes = page.read()
    data_str = data_bytes.decode('utf-8')
    page.close()
    #####################################################################
    # In this block of code
    # - The json string is converted to a Python dictionary.
    # - This is returned
    import json
    try:
        output = json.loads(data_str)
    except:
        print("Error")
        return(None)
    return(output)    
    #####################################################################


def GetFromQuandl(dCode, tCode, out="data", printInfo=True, printData=False, authCode="0"):
    """This function fetches data from the Quandl API.

    Mandatory arguments:
    dCode (string) -- A Quandl database code
    tCode (string) -- A Quandl table code
    
    Keyword arguments:
    out (string) --- Default is "data".  Can also use "dict" if the full dictionary of information is desired.
    printInfo (boolean) --- whether to print some basic information
    printData (boolean) --- whether to print full data set.
    authCode (string) --- a Quandl authorisation code.
    """

    # Define the API url:
    if authCode=="0":
        myURL = "https://www.quandl.com/api/v1/datasets/%s/%s.json"%(dCode,tCode)
    else:
        myURL = "https://www.quandl.com/api/v1/datasets/%s/%s.json?auth_token=%s"%(dCode,tCode,authCode)

    output = readJsonUrl(myURL)
    if output==None:
        return(None)

    #################################################################
    ### This block checks for a Quandl API error ####################
    if ("errors" in output):
        if output["errors"]!={}:
            print("The API reported errors:")
            print(output["errors"])
            print("Check the database and table codes are valid")
            return(None)
    elif ("error" in output):
        if output["error"]!={}:
            print("The API reported an error:")
            print(output["error"])
            print("Check the database and table codes are valid")
            return(None)
    #################################################################

    # Actual data stored here
    dataAPI = output["data"]

    #################################################################
    ### The following prints out key information on retrieved data ##
    if printInfo:
        print("Data name: " + output["name"])
        print("Source: " + output["source_name"])
        print("Data at: " + output["display_url"])
        print("Columns: " + str(output["column_names"]))
    if printData:
        print(" ")
        for d in dataAPI:
            print(d)
    #################################################################

    if out=="data":
        return(dataAPI)
    else:
        return(output)
