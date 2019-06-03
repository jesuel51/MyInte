# Since sometimes the density profile in the core region maybe quite peaked, which may result in high BS current in core region and thus bad confinement property.
#(1) useiniNe.py: here we use the initial density to represent the density profile but with sparse grid
if root['SETTINGS']['PHYSICS']['useiniNe'][0]==1:
    pvt_i=root['SETTINGS']['PHYSICS']['useiniNe'][1]
    drho_tgyro=root['SETTINGS']['PHYSICS']['drho_tgyro']
    num=int(pvt_i/drho_tgyro)+1
    diff_Ne=root['SETTINGS']['PHYSICS']['NEIN'][num]-root['SETTINGS']['PHYSICS']['Ne_TGYRO'][num]
#    diff_Te=root['SETTINGS']['PHYSICS']['TEIN'][num]-root['SETTINGS']['PHYSICS']['TEIN_TGYRO'][num]
    root['SETTINGS']['PHYSICS']['Ne_TGYRO'][0:num]=root['SETTINGS']['PHYSICS']['NEIN'][0:num]-diff_Ne
#    root['SETTINGS']['PHYSICS']['TEIN_TGYRO'][0:num]=root['SETTINGS']['PHYSICS']['TEIN'][0:num]-diff_Te
