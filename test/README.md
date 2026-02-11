READ ME
=======

Integrated testing will give confidence in the pipeline by allowing the automated detection of changes in the results.

Steps to set this up.

1. Subset one of the bathymetry inputs

In the bathymetry folder `/g/data/jk72/ed7737/datasets/bathymetry/ML_topos` run the following commands

`
module purge
module load nco
ncks -d lat,-50.,-45.  DTU_DKL_6_Ker50_pre_processed.nc DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc
ncks -d lon,110.0,115.0 DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc DTU_DKL_6_Ker50_pre_processed_subset_by_lat_lon.nc
`

Then cleanup

`
rm DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc
`

Move it to the `make_OM3_panant_topo` repository `test` folder.

`
mv DTU_DKL_6_Ker50_pre_processed_subset_by_lat_lon.nc /home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data
`