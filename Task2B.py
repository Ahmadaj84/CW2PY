import Task2A as T2A
import matplotlib.pyplot as plt
#
# @Author Ahmed ALJeferi
#

class Task2b:
    def __init__(self,allConData,targetedCountry):
        self.continint = {}
        #self.t2a = T2A.Task2a("140226060548-b66f7db7a94f69d0c1c995f0e65bddd6")
        self.allConData = allConData
        self.targetedCountry = targetedCountry
        for k ,v  in self.targetedCountry.items():
            for k2 ,v2 in self.allConData.items():
                if k2 == k:
                    if k2 in self.continint:
                        self.continint[v2] += v
                    else:
                        self.continint.setdefault(v2,v)

# Main was used for testing the class
if __name__ == "__main__":
    t =Task2b()
    for k,v in t.continint.items():
     print(k,str(v))
    fig, ax = plt.subplots()
    ax.barh(list(t.continint.keys()),list(t.continint.values()))
    plt.show()




