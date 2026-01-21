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

### GEBCO 2024
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/ik11/inputs/GEBCO_2024/GEBCO_2024.nc,INPUT_BATHY_SHORT=GEBCO24 -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the GEBCO24 folder
    mv access-om3-4km-ML-GEBCO24-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/GEBCO24
```

### GEBCO 2025
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/gebco_2025/GEBCO_2025.nc,INPUT_BATHY_SHORT=GEBCO25 -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the GEBCO25 folder
    mv access-om3-4km-ML-GEBCO25-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/GEBCO25
```

### ML MEAN
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/ML_mean_pre_processed.nc,INPUT_BATHY_SHORT=MEAN -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the ML_mean folder
    mv access-om3-4km-ML-MEAN-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/MEAN
```

### DTU_DKL
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DKL_6_Ker50_pre_processed.nc,INPUT_BATHY_SHORT=DTU_DKL -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the DTU_DKL folder
    mv access-om3-4km-ML-DTU_DKL-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/DTU_DKL
```

### DTU_DNN
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DNN_Biao_topo_version2_pre_processed.nc,INPUT_BATHY_SHORT=DTU_DNN -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the DTU_DNN folder
    mv access-om3-4km-ML-DTU_DNN-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/DTU_DNN
```

### NCU_DNN
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NCU_DNN_bathymetry_model_April_2025_pre_processed.nc,INPUT_BATHY_SHORT=NCU_DNN -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the NCU_DNN folder
    mv access-om3-4km-ML-NCU_DNN-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/NCU_DNN
```

### NRL_CNN
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NRL_CNN_bathy_prediction_p65_20250401_pre_processed.nc,INPUT_BATHY_SHORT=NRL_CNN -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the NRL_CNN folder
    mv access-om3-4km-ML-NRL_CNN-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/NRL_CNN
```

### SRTM15 V2.7
```bash
    qsub -v INPUT_HGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_hgrid.nc,INPUT_VGRID=/g/data/vk83/prerelease/configurations/inputs/access-om3/panan.4km/2026.01.08/ocean_vgrid.nc,INPUT_BATHY=/g/data/jk72/ed7737/datasets/bathymetry/SRTM15/SRTM15_V2.7_pre_processed.nc,INPUT_BATHY_SHORT=SRTM15_V2_7 -P $PROJECT gen_topo.sh

    bash finalise.sh

    # move outputs to the SRTM15_V2_7 folder
    mv access-om3-4km-ML-SRTM15_V2_7-*.nc kmt.nc topog.nc gen_topo.sh.* /g/data/jk72/ed7737/access-om3/inputs/4km-PanAntarctic/bathy_products/SRTM15_V2_7
```
