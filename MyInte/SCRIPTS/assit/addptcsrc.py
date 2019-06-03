# this script is used to add the particle source , which may comes from pellet injection
ptcsrc=root['SETTINGS']['PHYSICS']['iaddptcsrc']
# ptcsrc is an arrary of 5 elements.
# [flag, rho_min, rho_left_widht, rho_right_width, amplititude(10^19)]
num=201
flag=ptcsrc[0]
rmid=ptcsrc[1]
rlw=ptcsrc[2] # rho of left width
rrw=ptcsrc[3]
amp=ptcsrc[4]
srcpro=zeros(num)
ilb=int((rmid-rlw)*(num-1))    # index of left boundary
irb=int((rmid+rrw)*(num-1))    # index of right boundary
imid=int(rmid*(num-1))         # index of rho_mid
for k in range(1,num+1):
    if k >= ilb and k <= imid:
        srcpro[k]=(k-ilb)*amp/(imid-ilb)
    elif k>= imid and k<= irb:
        srcpro[k]=(irb-k)*amp/(irb-imid)
srcpro=1.e19*srcpro
if flag==1:
   # add the srcpro to the sbeam
    statefile=root['OUTPUTS']['ONETWOOutput']['statefile']
    # the original sbeam is backup to  another place
    root['SETTINGS']['TEMP']['beamsrc_orig']=statefile['sbeame']['data']
    statefile['sbeam']['data'][0]=statefile['sbeam']['data'][0]+srcpro
    statefile['sbeame']['data']=statefile['sbeame']['data']+srcpro
