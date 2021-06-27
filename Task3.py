import json
import Model as m
import tkinter as tkint

#
# @Author Ahmed ALJeferi
#



class browser:
    def __init__(self,Document,data,record):
          self.broLst = {}
          self.task3ALst = {}
          self.allData = data
          for line in self.allData:
                r = record
                r = line
                if r.__getDocId__() == Document:
                  temp = str(r.__getBroweser__())
                  if temp in self.task3ALst:
                      self.task3ALst[temp] += 1
                  else:
                      self.task3ALst.setdefault(temp,1)
                  temp3 =temp.split('/')
                  if len(temp3)>1:
                   temp2 = temp3[0]
                   temp4 = temp3[-2]
#I had a probelm with this user in 3M lines file:6267334cd0839f22 need to check what is the problem -----Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)
                   if temp2 == 'Mozilla':
                      if 'Safari' in temp4:
                       temp5 = temp2+' Safari'
                      elif 'Firefox' in temp4:
                        temp5 = temp2+' Firefox'
                      else:
                          temp5 = temp2
                   else:
                      temp5 = temp2
                  else:
                      temp5 = temp
                  if temp5 in self.broLst:
                      self.broLst[temp5] += 1
                  else:
                      self.broLst.setdefault(temp5,1)


# Main was used for testing the class
#if __name__ == "__main__":

 #   browser( m.model('issuu_cw22.json'))
  #  for k ,v in broLst.items():
   #     print(k+':'+str(v))