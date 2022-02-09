
import pandas as pd
import csv
# read csv file as a list of lists

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    df = pd.read_csv(csv_file_path)
    return df.values.tolist()

