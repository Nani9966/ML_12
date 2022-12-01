import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE= "API"
COLLECTION_TABEL="SENSOR"
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"row and columns:{df.shape}")
    

    # converting data to json formate

    df.reset_index(drop=True,inplace =True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    ##droping in MOnodb

    client[DATABASE][COLLECTION_TABEL].insert_many(json_record)