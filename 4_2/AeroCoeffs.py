import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "LLT_polar.txt",
    delim_whitespace=True,
    comment="#"
)


print(df.head())
print(df.columns)