READ ME
=======

Integrated testing will give confidence in the pipeline by allowing the automated detection of changes in the results.

Steps to set this up.


1. Subset the horizontal grid


```
cd /home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data/
module purge
module load nco
ncks -d nyp,1782,1840 -d ny,1782,1839 /g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc ocean_hgrid_subset_by_lat.nc
ncks -d nxp,5303,5329 -d nx,5303,5328 ocean_hgrid_subset_by_lat.nc ocean_hgrid_subset_by_lat_lon.nc
```

Then cleanup

```
rm ocean_hgrid_subset_by_lat.nc
```


2. Subset one of the bathymetry inputs

Move to the bathymetry folder `/g/data/jk72/ed7737/datasets/bathymetry/ML_topos` 

```
cd /g/data/jk72/ed7737/datasets/bathymetry/ML_topos
```

and run the following commands

````
module purge
module load nco
ncks -d lat,-65.5,-63.5  DTU_DKL_6_Ker50_pre_processed.nc DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc
ncks -d lon,40.5,42.5 DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc DTU_DKL_6_Ker50_pre_processed_subset_by_lat_lon.nc
````

Then cleanup

````
rm DTU_DKL_6_Ker50_pre_processed_subset_by_lat.nc
````

Move it to the `make_OM3_panant_topo` repository `test/data` folder.

````
mkdir -p /home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data/
mv DTU_DKL_6_Ker50_pre_processed_subset_by_lat_lon.nc /home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data/
````

3. Apply the `gen_topo.sh` script to these cut down datasets

```
qsub -v INPUT_HGRID=/home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data/ocean_hgrid_subset_by_lat_lon.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/home/552/ed7737/coding-and-projects/panant_bathy_ensemble/make_OM3_panant_topo/test/data/DTU_DKL_6_Ker50_pre_processed_subset_by_lat_lon.nc,INPUT_BATHY_SHORT=TEST -P $PROJECT gen_topo.sh
```

Unfortunately this doesn't work. I think it's becuase the script requires global bathymetry datasets, even though the grid file only covers a small region.