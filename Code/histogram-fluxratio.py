import matplotlib.pyplot as plt
import numpy as np



# x1 = [0.66247591,0.296680581,0.569666123, 18.44647335, 1.653057124, 1.06353104, 130.330156, 1.254325066, 12.62078562, 1.702509841, 3.1256855, 49.08937354, 4.892143075, 0]
# x2 = [1.17404608,0.194881146,0.666352908, 6.137229559, 2.847316662, 4.354874965, 95.49227311, 1.036139365, 15.79665636, 12.1835066, 2.157645406, 62.61168868, 6.897752178, 7.887552683]
# x3 = [0.677047901, 0.243907574, 0.719561469, 17.25455139, 1.525202839, 1.209872398, 156.2557857, 1.639899806, 12.99847531, 3.117337956, 3.2026664, 86.31432305, 6.798985352, 0]



x1 = [0.66247591, 0.296680581, 0.569666123, 18.44647335, 1.653057124, 1.06353104, 130.330156, 1.254325066, 12.62078562, 1.702509841, 3.1256855, 49.08937354, 4.892143075, 0]
x3 = [0.31091591, 0.05160926, 0.17646643, 1.625287408, 0.754038589, 1.153276633, 25.2886726, 0.274394863, 4.18333817, 3.226488381, 0.571396894, 16.58109546, 1.826692264, 2.088815471]
x2 = [0.555105625, 0.199977677, 0.589962125, 14.14685507, 1.250500406, 0.991963748, 128.1127456, 1.344539441, 10.65733568, 2.555877998, 2.62583804, 70.76835502, 5.574428347, 0 ]

x1 = np.log(x1)
x2 = np.log(x2)
x3 = np.log(x3)
barWidth = 0.25
br1 = np.arange(len(x1)) 
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, x1, color ='r', width = barWidth, 
        edgecolor ='grey', label ='IT') 
plt.bar(br2, x2, color ='g', width = barWidth, 
        edgecolor ='grey', label ='ECE') 
plt.bar(br3, x3, color ='r', width = barWidth, 
        edgecolor ='grey', label ='ECE') 


xlable = ['Fe II', 'Mg V', 'H2 S(5)', 'Ar II', 'Ar III', 'H2 S(2)', 'Ne II', 'Clorine','Ne III','H2 S(1)','Fe II','S III','Fe III','Fe II']

plt.xticks([r + barWidth for r in range(len(x1))], 
        xlable)
plt.title("log scale")
plt.show()