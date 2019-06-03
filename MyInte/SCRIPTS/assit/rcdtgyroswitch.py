#iNE=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']
iNE=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_DEN_METHOD0']
iTE=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']
iTI=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']
iER=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']
root['SETTINGS']['PHYSICS']['tgyroswitch']=array([iNE,iTE,iTI,iER])

