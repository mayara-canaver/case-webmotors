import pandas as pd
import os
import numpy as np

from pandas.api.types import is_string_dtype

pd.options.display.max_columns = None

# os.chdir("../data_folder")
dataset = pd.read_csv("../datasets/Case 1 - dados.csv", sep=",")
