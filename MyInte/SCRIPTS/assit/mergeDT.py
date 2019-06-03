# this script is used to merge the density of DT thus we can account the impurities effect on the confinment
root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ni_1']+root['INPUTS']['TGYROInput']['input.profiles']['ni_2']
root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ni_3']
root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ni_4']
#root['INPUTS']['TGYROInput']['input.tgyro']['LOC_N_ION']=3
# note when the impurities species changes this should also change
Mass=root['SETTINGS']['PHYSICS']['MassForMerge']
Charge=root['SETTINGS']['PHYSICS']['ChargeForMerge']
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_MA1']=Mass[0]
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_Z']=Charge[0]
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_MA2']=Mass[1]
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_Z2']=Charge[1]
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_MA3']=Mass[2]
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_Z3']=Charge[2]
