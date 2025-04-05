import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

def plot (file, title):

    df = pd.read_csv(file)

    zero_min = []
    one_min = []
    two_min = []
    three_min = []
    four_min = []

    metric = title

    for i in range(len(df["duration"])):
        if df["duration"].iloc[i] == 0:
            zero_min.append(float(df["ones"].iloc[i]))
        elif df["duration"].iloc[i] == 1:
            one_min.append(float(df["ones"].iloc[i]))
        elif df["duration"].iloc[i] == 2:
            two_min.append(float(df["ones"].iloc[i]))
        elif df["duration"].iloc[i] == 3:
            three_min.append(float(df["ones"].iloc[i]))
        else:
            four_min.append(float(df["ones"].iloc[i]))



    zero_min_np = np.array(zero_min)
    one_min_np = np.array(one_min)
    two_min_np = np.array(two_min)
    three_min_np = np.array(three_min)
    four_min_np = np.array(four_min)

    categories = ["0 min", "1 min", "2 mins", "3 mins", "4 mins"]
    means = [np.mean(zero_min_np), np.mean(one_min_np), np.mean(two_min_np), np.mean(three_min_np), np.mean(four_min_np)]
    sds = [np.std(zero_min_np), np.std(one_min_np), np.std(two_min_np), np.std(three_min_np), np.std(four_min_np)]

    plt.bar(categories, means, yerr=sds,capsize=5)
    plt.xlabel('Minutes')
    plt.ylabel(metric)
    plt.title(title)
    plt.savefig(title + ".png")
    plt.show()


def plot_cat(file, title):
    d = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4: 0}

    df = pd.read_csv(file)

    for i in range(len(df["url"])):
        duration = int(df["duration"].iloc[i])
        d[duration] += 1

    plt.bar(d.keys(), d.values())
    plt.xlabel('Minutes')
    plt.ylabel("Number of samples")
    plt.suptitle( "Number of samples", fontsize=15)
    plt.title('Not all videos could be redownloaded for measuring saturation metric ' + title, fontsize=8)
    plt.savefig(title + ".png")
    plt.show()


#plot("color_10_frames_without_brand0to258.csv", "Mean sat score without brand keywords")


#plot_cat("brand_search.csv", "with brand keywords")

def linear_regression(x, y):
    reg = LinearRegression()
    reg.fit(x, y)
    return reg.score(x, y)

def get_r_sq(file, func):
    df = pd.read_csv(file)
    predictor = df["duration"].to_numpy()
    predictor_reshaped = predictor.reshape(predictor.shape[0], -1)
    predicted = df["ones"]
    return func(predictor_reshaped, predicted)

print(get_r_sq("brand_search.csv", func=linear_regression)) #xor with linear regression
print(get_r_sq("generic_search_updated.csv", func=linear_regression)) #xor with linear regression

print(get_r_sq("color_10_frames_with_brand_all.csv", func=linear_regression)) #sat score with linear regression
print(get_r_sq("color_10_frames_without_brand0to258.csv", func=linear_regression)) #sat score with linear regression