# a1 and a2 are hand-crafted, copied from some randome web page with numbers on it.

b1 = ss.norm.rvs(5, 3, size=300)
b2 = ss.norm.rvs(5, 4, size=300)
b3 = ss.norm.rvs(5.1, 3, size=300)

c1 = ss.norm.rvs(loc=5, scale=3, size=300)
c2 = np.array([ss.norm.rvs(loc=2, scale=1, size=150), ss.norm.rvs(loc=8, scale=1, size=150)]).reshape(300)
