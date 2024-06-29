import os
import fileinput
import yaml
import sys
import pandas as pd

def generic_files_rename(tenantid,i):
    print(os.getcwd())
    dest = os.path.join('.','folder',f"tenant1-{i}.yaml")
    newname=os.path.join('.','folder', tenantid + '-' + i + '.yaml')
    try:
        os.rename(dest,newname) # changing file name
        file = fileinput.FileInput(newname,inplace=True) # 
        for line in file:
            a=line.replace("tenant1",tenantid)
            print(a,end='')
        fileinput.close()
    except FileNotFoundError:
        print ("files are not present", dest)
    except FileExistsError:
        print ("file already exists there",dest,sep=":")
inputs=sys.argv
tenantid = inputs[1].split("/")[1]
print(tenantid)
for i in ['con','rep','top','rbac']:
    generic_files_rename(tenantid,i)
