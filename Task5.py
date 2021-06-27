

#
# @Author Ahmed ALJeferi
#
import os


class task5:
  def __init__(self,targetDox,userID,readersOfDox , readers,filename ):
    self.targetDoc = targetDox
    self.userid = userID
    self.readersOfDox = readersOfDox
    self.readers = readers

    dotFileText = """

         digraph also_likes {
               ranksep=.75; ratio=compress; size = "15,22"; orientation=landscape; rotate=180;
             {
          node [shape=plaintext, fontsize=16];
           Readers -> Documents
              [label=\"Size: """+filename+"""\" ];"""
    lableAndShape = ''
    for k,v in self.readersOfDox.items():
      if k == self.targetDoc:
        lableAndShape += '\"'+k[-4:]+'\" [label=\"'+k[-4:]+'\",shape=\"circle\",style=filled,color=\".3 .9 .7\"];'
      else:
       lableAndShape += '\"'+k[-4:]+'\" [label=\"'+k[-4:]+'\",shape=\"circle\"];'


    for r in  self.readers:
      if r == self.userid:
       lableAndShape += '\"'+r[-4:]+'\" [label=\"'+r[-4:]+'\",shape=\"box\",style=filled,color=\".3 .9 .7\"];'
      else:
        lableAndShape += '\"'+r[-4:]+'\" [label=\"'+r[-4:]+'\",shape=\"box\"];'
    lableAndShape += '{ rank = same; \"Readers\";'
    for r in  self.readers:
      lableAndShape += '\"'+r[-4:]+'\" ;'
    lableAndShape += '};{ rank = same; \"Documents\";'
    for k,v in self.readersOfDox.items():
       lableAndShape += '\"'+k[-4:]+'\";'
    lableAndShape += '};'
    for k,v in self.readersOfDox.items():
      for re in v:
         lableAndShape += '\"'+re[-4:]+'\"' + '->'+'\"'+k[-4:]+'\";'
    lableAndShape += '};}'


    dotFileText += lableAndShape
    try:
     outputFileName = filename+'_'+targetDox[-4:]
     outputFileNames =outputFileName +'.dot'
     file = open(outputFileNames,'w')
     file.write(dotFileText)
    # print (dotFileText)
     file.close()
     comand = 'dot -Tpdf -o' + outputFileName + '.pdf '+outputFileName+'.dot'
     os.system(comand)
     comand2 = 'dot -Tps -o' + outputFileName + '.ps '+outputFileName+'.dot'
     os.system(comand2)
     comand3 = 'evince '+outputFileName+'.pdf'
     os.system(comand3)

    except:
        print('cant create a dot file')




