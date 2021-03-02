import random
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
import numpy as np
nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum()
walk.min()
walk.max()
(np.abs(walk) >= 10).argmax() #When does the walker cross 10 in either direction
#multiple simulations
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps)) # 0 or 1
steps = np.where(draws > 0,1,-1)
walks = steps.cumsum(1)
walks
walks.max()
walks.min()
hits30 = (np.abs(walks) >=30).any(1) #of all 5000 walks which ones hit 30?
hits30
hits30.sum() #number of walks that hit 30 out of 5000
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
