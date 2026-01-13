#!/usr/bin/env sh
# Copyright 2025 ACCESS-NRI and contributors. See the top-level COPYRIGHT file for details.
# SPDX-License-Identifier: Apache-2.0

#PBS -q normal
#PBS -l walltime=1:00:00
#PBS -l mem=70GB
#PBS -l jobfs=1GB
#PBS -l ncpus=10
#PBS -P jk72
#PBS -l wd
#PBS -l storage=gdata/ik11+gdata/jk72+gdata/xp65+gdata/vk83

module purge
module use /g/data/xp65/public/modules
module load conda/analysis3-25.11

python3 ./pre-process_ML_bathy_data.py


