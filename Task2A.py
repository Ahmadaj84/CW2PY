import Model as m
import matplotlib.pyplot as plt
#
# @Author Ahmed ALJeferi
#

class Task2a:
  def __init__(self,document,data,record):
    self.country = {}
    #self.modl = data
    self.rcords = data
    self.singleRecored = record
    for r in self.rcords:
     singleRecored = r
     if singleRecored.__getDocId__() == document:
         if singleRecored.__getCountry__() in self.country:
             self.country[singleRecored.__getCountry__()] += 1
         else:
             self.country.setdefault(singleRecored.__getCountry__(),1)


# Main was used for testing the class
if __name__ == "__main__":
    t =Task2a("130226190856-562231ddfb624e0db190c5ac82b72ad1")
    for k,v in t.country.items():
     print(k,str(v))
    fig, ax = plt.subplots()
    ax.barh(list(t.country.keys()),list(t.country.values()))
    plt.show()