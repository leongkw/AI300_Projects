import pandas as pd
from loguru import logger

class DataLoader:
    def __init__(self, path: str):
        self.path = path

    def load_data(self, type: str = 'csv') -> pd.DataFrame:
        '''
        Function that takes in a csv/xlsx file and returns a pandas dataframe.

        Arguments:
        1. type
        - csv: takes in csv file
        - xlsx: takes in excel file
        '''
        if type == 'csv':
            return pd.read_csv(self.path)
        elif type == 'xlsx':
            return pd.read_excel(self.path)
        else:
            logger.error("Unknown file type specific. Please specify either 'csv' or 'xlsx' as file type.")


        