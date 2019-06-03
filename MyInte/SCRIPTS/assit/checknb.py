# this script is mainly used to check the NB state, mainly 2 aspects:
# (1) how much power shine through
# (2) how much power are outside rho~0.8
iview=root['SETTINGS']['PLOTS']['iview']
dataOutput=root['OUTPUTSRec']['ONETWOOutput'][iview]
pshine_through_MW= sum(dataOutput['dnubeam_nbi_fld_state.cdf']['pinja']['data']-dataOutput['dnubeam_nbi_fld_state.cdf']['pinjs_res']['data'])/1.e6
print('shine_through_MW=',pshine_through_MW)
Pow_e=OMFIT['MyInte']['OUTPUTSRec']['ProfileGenOutput'][iview]['pow_e']
Pow_i=OMFIT['MyInte']['OUTPUTSRec']['ProfileGenOutput'][iview]['pow_i']
#nj=root['SETTINGS']['PHYSICS']['nj']
nj=len(Pow_e)
outrho=root['SETTINGS']['PLOTS']['outrho']
indout=floor((nj-1)*outrho)
Pow_e_out=max(Pow_e)-Pow_e[indout]
Pow_i_out=max(Pow_i)-Pow_i[indout]
pow_out=Pow_e_out+Pow_i_out
print( 'power outside r/a= %.2f is %.2f MW'%(outrho,pow_out))
