# basically,this script is used to rescale the temperature profile with different scaling factor over the profile
# the background is that sometimes we may change the pedestal density during the iteration ,for keeping the stability of the p-b mode, changing temperature is required
Tscale=root['SETTINGS']['PHYSICS']['Tscale']
rhoflat=Tscale[2]
nj=root['SETTINGS']['PHYSICS']['nj']
nflat=int(rhoflat*nj)+1
Tfct1=list(ones(nflat)*Tscale[0])
Tfct2_arr=linspace(sqrt(Tscale[0]),sqrt(Tscale[1]),nj-nflat)
#Tfct2=list(linspace(Tscale[0],Tscale[1],nj-nflat))
Tfct2=list(Tfct2_arr**2)
Tfct=array(Tfct1+Tfct2) 
Tipre=root['INPUTS']['ONETWOInput']['inone']['namelis1']['TIIN']
Tepre=root['INPUTS']['ONETWOInput']['inone']['namelis1']['TEIN']
Ti=Tipre*Tfct
Te=Tepre*Tfct
root['INPUTS']['ONETWOInput']['inone']['namelis1']['TIIN']=Ti
root['INPUTS']['ONETWOInput']['inone']['namelis1']['TEIN']=Te
