teams = times.team.unique()     # ['time', 'team']
fig, ax = plt.subplots(len(teams),
                       sharex=True, sharey=True)
for index, team in enumerate(teams):
    these_times = times[times.team == team]
    # and do what was on the previous slide
ax[0].set_title('Time by team')
min_tick = ax[0].get_xticks().min()
max_tick = ax[0].get_xticks().max()
ax[0].set_xticks(np.linspace(min_tick,
                             max_tick, 6))
fig.subplots_adjust(hspace=0)

