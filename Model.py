import json
#
# @Author Ahmed ALJeferi
#

class model:
    """ a class that get all the data from the json file and store it in an array to be dealed with later on  """

    def __init__(self,fileName):
        """
        once it start it will read all the data in the file to store in one array of recored objects
        """

        self.allRecoreds = []
        self.country = {}

        try:
         with open(fileName) as file:    #open the json file
            i=0
            for line in file: # loop thru the lines
                i+=1
                print("new line "+str(i))
                data = json.loads(line) #load each line as json type
                if 'event_type' in data: #check in the recored the event type if there and it has the type read
                  if data['event_type'] =='read':
                   if 'subject_type' in data : #check in the record the subject type and check if its of type doc or not
                     if data['subject_type']=='doc':
                      if 'visitor_useragent' in data:#the record should has user agent information
                        if 'visitor_username' in data:#check if the user has user name or not.If the user has we use it but if not we use uuid
                          visitor_ID = data['visitor_username'] #Storing the information in temp variables
                        else:
                          visitor_ID = data['visitor_uuid']
                        visitor_Agent = data['visitor_useragent']
                        visitor_country = data['visitor_country']
                        subject_doc_id = data['subject_doc_id']
                        r = Record() #create new object of record class
                        r.__setData___(visitor_ID,visitor_Agent,visitor_country,subject_doc_id)#assinge the data we got form the json file to it and add the object to a list of all our data
                        self.allRecoreds.append(r)
         file.close()
        except IOError:
            self.allRecoreds = None
        try:
         allcountryFile = open("allCountry.json",  "r",encoding="utf-8-sig")
         allcountryData = json.load(allcountryFile)
         allcountryFile.close()
        except:
            allcountryData = None
        if allcountryData != None:
         for c in allcountryData:
           self.country.setdefault(c['alpha-2'],c['region']) #Get all the country information from another json file. only store the short name and the region to be used in task 2a & 2b
    def __getRecoreds__(self):
        return self.allRecoreds
    def __getCountr__(self):
        return self.country

class Record:
    """ Each row in the json file stored in the array of all recored as an object of the class recored
    this class has the most importent data we need in the json to meet the assinment reqirments
    """
    def __init__(self):
        pass
    def __setData___(self,visitor_ID,visitor_Agent,visitor_country,subject_doc_id):
        self.visitor_ID = str (visitor_ID)
        self.visitor_Agent = str(visitor_Agent)
        self.visitor_country = str (visitor_country)
        self.subject_doc_id = str(subject_doc_id)

    def __getBroweser__(self):
        return self.visitor_Agent
    def __getuser__(self):
        return self.visitor_ID
    def __getCountry__(self):
        return self.visitor_country
    def __getDocId__(self):
        return self.subject_doc_id

#class user not used yet -------------------------------------
class user:

    dox = []
    def __init__(self):
        global dox
        pass
    def ___setUser__(self,visitor_ID ):
        self.visitor_ID = str (visitor_ID)
    def __setDox__(self,subject_doc_id):
        #global dox
        self.dox.append(subject_doc_id)
    def __getDox__(self):
        return dox
