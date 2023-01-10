import pandas as pd
import pandasql as ps
from pandasql import *
import plotly
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import glob
import warnings

warnings.simplefilter("ignore")

folder_path = 'volatility/sample_folder/'
path = + 'sample_input.csv' # Path to your CSV file
df = pd.read_csv(path)

df['log_returns_ul_c2c'] = ''
df['log_returns_ul_c2o'] = ''

for i in range(1, len(df)):
    df['log_returns_ul_c2c'][i] = np.log(df['close_ul'][i] / df['close_ul'][i - 1])
    df['log_returns_ul_c2o'][i] = np.log(df['open_ul'][i] / df['close_ul'][i - 1])

df['log_returns_ul_c2c'] = pd.to_numeric(df['log_returns_ul_c2c'], errors='coerce')
df['log_returns_ul_c2o'] = pd.to_numeric(df['log_returns_ul_c2o'], errors='coerce')

df['vol_c2c_20d'] = ''
df['vol_c2o_20d'] = ''
for i in range(19, len(df)):
    sum_squared_log_returns_c2c = 0
    sum_squared_log_returns_c2o = 0
    for j in range(1, 20):
        sum_squared_log_returns_c2c += (df['log_returns_ul_c2c'][i - 19 + j])**2
        sum_squared_log_returns_c2o += (df['log_returns_ul_c2o'][i - 19 + j])**2
        df['vol_c2c_20d'][i] = (sum_squared_log_returns_c2c / 20)**0.5 * 256**0.5
        df['vol_c2o_20d'][i] = (sum_squared_log_returns_c2o / 20)**0.5 * 256**0.5
df['vol_c2c_20d'] = pd.to_numeric(df['vol_c2c_20d'], errors='coerce')
df['vol_c2o_20d'] = pd.to_numeric(df['vol_c2o_20d'], errors='coerce')
print(underlying, "20d")

df['vol_c2c_40d'] = ''
df['vol_c2o_40d'] = ''
for i in range(39, len(df)):
    sum_squared_log_returns_c2c = 0
    sum_squared_log_returns_c2o = 0
    for j in range(1, 40):
        sum_squared_log_returns_c2c += (df['log_returns_ul_c2c'][i - 39 + j])**2
        sum_squared_log_returns_c2o += (df['log_returns_ul_c2o'][i - 39 + j])**2
        df['vol_c2c_40d'][i] = (sum_squared_log_returns_c2c / 40)**0.5 * 256**0.5
        df['vol_c2o_40d'][i] = (sum_squared_log_returns_c2o / 40)**0.5 * 256**0.5
df['vol_c2c_40d'] = pd.to_numeric(df['vol_c2c_40d'], errors='coerce')
df['vol_c2o_40d'] = pd.to_numeric(df['vol_c2o_40d'], errors='coerce')
print(underlying, "40d")

df['vol_c2c_60d'] = ''
df['vol_c2o_60d'] = ''
for i in range(59, len(df)):
    sum_squared_log_returns_c2c = 0
    sum_squared_log_returns_c2o = 0
    for j in range(1, 60):
        sum_squared_log_returns_c2c += (df['log_returns_ul_c2c'][i - 59 + j])**2
        sum_squared_log_returns_c2o += (df['log_returns_ul_c2o'][i - 59 + j])**2
        df['vol_c2c_60d'][i] = (sum_squared_log_returns_c2c / 60)**0.5 * 256**0.5
        df['vol_c2o_60d'][i] = (sum_squared_log_returns_c2o / 60)**0.5 * 256**0.5
df['vol_c2c_60d'] = pd.to_numeric(df['vol_c2c_60d'], errors='coerce')
df['vol_c2o_60d'] = pd.to_numeric(df['vol_c2o_60d'], errors='coerce')
print(underlying, "60d")

df['vol_c2c_80d'] = ''
df['vol_c2o_80d'] = ''
for i in range(79, len(df)):
    sum_squared_log_returns_c2c = 0
    sum_squared_log_returns_c2o = 0
    for j in range(1, 80):
        sum_squared_log_returns_c2c += (df['log_returns_ul_c2c'][i - 79 + j])**2
        sum_squared_log_returns_c2o += (df['log_returns_ul_c2o'][i - 79 + j])**2
        df['vol_c2c_80d'][i] = (sum_squared_log_returns_c2c / 80)**0.5 * 256**0.5
        df['vol_c2o_80d'][i] = (sum_squared_log_returns_c2o / 80)**0.5 * 256**0.5
df['vol_c2c_80d'] = pd.to_numeric(df['vol_c2c_80d'], errors='coerce')
df['vol_c2o_80d'] = pd.to_numeric(df['vol_c2o_80d'], errors='coerce')
print(underlying, "80d")

df['vol_parkinson'] = ''
for i in range(19, len(df)):
    sum_squared_log_returns = 0
    for j in range(0, 19):
        sum_squared_log_returns += (np.log(df['high_ul'][i - 19 + j] / df['low_ul'][i - 19 + j]))**2
        df['vol_parkinson'][i] = (sum_squared_log_returns / (4 * 20 * np.log(2)))**0.5 * 256**0.5
df['vol_parkinson'] = pd.to_numeric(df['vol_parkinson'], errors='coerce')
print(underlying, "parkinson")

df.to_csv(folder_path + '/sample_output.csv', index=False)