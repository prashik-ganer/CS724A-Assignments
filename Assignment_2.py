import numpy as np
import matplotlib.pyplot as p
import math
import statistics as s

# TASK 1
RSSI=[-32,-33,-38,-41,-34,-38,-43,-39,-47,-50,-48,-57,-45,-37,-42,-46,-52,-56,-44,-53,-46,-51]
d=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4]
Distances=[math.log10(i) for i in d]
coeff= np.polyfit(Distances,RSSI,1)
linearfn = np.poly1d(coeff)
predicted_RSSI = linearfn(Distances)
slope = coeff[0]
intercept = coeff[1]
PathLossExponent=abs(slope/10)
print(slope,"   ",intercept)
p.scatter(Distances,RSSI, label='Data Points')
p.plot(Distances, predicted_RSSI, color='red', label='Best-Fit Line')
Var=np.var(RSSI-predicted_RSSI)
# Var=s.variance(RSSI-predicted_RSSI)
print(Var)
# Add labels and a legend
p.xlabel('Distances')
p.ylabel('RSSI')
p.legend()
# Show the plot
p.show()

#TASK2
RSSI_5=[-38,-47,-45,-42,-53]
Distances_5=[2,2,3,3,4]
predicted_Distances=[((intercept-RSSI_5[i])/(10*PathLossExponent)) for i in range(5)]
for i in range(5):
    predicted_Distances[i]=pow(10,predicted_Distances[i])
# for i in range(5):
#     Distances_5[i]=math.log10(Distances_5[i])
error=[abs(Distances_5[i]-predicted_Distances[i]) for i in range(5)]
avg_error=np.mean(error)
print("The average error is - ",avg_error)
