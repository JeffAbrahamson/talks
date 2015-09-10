others_times = times[(times.category == category)
                     & (times.club != 'UNA')]
our_times = times[(times.category == category)
                  & (times.club == 'UNA')]
ax[index].plot(others_times.time.as_matrix(),
               np.ones(len(others_times)), 'bo')
ax[index].plot(our_times.time.as_matrix(),
               np.ones(len(our_times)), 'ro')
