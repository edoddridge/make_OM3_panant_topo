# module imports
import xarray as xr
import dask.distributed as dask
import numpy as np

def extend_topog(ds, extend_lon=False):
    """Append a region of zeros to the north and south of the ML datasets
    so that the bathymetry covers all of the model domain.
    
    Some of the datasets need the longitude extended to wrap the whole globe.
    For those, also extend by one column in longitude - clone the data from the first
    line of longitude and put it on the far side too.
    To Consider: Might be better to interpolate between the two columns?"""
    
    dlat = ds.lat[-1] - ds.lat[-2]
    
    south_extension = np.arange(ds.lat[0], -90+dlat/2, -dlat)[::-1][:-1]
    north_extension = np.arange(ds.lat[-1], 90-dlat/2, dlat)[1:]
    
    extended_lat = np.concatenate([south_extension, ds.lat.values,  north_extension])
        # Tried recreating the whole axis, but it must not have been identical enough
        # so xarray kept both sets of data and things got messy.
        # np.arange(-90+dlat/2, 90-dlat/2,dlat)[:-1]
    
    if extend_lon:
        extended_lon = np.concatenate([ds.lon.values, np.array(-ds.lon.values[0],ndmin=1)])
    else:
        extended_lon=ds.lon.values
    
    extra_topog = xr.DataArray(np.zeros((len(extended_lat), len(extended_lon))),
                               [('lat', extended_lat),
                                ('lon', extended_lon)]).chunk('auto').to_dataset(name='elevation')

    lon_slice = xr.DataArray(ds['elevation'].sel(lon=ds.lon[0]),
                             {'lat':ds.lat,
                              'lon':-ds.lon[0]}).chunk('auto').to_dataset(name='elevation')
    
    # replace line of zeros at the extended longitude value with data from the
    # first line of longitude
    extra_topog = extra_topog.combine_first(lon_slice)

    ds_extended_topog = ds.combine_first(extra_topog)

    return ds_extended_topog
        
def pre_process():
    """Convert the variable names in the ML datasets to be consistent with
    GEBCO and expand the domain to cover -90 to 90 Lat so that the ACCESS-NRI
    topog tools will work with these datasets.

    To consider:
        - add input to the function for directory where the datasets are stored.
        - add input to the function for directory where the outputs should go.
    
    """

    # ToDo
    # - add input to the function for directory where the datasets are stored.
    # - add input to the function for directory where the outputs should go.
    
    # initialise cluster
    client = dask.Client(threads_per_worker = 1)

    # load ML based datasets
    ds_ML_mean = xr.open_dataset('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/MEAN.nc', chunks='auto')
    ds_dtu_dkl = xr.open_dataset('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DKL_6_Ker50.nc', chunks='auto')
    ds_dtu_dnn = xr.open_dataset('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DNN_Biao_topo_version2.nc', chunks='auto')
    ds_ncu_dnn = xr.open_dataset('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NCU_DNN_bathymetry_model_April_2025.nc', chunks='auto')
    ds_nrl_cnn = xr.open_dataset('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NRL_CNN_bathy_prediction_p65_20250401.nc', chunks='auto')

    # rename variable to 'elevation'
    ds_ML_mean = ds_ML_mean["z"].rename("elevation").to_dataset()
    ds_dtu_dkl = ds_dtu_dkl["z"].rename("elevation").to_dataset()
    ds_dtu_dnn = ds_dtu_dnn["prediction"].rename("elevation").to_dataset()
    ds_ncu_dnn = ds_ncu_dnn["z"].rename("elevation").to_dataset()
    ds_nrl_cnn = ds_nrl_cnn["z"].rename("elevation").to_dataset()

    # append a region that extends to the south pole for interpolation
    ds_ML_mean = extend_topog(ds_ML_mean, extend_lon=True)
    ds_dtu_dkl = extend_topog(ds_dtu_dkl, extend_lon=True)
    ds_dtu_dnn = extend_topog(ds_dtu_dnn)
    ds_ncu_dnn = extend_topog(ds_ncu_dnn)
    ds_nrl_cnn = extend_topog(ds_nrl_cnn)

    # export to netcdf
    ds_ML_mean.to_netcdf('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/ML_mean_pre_processed.nc')
    ds_dtu_dkl.to_netcdf('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DKL_6_Ker50_pre_processed.nc')
    ds_dtu_dnn.to_netcdf('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/DTU_DNN_Biao_topo_version2_pre_processed.nc')
    ds_ncu_dnn.to_netcdf('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NCU_DNN_bathymetry_model_April_2025_pre_processed.nc')
    ds_nrl_cnn.to_netcdf('/g/data/jk72/ed7737/datasets/bathymetry/ML_topos/NRL_CNN_bathy_prediction_p65_20250401_pre_processed.nc')

    return

if __name__ == "__main__":
    pre_process()
