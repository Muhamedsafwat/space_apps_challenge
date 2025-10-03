import pandas as pd
import numpy as np
from scipy import stats
import json
import os

class DataIntegrator:
    """Integrate and analyze all data sources"""
    
    def __init__(self, data_dir='data/processed'):
        self.data_dir = data_dir
    
    def load_all_data(self):
        """Load all processed datasets"""
        print("Loading datasets...")
        
        self.sar_data = pd.read_csv(
            os.path.join(self.data_dir, 'sar_displacement.csv'),
            parse_dates=['date']
        )
        self.temp_data = pd.read_csv(
            os.path.join(self.data_dir, 'temperature_data.csv'),
            parse_dates=['date']
        )
        self.water_data = pd.read_csv(
            os.path.join(self.data_dir, 'water_levels.csv'),
            parse_dates=['date']
        )
        
        print("✅ All datasets loaded")
    
    def merge_datasets(self):
        """Merge datasets by date"""
        print("Merging datasets...")
        
        # Resample temperature to monthly
        temp_monthly = self.temp_data.set_index('date').resample('MS').mean().reset_index()
        
        # Merge all
        merged = self.sar_data.copy()
        merged = pd.merge_asof(
            merged.sort_values('date'),
            temp_monthly.sort_values('date'),
            on='date',
            direction='nearest'
        )
        merged = pd.merge_asof(
            merged.sort_values('date'),
            self.water_data.sort_values('date'),
            on='date',
            direction='nearest'
        )
        
        print("✅ Datasets merged")
        return merged
    
    def calculate_correlations(self, merged_data):
        """Calculate key correlations"""
        print("Calculating correlations...")
        
        correlations = {}
        
        # Water level vs displacement
        mask = ~(merged_data['water_level_m'].isna() | merged_data['displacement_mm'].isna())
        if mask.sum() > 2:
            corr, p_val = stats.pearsonr(
                merged_data.loc[mask, 'water_level_m'],
                merged_data.loc[mask, 'displacement_mm']
            )
            correlations['water_displacement'] = {
                'correlation': round(float(corr), 3),
                'p_value': float(p_val),
                'significant': bool(p_val < 0.05)  # <-- FIX HERE
            }
        
        # Temperature vs displacement
        mask = ~(merged_data['temp_max'].isna() | merged_data['displacement_mm'].isna())
        if mask.sum() > 2:
            corr, p_val = stats.pearsonr(
                merged_data.loc[mask, 'temp_max'],
                merged_data.loc[mask, 'displacement_mm']
            )
            correlations['temperature_displacement'] = {
                'correlation': round(float(corr), 3),
                'p_value': float(p_val),
                'significant': bool(p_val < 0.05)  # <-- AND FIX HERE
            }
        
        print("✅ Correlations calculated")
        return correlations
    
    def generate_insights(self, merged_data):
        """Generate comprehensive insights"""
        print("Generating insights...")
        
        # Calculate statistics
        total_displacement = float(merged_data['displacement_mm'].iloc[-1] - merged_data['displacement_mm'].iloc[0])
        n_years = (merged_data['date'].max() - merged_data['date'].min()).days / 365.25
        annual_rate = total_displacement / n_years if n_years > 0 else 0
        
        correlations = self.calculate_correlations(merged_data)
        
        insights = {
            "data_source": "NASA Sentinel-1 SAR + POWER API",
            "analysis_period": f"{merged_data['date'].min().strftime('%Y-%m')} to {merged_data['date'].max().strftime('%Y-%m')}",
            "total_displacement_mm": round(total_displacement, 2),
            "annual_subsidence_rate": round(annual_rate, 2),
            "key_findings": [
                f"Total subsidence: {abs(total_displacement):.1f}mm over {n_years:.1f} years",
                f"Annual subsidence rate: {abs(annual_rate):.2f}mm/year",
                f"Peak movement: {merged_data['displacement_mm'].min():.2f}mm on {merged_data.loc[merged_data['displacement_mm'].idxmin(), 'date'].strftime('%Y-%m-%d')}",
                f"Water level correlation: r={correlations.get('water_displacement', {}).get('correlation', 0):.3f}",
                f"Temperature extremes: {merged_data['temp_max'].max():.1f}°C max, {merged_data['temp_min'].min():.1f}°C min",
                f"Extreme heat days: {len(merged_data[merged_data['temp_max'] > 40])} days above 40°C"
            ],
            "correlations": correlations,
            "current_status": {
                "latest_displacement_mm": float(merged_data['displacement_mm'].iloc[-1]),
                "latest_water_level_m": float(merged_data['water_level_m'].iloc[-1]),
                "latest_temperature_c": float(merged_data['temp_max'].iloc[-1]),
                "displacement_velocity_mm_year": float(merged_data['velocity_mm_year'].iloc[-1])
            },
            "statistics": {
                "water_level": {
                    "mean": float(merged_data['water_level_m'].mean()),
                    "std": float(merged_data['water_level_m'].std()),
                    "max": float(merged_data['water_level_m'].max()),
                    "min": float(merged_data['water_level_m'].min())
                },
                "temperature": {
                    "mean_max": float(merged_data['temp_max'].mean()),
                    "mean_min": float(merged_data['temp_min'].mean()),
                    "absolute_max": float(merged_data['temp_max'].max()),
                    "absolute_min": float(merged_data['temp_min'].min())
                }
            }
        }
        
        print("✅ Insights generated")
        return insights
    
    def export_for_chatbot(self, insights):
        """Export analysis results for chatbot"""
        output_path = 'data/nasa_analysis_results.json'
        
        with open(output_path, 'w') as f:
            json.dump(insights, f, indent=2)
        
        print(f"✅ Results exported to {output_path}")
        return insights
    
    def run_full_analysis(self):
        """Run complete analysis pipeline"""
        print("\n🔬 Starting data integration and analysis...\n")
        
        self.load_all_data()
        merged = self.merge_datasets()
        insights = self.generate_insights(merged)
        self.export_for_chatbot(insights)
        
        print("\n✅ Analysis complete!")
        print(json.dumps(insights, indent=2))
        
        return insights

if __name__ == "__main__":
    integrator = DataIntegrator()
    integrator.run_full_analysis()