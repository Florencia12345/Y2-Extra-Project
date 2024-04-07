import pyneb as pn 
O3 = pn.Atom('O', 3)
N2 = pn.Atom('N', 2)
S2 = pn.Atom('S', 2)

O3.getEnergy(4, unit='eV')
print(O3.getEnergy(4, unit='eV'))

density = S2.getTemDen(1.1, tem = 1e4, wave1=6730, wave2 = 6716)

print("density:", density)

# onic abundance determination
# The ionic abundance is obtained from the intensity of a line normalized to Hbeta=100.
abun = S2.getIonAbundance(int_ratio=72, tem=1.5e4, den=100., to_eval='L(6716)+L(6731)')
print("abundance:", abun)

Opp_abund = O3.getIonAbundance(int_ratio=3239.4, tem=1.5e4, den=110., to_eval='L(5007)+L(4959)', Hbeta=100.0)
print('O++/O = {:5.2e}'.format(Opp_abund))

atom_abun = {'O2': 0.001, 'O3': 0.002, 'Ne3': 1.2e-5}
icf = pn.ICF()
print(icf.getAvailableICFs('Ne'))   # lists all the available recipes for Ne

elem_abun = icf.getElemAbundance(atom_abun, icf_list=['TPP77_15']) # Computes the Ne abundance with the TPP06 recipe
print(elem_abun)
#what are these 

elem_abun2 = icf.getElemAbundance(atom_abun, icf_list=['Ial06_19b']) 
print(elem_abun2)

