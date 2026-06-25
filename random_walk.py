import numpy as np
import matplotlib.pyplot as plt
def random_walk(n):
  s=0
  position=[0]
  X=np.random.choice([-1,1],n)
  for i in X:
      s=s+i
      position.append(s)
  return position
for i in range(20):
   Trajectoire = random_walk(500)
   plt.plot(Trajectoire,linewidth=1)
plt.xlabel("temps")
plt.ylabel("position")
plt.title("Simulation d'une marche aléatoire")
plt.grid()
plt.savefig("random_walks.png")
plt.show()
dernier_position=[]
for i in range(10000):
   Trajectoire = random_walk(500)
   dernier_position.append(Trajectoire[-1])
plt.hist(dernier_position,bins=30)
plt.xlabel("Position finale")
plt.ylabel("Fréquence")
plt.title("Distribution des positions finales")
plt.grid()
plt.savefig("final_distribution.png")
plt.show()
