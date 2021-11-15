import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine


def compute_similarity(data):
    for column in data.columns:
        similarity = 1 - cosine(data["c1"], data[column])
        print(f"The cosine similarity of c1 with {column} is {similarity}")


def tf_idf(data: pd.DataFrame):
    for index, row in data.iterrows():
        t = 0
        for elem in row:
            if elem != 0:
                t += 1

        idf = np.log(row.shape[0]/t)
        data.loc[index] = data.loc[index] * idf

    return data


if __name__ == '__main__':
    data = pd.read_excel("./data/memo.xlsx", index_col=0)
    print(data)

    print("----- Without TF-IDF -----")
    compute_similarity(data)

    print("\n----- With TF-IDF -----")
    tf_idf_data = tf_idf(data)
    compute_similarity(tf_idf_data)
