# make_OM3_4km_PanAnt_topo

Make 4 km `topog.nc` MOM bathymetry file from the machine learning bathymetry datasets

## Workflow Overview

0. **Pre-Process ML bathymetry products:**
   
   Use `pre_process_topo.sh` to massage the ML bathymetry products to work with this pipeline.

1. **Generate Topography:**  
   Use `./gen_topog.sh` to generate the topography and associated files. For 0.25-degree resolution or higher, this will require submission via `qsub`.

   First, add gdata for your project & working directory to the `#PBS -l storage=` line in `get_topo.sh`

   Then, use the `qsub` command to submit the script, passing the required input files as arguments. For example:  
   ```bash
   qsub -v INPUT_HGRID="/path/to/ocean_hgrid.nc",INPUT_VGRID="/path/to/ocean_vgrid.nc",INPUT_GBCO="/path/to/GEBCO_2024.nc" -P $PROJECT gen_topo.sh
   ```

2. **Finalize Output Files:**  
   Once the output files meet your satisfaction, commit and push the changes, then add the git commit hash as metadata in the output `.nc` files by running `finalise.sh`.

## Note on Dependencies  

This workflow relies on the **xp65 conda environments** for running the scripts and generating the outputs. As long as you are a member of the _xp65_ project, this conda environment is loaded as part of the scripts.

--- 

## Commands

### GEBCO
```bash
qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/ik11/inputs/GEBCO_2024/GEBCO_2024.nc,INPUT_BATHY_SHORT=GEBCO24 -P $PROJECT gen_topo.sh
```
#### Finalise files
```bash
bash finalise.sh
```

#### Move outputs to the GEBCO folder
```bash
mv access-om3-4km-ML-GEBCO24-*.nc kmt.nc topog.nc /g/data/jk72/ed7737/access-om3/inputs/8km-global/bathy_products/GEBCO
```

Repeat for the other datasets.

### ML Mean
```bash
qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/ML_mean_pre_processed.nc,INPUT_BATHY_SHORT=MEAN -P $PROJECT gen_topo.sh
```
#### Finalise files
```bash
bash finalise.sh
```

#### Move outputs to the ML Mean folder
```bash
mv access-om3-4km-ML-MEAN-*.nc kmt.nc topog.nc /g/data/jk72/ed7737/access-om3/inputs/8km-global/bathy_products/ML_mean
```

### DTU_DKL
```bash
qsub -v INPUT_HGRID=//g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DKL_6_Ker50_pre_processed.nc,INPUT_BATHY_SHORT=DTU_DKL -P $PROJECT gen_topo.sh
```

#### Finalise files
```bash
bash finalise.sh
```

#### Move outputs to the DTU_DKL folder
```bash
mv access-om3-4km-ML-DTU_DKL-*.nc kmt.nc topog.nc /g/data/jk72/ed7737/access-om3/inputs/8km-global/bathy_products/DTU_DKL
```
And so on for the remaining datasets: `DTU_DNN`, `NCU_DNN`, and `NRL_CNN`.

