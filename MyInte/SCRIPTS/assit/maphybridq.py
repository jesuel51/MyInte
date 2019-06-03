# this script is used to take the core q profile of AUG hybrid mode to be the q profile of the present q profile
tgyroinput=root['INPUTS']['TGYROInput']
physics=root['SETTINGS']['PHYSICS']
if tgyroinput.has_key('input.profiles_hybrid') and physics['iusehybridq'][0]==1:
# eg. physics['iusehybridq']=array([1,0.3,0.4,6])
    rho=tgyroinput['input.profiles_hybrid']['rho']
    q_input=abs(tgyroinput['input.profiles']['q'])
    q_hybrid=abs(tgyroinput['input.profiles_hybrid']['q'])
    rho_pivot_hybrid=physics['iusehybridq'][1]
    rho_pivot_input=physics['iusehybridq'][2]
    n_hybrid_sparse=physics['iusehybridq'][3]
    rho_sparse=linspace(0,rho_pivot_hybrid,n_hybrid_sparse)
#ne_12_ped=interp(rho_ped,r_12,ne_old)
    q_sparse=interp(rho_sparse,rho,q_hybrid)  # the hybrid q profile in sparse form
    ind_pivot_input=int(rho_pivot_input*len(rho))
    rho_mix=concatenate((rho_sparse,rho[ind_pivot_input:]))
    q_mix=concatenate((q_sparse,q_input[ind_pivot_input:]))
    q_update=interp(rho,rho_mix,q_mix)
    # give back to the input.profiles
    tgyroinput['input.profiles']['q']=q_update
