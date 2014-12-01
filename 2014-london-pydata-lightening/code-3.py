import matplotlib.pyplot as plt

these_times = times[times.team == team]
ax[index].plot(these_times.time.as_matrix(),
         np.ones(len(these_times)), 'o')
ax[index].set_ylabel(team, rotation='horizontal',
               labelpad=30)
ax[index].set_ybound(0.5, 1.5)
ax[index].set_position([0.1, 0.1, 8.0, 1.0])
ax[index].set_yticks([])
