import os
import fileinput
import yaml
import sys
import pandas as pd

def generic_files_rename(tenantid,i):
    dest="/folder/hellomot-"+ i +".yaml"
    newname="/folder/"+ tenantid + "-"+i +".yaml"
    try:
        os.rename(dest,newname) # changing file name
        file = fileinput.FileInput(newname,inplace=True) # 
        for line in file:
            a=line.replace("hellomot",tenantid)
            print(a,end='')
        fileinput.close()
    except FileNotFoundError:
        print ("files are not present", dest)
    except FileExistsError:
        print ("file already exists there",dest,sep=":")
tenant=sys.argv
for i in ['con','rep','top','rbac']:
    generic_files_rename(tenant[1],i)