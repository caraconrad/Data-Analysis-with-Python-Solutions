import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df.apply(lambda row: int(row['weight']/((row['height']*.01)**2) > 25), axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize_cholesterol(row):
    if row['cholesterol'] == 1:
        return 0
    elif row['cholesterol'] > 1:
        return 1

def normalize_gluc(row):
    if row['gluc'] == 1:
        return 0
    elif row['gluc'] > 1:
        return 1

df['cholesterol'] = df.apply(lambda row: normalize_cholesterol(row), axis=1)
df['gluc'] = df.apply(lambda row: normalize_gluc(row), axis=1)   


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    #sns.catplot(x='cardio', data = df_cat, kind = 'count')
    plot = sns.catplot(data=df_cat, x='variable', col='cardio', kind='count', hue='value')
    plot.set(ylabel='total')
    fig = plot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(.975)) & (df['weight'] >= df['weight'].quantile(.025)) & (df['weight'] <= df['weight'].quantile(.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()   

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(14, 14))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=1.0, cmap="icefire",                square=True, center=0, vmax=.3, vmin=-.15,  cbar_kws={"shrink": .4, "ticks": [-.08, 0, .08, .16, .24]}, annot_kws={"size": 12})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
