from typing import Collection
import pandas as pd
import json
import os
from matplotlib import pyplot as plt


def get_paths():
    """Get file name of all data in data_input folder"""

    paths = os.listdir('data_input')

    return filter(lambda x: x != ".gitignore", paths)


def import_and_clean(path):
    """Import the json data and drop the metadata array and the raw arrays"""

    with open(path) as json_file:
        data = json.load(json_file)

    clean_data = {}

    for k, v in data.items():

        if "metadata" not in k and "raw" not in k:
            clean_data[k] = v

    name = path.split("/")[-1]

    name = name.split(".")[0]

    return (name, clean_data)


def calculate_avgs(df):
    """Accept a dataframe and return it with average sets only"""

    # work out how many spectra there are from the column names:

    spectra = []

    for col in df.columns:

        if col != "x":

            spectra.append(col[0])

    spectra = set(spectra)

    # now put them in a dict

    spec_dict = {}

    for col in spectra:

        spec_dict[col] = []

    for col in df.columns:

        if col != "x":

            spec_dict[col[0]].append(df[col])

    # finally, calculate the averages and return a new df

    avg_df = pd.DataFrame()

    for k, v in spec_dict.items():

        avg_df[k] = sum(v) / len(v)

    return avg_df


if __name__ == "__main__":

    try:

        paths = get_paths()

        data_sets = [import_and_clean(
            f"./data_input/{path}") for path in paths]

        dfs_with_name = [(data_set[0], pd.DataFrame(data_set[1]))
                         for data_set in data_sets]

        for tuple in dfs_with_name:

            name, df = tuple
            avg_df = calculate_avgs(df)

            plt.plot(avg_df)
            plt.savefig(f"./graph_output/{name}.png")

        print("Hello K-tyn, your new graphs are in graph_output/")
        print("Have a nice day :)")

    except Exception:

        print("Hello K-tyn, there was a problem making your graphs :(")
