#import Model as m
#
# @Author Ahmed ALJeferi
#
class task4:
    def __init__(self,Document,data,record):

        self.data = data
        #self.record =m.Record()
        self.record = record
        self.readers = []
        self.ReadersOfDox = {}
        #self.readersWithDox = {}
        #loop to get all the peaple how read that document
        for r in self.data:
            self.record = r
            if self.record.subject_doc_id == Document: #check the document
               if  self.record.__getuser__() not in self.readers:
                  self.readers.append(self.record.__getuser__()) # get the reader and add to the list of readers
        #loop to get the documents of the readers
        for reader in self.readers:
            #loop in all the data
            for r in self.data:
                tempList = []
                self.record = r
                if reader == self.record.visitor_ID:#check the id of the rader
                    #if self.record.subject_doc_id != Document:
                        #######################
                        if self.record.subject_doc_id in self.ReadersOfDox:
                            if reader not in self.ReadersOfDox[self.record.subject_doc_id]:
                                self.ReadersOfDox[self.record.subject_doc_id].append(reader)
                        else:
                            tempList.append(reader)
                            self.ReadersOfDox.setdefault(self.record.subject_doc_id, tempList)


# Main was used for testing the class
if __name__ == "__main__":
    t = task4('140310171202-000000002e5a8ff1f577548fec708d50')
    for k,v in t.ReadersOfDox.items():
      #if len(v)> 1:
        print('Dox Number: '+k[-4:]+': '+str(len(v)))
        print('---------------------------------')
        for d in v:
            print(d[-4:])


            #if self.record.subject_doc_id not in tempList:
             #            tempList.append(self.record.subject_doc_id)
              #          if self.record.subject_doc_id not in self.DoxOfReaders:
               #          self.DoxOfReaders.setdefault(self.record.subject_doc_id,1)
                #        else:
                 #        self.DoxOfReaders[self.record.subject_doc_id] += 1
            #self.readersWithDox.setdefault(reader,tempList)