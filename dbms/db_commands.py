import os
import time
import random
class db:
    def __init__(self):
        self.root = ""
        print(self.root)

    def create_table(self, table_name:str,fields:list):	
        with open(table_name+".csv","w") as f:
            f.write("id,"+",".join(fields))
            print("Table Created")

    def drop_table(self, table_name:str):
        os.remove(table_name+".csv")
        print("Table Dropped")

    def insert_into_table(self,table_name:str,values:list,fields:list = None):
        with open("dbms/"+table_name+".csv","r") as f:
            tbl_fields = f.readline().replace("\n","").split(",")[1::]
            new_index = str(int(time.time()))+"."+str(random.randint(1,10000))
            if (values):
                for i in range(len(values)):
                    values[i] = str(values[i])
            if (fields!=None):
                pass
                print(tbl_fields)
                pass
                pass
                pass
            else:pass
            real_values = []
            if (fields==None):real_values = values
            else:
                for i in tbl_fields:
                    real_values.append(values[tbl_fields.index(i)])
            with open(table_name+".csv","a") as f:
                f.write("\n"+str(new_index)+","+",".join(real_values))
                print("Values Inserted")
                return new_index
    def get_data(self,table_name:str,fields:list = []):
        with open("dbms/"+table_name+".csv","r") as f:
            raw_data = f.readlines()
            tbl_fields = raw_data[0][:-1:].split(",")[0::]
            if (len(fields)!=0):
                pass
                pass
            else:
                fields = tbl_fields
            if ("id" not in fields):fields = ["id"]+fields
            parsed_data = []
            for i in raw_data[1::]:
                i = i.replace("\n","").split(",")
                temp = {}
                for j in range(len(fields)):
                    temp[fields[j]] = i[tbl_fields.index(fields[j])]
                parsed_data.append(temp)
            return parsed_data
    def delete_item(self,table_name:str,id:str):
        with open(table_name+".csv","r") as f:
            raw_data = f.readlines()
            flag = False
            for i in range(len(raw_data)-1):
                if (raw_data[i+1].split(",")[0]==id):
                    with open(table_name+".csv","w") as f2:
                        f2.write("".join(raw_data[:i+1:]+raw_data[i+2::]))
                    flag = True
                    break
            if (flag==False):print("Item not found")
            else:print("Item deleted")
            
