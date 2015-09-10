these_times = times[times.team == team]
ax[index].plot(these_times.time.as_matrix(),
         np.ones(len(these_times)), 'o')
