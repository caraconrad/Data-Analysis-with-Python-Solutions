import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(.975))]


def draw_line_plot():
    # Draw line plot
    plot = df.plot.line(figsize = (25,8), fontsize = 18, color = {'value' : 'red'})
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize = 20)
    plt.xlabel('Date', fontsize = 20)
    plt.ylabel('Page Views', fontsize = 20)
    fig = plot.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df.index.year), (df.index.month)]).mean()

    # Draw bar plot
    fig = df_bar.unstack().plot(kind = 'bar', figsize = (12,10.5), fontsize = 18).figure
    plt.legend(title = "Months", title_fontsize = 15, labels=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"), fontsize = 15)
    plt.xlabel("Years", fontsize = 15)
    plt.ylabel("Average Page Views", fontsize = 15)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(7)    
    ax1 = sns.boxplot(x="year", y="value", data=df_box, ax = ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")    
    ax2 = sns.boxplot(x="month", y="value", data=df_box, ax = ax2, order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")        

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig