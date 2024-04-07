import pyneb as pn 
import numpy as np
# declare all the metals:
O3 = pn.Atom('O', 3) 
Fe2 = pn.Atom('Fe', 2) 
Fe3 = pn.Atom('Fe', 3) 
Mg5 = pn.Atom('Mg', 5) 
Ar2 = pn.Atom('Ar', 2) 
Ar3 = pn.Atom('Ar', 3)
# Si5 = pn.Atom('SI', 5) 
Ne2 = pn.Atom('Ne', 2) 
Ne3 = pn.Atom('Ne', 3)
n2 = pn.Atom('N', 2)
Cl2 = pn.Atom('Cl', 2) #lambda = 14.5 
# H2S = pn.Atom('H2S', 1) 
s3 = pn.Atom('S', 3)
s2 = pn.Atom('S', 2)
# redshift
# Mg5_real = Mg5.getTransition(55635.9)
rs = 56066.77 / 55635.9 -1 # 0.007744459962002903


# deduce the electron densities in the region given temperature 
tem = 10000
# use the ratio between SIII at 18 and 33 micrometer to determine the electron density
# ratio = 112.2/145
# correction for redshift 
wave_1 = 188900 / (1 + rs)
wave_2 = 337900 / (1 + rs)

# num =0
# while num < 40000: 
#     num += 1000
#     print('num =', num)
#     print(s3.getTemDen(0.77379, tem = num, wave1 = 187078.08, wave2 = 334703.72))

den = 300  # 214.07
obs = pn.Observation()
obs.readData('/Users/vivian/Desktop/Undergrad Study/Y2 Physics/Extra Project/Code/Observation_arm1.dat', fileFormat='lines_in_rows', err_default=0.05)
obs.printIntens(returnObs=True)
# redden correction
obs.def_EBV(label1 = "H1pfa_7.529",label2 = "Ar2_7.0m", r_theo = 0.22734 )		
obs.correctData(normWave=70000)

all_atoms = pn.getAtomDict(atom_list=obs.getUniqueAtoms())
ab_dict = {}
ab_labels = ['Mg5_5.6m', 'Ar2_7.0m', 'Ar3_9.0m', 'Ne2_12.8m', 'Ne3_15.6m', 's3_18.7m', 'Cl2_14.4m']
# 'Fe2_18.05m',, 'Fe3_23.4m'

# nucleus abundance 
for line in obs.getSortedLines():
    if line.label in ab_labels:
        ab_dict[line.label] = all_atoms[line.atom].getIonAbundance(line.corrIntens, tem, den, 
                                                  to_eval=line.to_eval, Hbeta=100)
for line in sorted(ab_dict):
    print('{:10} {:.2f}'.format(line, 12+np.log10(ab_dict[line][0])))


print(ab_dict)

