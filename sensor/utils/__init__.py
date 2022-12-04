import pandas as pandas
from sensor.config import mongoclient

def get_collection_as_dataframe(database_name:str,collection_name:str) ->pd.dateFrame:

    try:
        logging.info("Reading data from database: {database_name} and collection:{collection_name}")
        df = pd.dateFrame(list(mongoclient[database_name][collection_name].find()))
        logging.info(f"Found colmns :{df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df=df.dr("_id",axis=1)
        logging.info(f"Row and col")
        return df
    except Exception as e:
        raise SensorException(e,sys)
