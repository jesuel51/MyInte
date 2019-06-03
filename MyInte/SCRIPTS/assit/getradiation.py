# this script is sued to calculate the radiation power in the existence of W
# the W density profile is kept in the OMFIT['MyInte']['SETTINGS']['DEPENDENCIES']['W']
# first we need to keep the previous inone file which will be recoverred later
ONETWOInput=root['INPUTS']['ONETWOInput']
ONETWOInput['inone_bak']=ONETWOInput['inone'].duplicate()
iternum=root['SETTINGS']['TEMP']['iternum']
#ONETWOInput['inone_bak']=ONETWOInput['inone'].deepcopy()
# then we can do some changing according to in the inone file
# it's a good news to know that onetwo can handle 5 ion species when NB is not running
# turn of the nubeam
ONETWOInput['inone']['NAMELIS2']['use_nubeam']=False
if ONETWOInput['inone']['NAMELIS2'].has_key('beam_data_namelist'):
    del ONETWOInput['inone']['NAMELIS2']['beam_data_namelist']
# change the densities of ion species
ONETWOInput['inone']['NAMELIS1']['NAMEP']=array(['dt','he'])
ONETWOInput['inone']['NAMELIS1']['NAMEI']=array(['w','ar'])
ONETWOInput['inone']['NAMELIS1']['enp'].T[0]=ONETWOInput['inone']['NAMELIS1']['enp'].T[0]+ONETWOInput['inone']['NAMELIS1']['enp'].T[1]
ONETWOInput['inone']['NAMELIS1']['enp'].T[1]=ONETWOInput['inone']['NAMELIS1']['eni'].T[0]
ONETWOInput['inone']['NAMELIS1']['eni'].T[0]=root['SETTINGS']['DEPENDENCIES']['W']
# in addition, the input powers calculated by Nubeam can be input to the inone file so hopefully we can get the correct the H_98 and tau_e parameters
ONETWOInput['inone']['NAMELIS2']['extqerf']=1
ONETWOInput['inone']['NAMELIS2']['extqerf_watts']=0
ONETWOInput['inone']['NAMELIS2']['extqirf']=1
ONETWOInput['inone']['NAMELIS2']['extqirf_watts']=0
qbeame=root['OUTPUTSRec']['ONETWOOutput'][iternum]['trpltout.nc']['qbeame']['data'][-1]
qbeami=root['OUTPUTSRec']['ONETWOOutput'][iternum]['trpltout.nc']['qbeami']['data'][-1]
numrho=len(qbeame)
ONETWOInput['inone']['NAMELIS2']['extqerf_nj']=numrho
ONETWOInput['inone']['NAMELIS2']['extqirf_nj']=numrho
ONETWOInput['inone']['NAMELIS2']['extqerf_rho']=linspace(0,1,numrho)
ONETWOInput['inone']['NAMELIS2']['extqirf_rho']=linspace(0,1,numrho)
ONETWOInput['inone']['NAMELIS2']['extqerf_qe']=qbeame
ONETWOInput['inone']['NAMELIS2']['extqirf_qi']=qbeami
# run ONETWO
root['SCRIPTS']['RunONETWO']['baserun12_v57.py'].run()
# remerber to get the radiation power
# recover the inone file
root['INPUTSRec']['ONETWO'][iternum]['inone_dt']=ONETWOInput['inone'].duplicate()
ONETWOInput['inone']=ONETWOInput['inone_bak'].duplicate()
#ONETWOInput['inone']=ONETWOInput['inone_bak'].deepcopy()
# get the summary file which will be used to present the global parameters
root['OUTPUTSRec']['ONETWOOutput'][iternum]['summary_dt']=root['OUTPUTS']['ONETWOOutput']['summary'].duplicate()
