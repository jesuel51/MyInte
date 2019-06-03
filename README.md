# MyInte
MyInte integrated predictive module 
This module is used to do the integrated predictive modeling, mostly for CFETR. Original comes from /scratch/xiangjian/OMFIT-source/modules/MyInte on kuafu.
Some features of this module.
1. Can atomitically adjust the auxliary heating power to keep the ohmic current fraction in a desired level which is specified by the user;
2. Can integrate the ForW module to do the integrated modeling with self-consistent evaluation of the impurity profile and its effect on the global performance.
One template projects would be.
/scratch/xiangjian/OMFITdata/pro_ssy/CFETR7.2_HY__5_modifyECW_jglirefrad_0.95correctPedestalEnergyBeam1_300EnergyBeam2_600RT1_480RT2_660PowNB1_24pvtin_0.25n1.1ECLFS2rfpow1_0rfpow2_10addpellet_rhomid_0.6amptcsrc_6PowHelicon_20.zip
This module is very flexible, the setting can vary significantly with the users requirement.
