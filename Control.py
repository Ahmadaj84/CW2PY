import Model as m
import Task2A as t2a
import Task2B as t2b
import Task3 as t3
import Task4 as t4
import Task5 as t5


#
# @Author Ahmed ALJeferi
#

class control:
    def __init__(self,file):
        mm = m.model(file)
        self.data = mm.__getRecoreds__()
        if self.data != None:
         self.record = m.Record()
         self.countries = mm.country
         self.file = file
        else:
           print('problem with file path')

    def startTask2A(self,Document):
        if self.data !=None:
            self.t2 = t2a.Task2a(Document,self.data,self.record)
            self.countriesResult = self.t2.country

        else:
            return False
    def startTask2B(self,Document):
        self.startTask2A(Document)
        if self.data!= None:
            self.t2B = t2b.Task2b(self.countries,self.countriesResult)
            self.continit = self.t2B.continint
        else:
            return False
    def startTask3a(self,Document):
        if self.data !=None:
            self.t33 = t3.browser(Document,self.data,self.record)
            self.broser = self.t33.task3ALst
        else:
            return False
    def startTask3b(self,Document):
        if self.data !=None:
            self.t33 = t3.browser(Document,self.data,self.record)
            self.broserMainName = self.t33.broLst
        else:
            return False


    def startTask4(self,Document):#the class of task 4 start without accessing the model class only ture the controler
        if self.data != None:
         t =t4.task4(Document,self.data,self.record)
         self.ReadersOfdox = t.ReadersOfDox # data passed from the task for class to the controler so it can pass it to the view class
         self.usersThatRead = t.readers
        else:
            return False
    def startTask5(self,Docuemnt,user):
        if self.data !=None:
            self.startTask4(Docuemnt)
            filename = self.file.split('_')
            if len(filename) > 0:
             tt5 = t5.task5(Docuemnt,user,self.ReadersOfdox,self.usersThatRead,filename[1])
            else:
                tt5 = t5.task5(Docuemnt,user,self.ReadersOfdox,self.usersThatRead,filename)






if __name__ == "__main__":
    c = control('sample_200k_lines.json') #issuu_cw22 sample_400k_lines
    if c.startTask4("140310170010-0000000067dc80801f1df696ae52862b") != False:

      for k,v in c.ReadersOfdox.items():
         print('Dox Number: '+k[-4:]+': '+str(len(v)))
         print('---------------------------------')
         print('Readers :')
         for d in v:
            print(d[-4:])

    if c.startTask2A("140310170010-0000000067dc80801f1df696ae52862b") !=False:
         for k,v in c.countriesResult.items():
             print(k,str(v))

    if c.startTask2B("140310170010-0000000067dc80801f1df696ae52862b") != False:
        for k,v in c.continit.items():
            print(k,v)
    c.startTask5("100806162735-00000000115598650cb8b514246272b5",'00000000deadbeef')
