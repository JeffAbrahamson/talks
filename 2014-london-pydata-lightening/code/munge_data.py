#!/usr/bin/python3

"""Analyze time data from the Journée Nationale du Huit, 16 Nov 2014, Nantes."""

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def get_data():
    """Read the data.

    It has been prepared with the shell script get-data."""
    # Read the data.
    df = pd.read_csv('resultats-clean-final.txt', delimiter='\t', header=None, names=['index','boat','category','club','captain','time','offset'])

    # Make time and offset be proper dateime.time values.
    df.time = pd.Series([datetime.time(0, int(val[:2]), int(val[3:5]), int(val[6:])*100000)
                         for val in df.time], index = df.index)
    df.offset = pd.Series([datetime.time(0, int(val[:2]), int(val[3:5]), int(val[6:])*100000)
                           for val in df.offset], index = df.index)
    return df

def filename(entity, zero):
    """Create a descriptive filename.

    Entity is club or category.
    Zero is True if origin is at 0, False if left edge of plot is at min."""
    if zero:
        origin = ''
    else:
        origin = '-zero'
    return 'jn8-{0}{1}.png'.format(entity, origin)
    
def plot_by_club(df, live):
    """Plot a histogram of number of boats entered by club."""
    # Histogram of club representation.
    df.club.value_counts().plot(kind='bar')
    plt.xlabel("Participation par club")
    render_plot(8, 6, live, 'jn8-clubs.png')

def plot_by_category(df, live):
    """Plot a histogram of number of boats entered by category type."""
    # Histogram of category representation.
    df.category.value_counts().plot(kind='bar')
    plt.xlabel("Participation par type d'équipe")
    render_plot(8, 6, live, 'jn8-categories.png')

def plot_times_by_club(df, live, zero):
    """Plot the times for each club.

    If zero is True, then set first x-tick at 0 seconds (beginning of race)."""
    times = df.loc[:, ['time', 'club']]
    clubs = times.club.unique()
    fig, ax = plt.subplots(len(clubs), sharex=True, sharey=True)
    for index, club in enumerate(clubs):
        these_times = times[times.club == club]
        ax[index].plot(these_times.time.as_matrix(), np.ones(len(these_times)), 'o')
        ax[index].set_ylabel(club, rotation='horizontal', labelpad=30)
        ax[index].set_yticks([])
        ax[index].set_ybound(0.5, 1.5)
        ax[index].set_position([0.1, 0.1, 8.0, 1.0])
        ax[index].set_yticks([])
    ax[0].set_title('Temps, vu par club')
    min_tick = ax[0].get_xticks().min()
    if zero:
        min_tick = 0.0
        ax[0].set_xbound(lower=0.0)
    max_tick = ax[0].get_xticks().max()
    ax[0].set_xticks(np.linspace(min_tick, max_tick, 6))
    fig.subplots_adjust(hspace=0)
    render_plot(8, 6, live, filename('club', zero))

def plot_times_by_category(df, live, zero):
    """Plot the times for each category.

    If zero is True, then set first x-tick at 0 seconds (beginning of
    race).

    This is almost identical to plot_times_by_club.  They should be the
    same function."""
    times = df.loc[:, ['time', 'category', 'club']]
    categories = times.category.unique()
    fig, ax = plt.subplots(len(categories), sharex=True, sharey=True)
    for index, category in enumerate(categories):
        others_times = times[(times.category == category) & (times.club != 'UNA')]
        our_times = times[(times.category == category) & (times.club == 'UNA')]
        ax[index].plot(others_times.time.as_matrix(), np.ones(len(others_times)), 'bo')
        ax[index].plot(our_times.time.as_matrix(), np.ones(len(our_times)), 'ro')
        ax[index].set_ylabel(category, rotation='horizontal', labelpad=30)
        ax[index].set_yticks([])
        ax[index].set_ybound(0.5, 1.5)
        ax[index].set_position([0.1, 0.1, 8.0, 1.0])
        ax[index].set_yticks([])
    ax[0].set_title('Temps, vu par catégorie (UNA=rouge)')
    min_tick = ax[0].get_xticks().min()
    if zero:
        min_tick = 0.0
        ax[0].set_xbound(lower=0.0)
    max_tick = ax[0].get_xticks().max()
    ax[0].set_xticks(np.linspace(min_tick, max_tick, 6))
    fig.subplots_adjust(hspace=0)
    render_plot(8, 6, live, filename('category', zero))

def render_plot(xdim, ydim, live, filename):
    """Display or save the plot image.

    If live is True, then display in a window.
    If live is False, save to the named file."""
    if live:
        plt.show()
    else:
        gc = plt.gcf()
        gc.set_size_inches(xdim, ydim)
        gc.savefig(filename, dpi=100)

def main():
    """Fetch data and make some plots."""
    if len(sys.argv) > 1 and sys.argv[1] == 'live':
        live = True
    else:
        live = False
    df = get_data()
    plot_by_club(df, live)
    plot_by_category(df, live)
    plot_times_by_club(df, live, True) 
    plot_times_by_club(df, live, False) 
    plot_times_by_category(df, live, True) 
    plot_times_by_category(df, live, False) 

if __name__ == "__main__":
    main()
