import os
import random
import pandas as pd


def generate_test_data(directory, num_files, num_rows, num_columns):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_files):
        file_name = f"test_data_{i}.csv"
        file_path = os.path.join(directory, file_name)

        header = [f"col_{j}" for j in range(num_columns)]
        data = [[random.random() for _ in range(num_columns)] for _ in range(num_rows)]
        df = pd.DataFrame(data, columns=header)
        df.to_csv(file_path, index=False)


if __name__=='__main__':
    from simplecsvdataset.whereami import TESTDATA
    generate_test_data(directory=TESTDATA, num_files=10, num_rows=100, num_columns=5)
