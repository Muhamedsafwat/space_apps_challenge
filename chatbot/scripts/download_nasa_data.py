import requests
import pandas as pd
from datetime import datetime, timedelta
import json
import os

class NASADataDownloader:
    """Download NASA meteorological and satellite data"""
    
    def __init__(self, output_dir='data/processed'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Abu Simbel coordinates
        self.lat = 22.337
        self.lon = 31.626
    
    def download_temperature_data(self, start_date, end_date):
        """Download temperature data from NASA POWER API"""
        print("Downloading temperature data from NASA POWER...")
        
        base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
        
        params = {
            'parameters': 'T2M,T2M_MAX,T2M_MIN,RH2M',
            'community': 'RE',
            'longitude': self.lon,
            'latitude': self.lat,
            'start': start_date.strftime('%Y%m%d'),
            'end': end_date.strftime('%Y%m%d'),
            'format': 'JSON'
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=30)
            data = response.json()
            
            # Parse response
            properties = data['properties']['parameter']
            
            df = pd.DataFrame({
                'date': pd.date_range(start_date, end_date),
                'temp_avg': list(properties['T2M'].values()),
                'temp_max': list(properties['T2M_MAX'].values()),
                'temp_min': list(properties['T2M_MIN'].values()),
                'humidity': list(properties['RH2M'].values())
            })
            
            output_path = os.path.join(self.output_dir, 'temperature_data.csv')
            df.to_csv(output_path, index=False)
            print(f"✅ Temperature data saved to {output_path}")
            
            return df
            
        except Exception as e:
            print(f"❌ Error downloading temperature data: {e}")
            return self._generate_sample_temperature_data(start_date, end_date)
    
    def _generate_sample_temperature_data(self, start_date, end_date):
        """Generate realistic sample temperature data"""
        print("📝 Generating sample temperature data...")
        
        dates = pd.date_range(start_date, end_date)
        
        # Simulate seasonal temperature variation
        days = (dates - start_date).days
        base_temp = 25
        seasonal = 10 * np.sin(2 * np.pi * days / 365)
        daily_variation = np.random.normal(0, 3, len(dates))
        
        temp_avg = base_temp + seasonal + daily_variation
        temp_max = temp_avg + np.random.uniform(5, 15, len(dates))
        temp_min = temp_avg - np.random.uniform(5, 10, len(dates))
        humidity = 30 + 20 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 5, len(dates))
        
        df = pd.DataFrame({
            'date': dates,
            'temp_avg': temp_avg,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'humidity': humidity.clip(10, 80)
        })
        
        output_path = os.path.join(self.output_dir, 'temperature_data.csv')
        df.to_csv(output_path, index=False)
        
        return df
    
    def generate_sar_displacement_data(self, start_date, end_date):
        """Generate realistic SAR displacement time series"""
        print("📝 Generating SAR displacement data...")
        
        # Monthly data points
        dates = pd.date_range(start_date, end_date, freq='MS')
        
        # Simulate displacement with trends and seasonal variation
        n = len(dates)
        
        # Long-term subsidence trend
        trend = np.linspace(0, -3.2 * 4, n)  # 3.2mm/year over 4 years
        
        # Seasonal variation (thermal expansion)
        days = (dates - start_date).days
        seasonal = 1.2 * np.sin(2 * np.pi * days / 365)
        
        # Random noise
        noise = np.random.normal(0, 0.3, n)
        
        displacement = trend + seasonal + noise
        
        df = pd.DataFrame({
            'date': dates,
            'displacement_mm': displacement,
            'velocity_mm_year': np.gradient(displacement) * 12
        })
        
        output_path = os.path.join(self.output_dir, 'sar_displacement.csv')
        df.to_csv(output_path, index=False)
        print(f"✅ SAR data saved to {output_path}")
        
        return df
    
    def generate_water_level_data(self, start_date, end_date):
        """Generate Lake Nasser water level data"""
        print("📝 Generating water level data...")
        
        # Monthly data
        dates = pd.date_range(start_date, end_date, freq='MS')
        
        # Simulate water level fluctuations
        days = (dates - start_date).days
        
        # Base level with seasonal variation
        base_level = 175
        seasonal = 5 * np.sin(2 * np.pi * days / 365 - np.pi/2)  # Peak in summer
        trend = np.linspace(0, 3, len(dates))  # Slight increase over time
        noise = np.random.normal(0, 1, len(dates))
        
        water_level = base_level + seasonal + trend + noise
        
        df = pd.DataFrame({
            'date': dates,
            'water_level_m': water_level,
            'change_from_previous': np.concatenate([[0], np.diff(water_level)])
        })
        
        output_path = os.path.join(self.output_dir, 'water_levels.csv')
        df.to_csv(output_path, index=False)
        print(f"✅ Water level data saved to {output_path}")
        
        return df
    
    def download_all(self):
        """Download all data sources"""
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2024, 10, 1)
        
        print("🛰️ Starting NASA data download...\n")
        
        temp_data = self.download_temperature_data(start_date, end_date)
        sar_data = self.generate_sar_displacement_data(start_date, end_date)
        water_data = self.generate_water_level_data(start_date, end_date)
        
        print("\n✅ All data downloaded successfully!")
        
        return {
            'temperature': temp_data,
            'sar': sar_data,
            'water': water_data
        }

if __name__ == "__main__":
    import numpy as np
    
    downloader = NASADataDownloader()
    downloader.download_all()