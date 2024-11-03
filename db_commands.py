import os
import time
import random
class db:
    def __init__(self):
        self.root = ""
    def insert_into_table(self,table_name:str,values:list,fields:list = None):
        with open(""+table_name+".csv","r") as f:
            tbl_fields = f.readline().replace("\n","").split(",")[1::]
            new_index = str(int(time.time()))+"."+str(random.randint(1,10000))
            if (values):
                for i in range(len(values)):
                    values[i] = str(values[i])
            if (fields!=None):
                assert len(fields)==len(tbl_fields),"Number of fields and table fields are not equal"
                assert (len(list(set(fields)-set(tbl_fields)))==0),"One or multiple of the fields is not present in table"
                assert len(fields)==len(values),"Number of fields and values are not equal"
                assert len(list(set(fields)))==len(fields),"Duplicate fields"
            else:assert len(values)==len(tbl_fields),"Number of fields and values are not equal"
            real_values = []
            if (fields==None):real_values = values
            else:
                for i in tbl_fields:
                    real_values.append(values[tbl_fields.index(i)])
            with open(table_name+".csv","a") as f:
                f.write("\n"+str(new_index)+","+",".join(real_values))
                print("Values Inserted")
                return new_index
    def get_data(self,table_name:str):
        with open(table_name+".csv","r") as f:
            raw_data = f.readlines()
            tbl_fields = raw_data[0][:-1:].split(",")[0::]
            parsed_data = []
            for i in raw_data[1::]:
                i = i.replace("\n","").split(",")
                temp = {}
                for j in range(len(tbl_fields)):
                    temp[tbl_fields[j]] = i[j]
                parsed_data.append(temp)
            return parsed_data