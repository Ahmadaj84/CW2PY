import os
import shutil

path = r'C:\Users\ahmoo\Desktop'
to = r'C:\Users\ahmoo\Documents\test'

arr = []
toArry =[]
for root, dirs, files in os.walk(path):
        for f in files:
            arr.append(root + r"\\" + f)




def listToString (l):
	str1 = "\\"
	return (str1.join(l))
#create list with the distinations
for originalFile in arr:
    toArry.append(to+"\\"+listToString(originalFile.split("\\")[4:]))
#TEst the list is the same
for i in range(len(arr)):
    print (arr[i])
    print (toArry[i])

#Trying to copy 50 file
for i in range(50):
    try:
    shutil.copy(arr[i], toArry[i])
    print("File copied successfully.")

# If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

# If there is any permission issue
    except PermissionError:
    print("Permission denied.")

# For other errors
except:
    print("Error occurred while copying file.")
