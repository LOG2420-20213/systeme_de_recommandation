import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine


if __name__ == '__main__':
    data = pd.read_excel("./data/memo.xlsx", index_col=0)
    print(data)
