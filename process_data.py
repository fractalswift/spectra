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

            # just take the first character of the column
            # since naming convetino is 1_01, 1_02 etc we want just "1"
            spectra.append(col[0])

    # remove duplicates
    spectra = set(spectra)

    # now put them in a dict
    spec_dict = {}

    # Make a key for each SET so 1, 2, 3, 4, 5
    for col in spectra:

        # spec_dict[col] = []
        spec_dict[col] = pd.DataFrame()

    print(f"spec dict cols: ", spec_dict.keys())

    # Now put each Y under the correct key, e.g 1_01 and 1_02 both go in set key 1
    for col in df.columns:

        if col != "x":

            # spec_dict[col[0]].append(df[col])

            spec_dict[col[0]][col] = df[col]

    # TODO write a test - we expect there to be 5 columns for each set key

    for k, v in spec_dict.items():
        print(f"set {k} has {len(v.columns)} columns in it")

        print(f"each column of {k} has {len(v)} rows in it")

        print(f"the type of data is {type(v)}")

    # calculate the averages

    avg_df = pd.DataFrame()

    # print(avg_df.columns)

    for k, v in spec_dict.items():

        # take the average of each set df and put the column into the avg df

        avg_df[k] = v.mean(axis=1)

        # avg_df[k] = sum(v) / len(v)

    # # add the x column back in
    avg_df["x"] = df["x"]

    # sort the columns numerically - its just upsetting to look at otherwise
    avg_df = avg_df.reindex(sorted(avg_df.columns), axis=1)

    print(avg_df.head())

    return avg_df


def plot_set_averages(tuple):
    """Accept  tuple of (name, df) and save a png of the plot of x / sets"""

    name, df = tuple
    avg_df = calculate_avgs(df)

    x = avg_df["x"]

    avgs = avg_df.drop(["x"], axis=1)

    for col in avgs.columns:

        plt.plot(x, avgs[col], label=col)

        plt.title(f"Scan {col}")
        plt.xlabel("Wavenumbers")
        plt.ylabel("Signal Intensity")
        plt.savefig(f"./graph_output/{name}-SET-{col}.png")

        plt.close()


def plot_big_average(tuple):
    """Accept  tuple of (name, df) and save a png of the plot of x / (average of all sets)"""

    name = tuple[0]
    df = tuple[1]
    df = calculate_avgs(df)

    x = df["x"]
    just_avgs = df.drop(["x"], 1)

    all_avgs = just_avgs.mean(axis=1)

    plt.plot(x, all_avgs, label="Average")

    plt.title("Composite Spectrum")
    plt.xlabel("Wavenumbers")
    plt.ylabel("Signal Intensity")
    plt.savefig(f"./graph_output/{name}-ALL_SETS_AVG.png")

    plt.close()


if __name__ == "__main__":

    try:

        paths = get_paths()

        data_sets = [import_and_clean(
            f"./data_input/{path}") for path in paths]

        dfs_with_name = [(data_set[0], pd.DataFrame(data_set[1]))
                         for data_set in data_sets]

        for tuple in dfs_with_name:

            plot_big_average(tuple)
            plot_set_averages(tuple)

        print("Hello K-tyn, your new graphs are in graph_output/")
        print("Have a nice day :)")

    except Exception as e:

        print("Hello K-tyn, there was a problem making your graphs :(")
        print(f"The error message is: {str(e)}")
