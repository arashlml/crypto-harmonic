# harmonic_backtester/visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_returns(df_results: pd.DataFrame):
    sns.histplot(df_results["return"], kde=True)
    plt.title("Distribution of Harmonic Pattern Returns")
    plt.xlabel("Return")
    plt.ylabel("Count")
    plt.show()

def plot_patterns(df_signals: pd.DataFrame, df_results: pd.DataFrame):
    df = pd.concat([df_signals, df_results], axis=1)
    sns.boxplot(x="pattern_name", y="return", data=df)
    plt.xticks(rotation=45)
    plt.title("Pattern Performance Comparison")
    plt.show()
