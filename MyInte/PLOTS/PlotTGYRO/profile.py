# Created by xiangjian at 2015/05/04 21:32
# this script is used to read the files and turn it into profile and profile gradient and write them in root['SETTINGS']['TEMP']
def readouttgyro(filename):
# return all the numerisim data in a format of [numrho*niter, ncol]
    f=open(filename,'Ur')
    fread=f.readlines()
    lis=[]
    for line in fread:
        lintemp=line.split()
        try:
            temp=float(lintemp[0])
            lis.append(line)
        except:
            continue
# turn the list to array so that it can be easily handled
    row=len(lis)
    col=len(lis[0].split())
    arr=zeros([row,col])
    for k in arange(row):
        arr[k]=[float(item) for item in lis[k].split()]
    arr=arr.T
    return arr
    f.close()


inputtgyro=root['INPUTS']['TGYRO']['input.tgyro']
tgyro_max=inputtgyro['TGYRO_RMAX']
ptgyro=len(inputtgyro['DIR'])
outtgyro=root['OUTPUTS']['TGYRO']
# r/a, beta_unit, a*beta_*, a*gamma_p/cs, a*gamma_e/cs, a*f_rot, Mach
arr_profile=readouttgyro(outtgyro['out.tgyro.profile'].filename)
# r/a, ne, a/Lne,te,a/LTe,betae
arr_profile_e=readouttgyro(outtgyro['out.tgyro.profile_e'].filename)
# r/a, ne, a/Lni1, ti1, a/LTi1, betai1
arr_profile_i1=readouttgyro(outtgyro['out.tgyro.profile_i1'].filename)
# r/a, rho, q, s, kappa, s_kappa, delta, s_delta, shift, rmaj/a, b_unit
arr_geometry1=readouttgyro(outtgyro['out.tgyro.geometry.1'].filename)
# r/a , Chi_GB,Q _GB, Gamma_GB, Pi_GB, S_GB, c_s
arr_gyrobohm=readouttgyro(outtgyro['out.tgyro.gyrobohm'].filename)
# get the profiles(simculated and expinal)
# simculated 
ne_sim=arr_profile_e[1][-ptgyro-1:]
aLne_sim=arr_profile_e[2][-ptgyro-1:]
Te_sim=arr_profile_e[3][-ptgyro-1:]
aLTe_sim=arr_profile_e[4][-ptgyro-1:]
ni_sim=arr_profile_i1[1][-ptgyro-1:]
aLni_sim=arr_profile_i1[2][-ptgyro-1:]
Ti_sim=arr_profile_i1[3][-ptgyro-1:]
aLTi_sim=arr_profile_i1[4][-ptgyro-1:]
# rotation
Mach_sim=arr_profile[6][-ptgyro-1:]
a=root['INPUTS']['TGYRO']['input.profiles']['rmin'][-1]
rho=arr_geometry1[1][-ptgyro-1:]
gcs_sim=arr_gyrobohm[6][-ptgyro-1:]
rmaj=a*arr_geometry1[9][-ptgyro-1:]
w0_sim=Mach_sim*gcs_sim/rmaj
aLw0_sim=arr_profile[3][-ptgyro-1:]
# expinal
ne_exp=arr_profile_e[1][0:ptgyro+1]
aLne_exp=arr_profile_e[2][0:ptgyro+1]
Te_exp=arr_profile_e[3][0:ptgyro+1]
aLTe_exp=arr_profile_e[4][0:ptgyro+1]
ni_exp=arr_profile_i1[1][0:ptgyro+1]
aLni_exp=arr_profile_i1[2][0:ptgyro+1]
Ti_exp=arr_profile_i1[3][0:ptgyro+1]
aLTi_exp=arr_profile_i1[4][0:ptgyro+1]
# rotation
Mach_exp=arr_profile[6][0:ptgyro+1]
gcs_exp=arr_gyrobohm[6][0:ptgyro+1]
rmaj=a*arr_geometry1[9][0:ptgyro+1]
w0_exp=Mach_exp*gcs_exp/rmaj
aLw0_exp=arr_profile[3][0:ptgyro+1]
# store the date
root['SETTINGS']['TEMP']=OMFITtree()
temp=root['SETTINGS']['TEMP']
temp['rho']=rho
temp['ne']=ne_sim
temp['Te']=Te_sim
temp['Ti']=Ti_sim
temp['w0']=w0_sim
temp['aLne']=aLne_sim
temp['aLTe']=aLTe_sim
temp['aLTi']=aLTi_sim
temp['aLw0']=aLw0_sim
#temp['ne_exp']=ne_exp
#temp['Te_exp']=Te_exp
#temp['Ti_exp']=Ti_exp
#temp['w0_exp']=w0_exp
#temp['aLne_exp']=aLne_exp
#temp['aLTe_exp']=aLTe_exp
#temp['aLTi_exp']=aLTi_exp
#temp['aLw0_exp']=aLw0_exp

