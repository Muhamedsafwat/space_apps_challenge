import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt

class InSARProcessor:
    """Process InSAR data to extract ground deformation"""
    
    def __init__(self, reference_date, secondary_date):
        self.ref_date = reference_date
        self.sec_date = secondary_date
        
    def calculate_displacement(self, interferogram_path):
        """Calculate ground displacement from interferogram"""
        # Open interferogram
        ds = gdal.Open(interferogram_path)
        phase = ds.ReadAsArray()
        
        # Convert phase to displacement
        wavelength = 0.056  # Sentinel-1 C-band wavelength (m)
        displacement = (phase / (4 * np.pi)) * wavelength * 1000  # Convert to mm
        
        return displacement
    
    def extract_temple_point(self, displacement_map, lat=22.337, lon=31.626):
        """Extract displacement at temple location"""
        # Convert lat/lon to pixel coordinates
        geotransform = self.get_geotransform()
        pixel_x, pixel_y = self.latlon_to_pixel(lat, lon, geotransform)
        
        # Get displacement value
        temple_displacement = displacement_map[pixel_y, pixel_x]
        
        return temple_displacement
    
    def generate_time_series(self, displacement_maps, dates):
        """Generate displacement time series"""
        time_series = []
        
        for disp_map, date in zip(displacement_maps, dates):
            value = self.extract_temple_point(disp_map)
            time_series.append({
                'date': date,
                'displacement_mm': value
            })
        
        return time_series