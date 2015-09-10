import matplotlib.pyplot as plt

these_times = times[times.team == team]
plt.plot(these_times.time.as_matrix(),
         np.ones(len(these_times)), 'o')
plt.set_ylabel(team, rotation='horizontal',
               labelpad=30)
plt.set_ybound(0.5, 1.5)
plt.set_position([0.1, 0.1, 8.0, 1.0])
plt.set_yticks([])
