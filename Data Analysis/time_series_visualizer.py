import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('data/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
# Clean data
df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12,4))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    sns.lineplot(data=df, x='date', y='value')
    # Save image and return fig (don't change this part)
    fig.savefig('output/line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot.bar(xlabel='Years', ylabel='Average Page Views', figsize=(10,5), legend=True).figure
    plt.legend(months).figure
    # Save image and return fig (don't change this part)
    fig.savefig('output/bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_id'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_id')
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(12,4))
    ax[0] = sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax[1] = sns.boxplot(data=df_box, x='month', y='value', ax=ax[1])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('output/box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()