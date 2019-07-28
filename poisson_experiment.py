import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

initial = 10
range_to = 100
poi_num = list()
poi_all = list()
r_v = 0

for j in range(range_to):
    poi_num = list()
    for i in range(initial):
        if i > 1:
            r_v = np.random.poisson(r_v)
        else:
            r_v = np.random.poisson(initial)

        poi_num.append(r_v)
    poi_all.append(poi_num)

poi_all = [np.mean(i) for i in poi_all]
  
sns.lineplot(range(0,range_to), poi_all)
plt.title("Number of Walkers over Time")
plt.xlabel("Iterations")
plt.ylabel("Number of Walkers")

np.mean(poi_all)