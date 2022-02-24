# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:20:00 2022

@author: schne_la
"""

# =============================================================================
# Packages
# =============================================================================
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import cartopy.crs as ccrs
from dfm_tools.get_nc import plot_netmapdata
from mpl_toolkits.axes_grid1 import make_axes_locatable

# =============================================================================
# Functions
# =============================================================================

# ideas to expand:
# take multiple model simulations. modData_time and modData_value then as *args??
def plotTS_modelNWDM(obsdata_time, 
                    obsdata_value, 
                    modData_time, 
                    modData_value, 
                    loc_x, 
                    loc_y, 
                    lab_vars, 
                    stationName,
                    minVal = 0,
                    **kwargs):
    """
    Plot NWDM and model timeseries in one plot along with a map of location.

    Parameters
    ----------
    obsdata_time : panda series
        date column of the NWDM observation dataframe.
    obsdata_value : panda series
        value column of the NWDM observation dataframe.
    modData_time : panda series
        date column of the model output dataframe.
    modData_value : panda series
        value column of the model output datafram.
    loc_x : panda series
        x column (long) of the location dataframe.
    loc_y : panda series
        y column (lat) of the location dataframe.
    lab_vars : str
        string of the colorbar label.
    stationName : str
        station name of the station that is plotted.
    minVal : int, optional
        DESCRIPTION. minimum y axis value. The default is 0.
    **title : str
        title of the plot.
    **mapExtent : list
        coordinates of the extent of the map.

    Returns
    -------
    None.

    """
    # create figure 
    fig = plt.figure(figsize=(12,6), dpi=300)
    # divide figure into 6 parts using gridspec
    gs = fig.add_gridspec(6, 6)
    # set global font size
    plt.rcParams.update({'font.size': 12})   
    
    # first part of figure in first 4 columns of gridspec
    ax = fig.add_subplot(gs[:, 0:4])      
    # Plot observations from NWDM
    ax.plot(obsdata_time, obsdata_value, color='grey', linestyle='None', marker='.', markersize=10, label = 'obs')
    # Plot model 
    ax.plot(modData_time, modData_value, color = 'red', linestyle='-', linewidth=0.6, label = 'sim') 
    
    # leg = ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left", borderaxespad=0, ncol=5, fontsize = 7)
    
    # y-axis settings
    ax.set_ylabel(lab_vars, fontsize=15)  
    ax.set_ylim(ymin = minVal)
        
    # x-axis settings [use ax.set_xlim([tstart, tend])  if the x axis should be tight]
    # set date format and label size
    myFmt = mdates.DateFormatter('%b%y')
    ax.xaxis.set_major_formatter(myFmt)
    ax.tick_params(axis="x", labelsize=11)
    
    # title
    ax.set_title(stationName)
       
    # add map to last two column of gridspec
    map1 = fig.add_subplot(gs[:, 4:6], projection=ccrs.PlateCarree())  
    
    if 'title' in kwargs.keys():
        plt.title(kwargs['title'])
        
    if 'mapExtent' in kwargs.keys():
        map1.set_extent(kwargs['mapExtent'], ccrs.PlateCarree())
    else:
        map1.set_extent([-5, 15, 50, 65], ccrs.PlateCarree())
        
    map1.set_extent([-5, 15, 50, 65], ccrs.PlateCarree())
    map1.coastlines(resolution='10m')
    map1.gridlines(draw_labels=True)
    map1.plot(loc_x, loc_y,  markersize=5, marker='o', color='red')
    
    plt.tight_layout()
    
    
def dotplot_modelNWDM(ugrid, 
                      modData_value, 
                      obsData_x, obsData_y, obsData_value,
                      pltLabel,
                      clim,
                      key, 
                      year, 
                      pltTitle, 
                      **kwargs):
    """
    Plot map of model output with NWDM data as dots.

    Parameters
    ----------
    ugrid : dfm_tools.ugrid.UGrid
        DESCRIPTION.
    modData_value : pandas dataframe
        DESCRIPTION.
    obsData_x : panda series
        DESCRIPTION.
    obsData_y : panda series
        DESCRIPTION.
    obsData_value : panda series
        DESCRIPTION.
    pltLabel : str
        DESCRIPTION.
    clim : list
        DESCRIPTION.
    key : str
        DESCRIPTION.
    year : int
        DESCRIPTION.
    pltTitle : str
        DESCRIPTION.
    **lat : list
        DESCRIPTION.
    **lon : list
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # create figure
    fig, ax_input = plt.subplots(1,1)
    # plot map of model output
    pc = plot_netmapdata(ugrid.verts, values=modData_value, ax=ax_input, linewidth=0.5, edgecolors='face', cmap='viridis')
    # set colorbar limit for map
    pc.set_clim(clim)
    # plot NWDM data as dots
    dc = plt.scatter(obsData_x, obsData_y, s=6, c=obsData_value, cmap='viridis', edgecolors='black', linewidth=0.1)
    # set colorbar limit for dots (same as for map)
    dc.set_clim(clim)
    # equal axis
    ax_input.set_aspect('equal')
    
    # define extent of map
    if 'lon' in kwargs.keys():
        ax_input.set_xlim(kwargs['lon'])
        
    if 'lat' in kwargs.keys():
        ax_input.set_ylim(kwargs['lat'])
    
    # create an axes 
    divider = make_axes_locatable(ax_input)
    # bottom of the map
    # The width of cax will be 5% of ax and the padding between cax and ax will be fixed at 0.3 inch.
    cax = divider.append_axes("bottom", size="5%", pad=0.3)
    # create colorbar
    fig.colorbar(pc,ax=ax_input,label=pltLabel, orientation='horizontal', extend = 'max', cax=cax)
    # set plot title using keyword  
    if key == 'single':
        ax_input.set_title(year)
    else:
        ax_input.set_title(pltTitle)
        
