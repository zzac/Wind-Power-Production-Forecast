import pandas as pd
import os
dirname = os.path.dirname(__file__)

def load_production_dataset():
    return pd.read_parquet(os.path.join(dirname, "../../data/dataset_1.parquet"))

def load_coordinates_dataset():
    return pd.read_parquet(os.path.join(dirname, "../../data/dataset_2.parquet"))

def load_weather_dataset():
    return pd.read_parquet(os.path.join(dirname, "../../data/dataset_3.parquet"))

def load_full_dataset():
    df_prod = load_production_dataset()
    df_coords = load_coordinates_dataset()
    df_weather = load_weather_dataset()

    # Ensure delivery_time is in datetime format for both
    df_prod['delivery_time'] = pd.to_datetime(df_prod['delivery_time'])
    df_weather['delivery_time'] = pd.to_datetime(df_weather['delivery_time'])
    
    # Merge production and weather on site and time
    # Use an inner join to keep only rows present in both datasets
    df_merged = pd.merge(
        df_prod,
        df_weather,
        on=['site_name', 'delivery_time'],
        how='inner'
    )
    
    # Merge with coordinates to add latitude and longitude
    df_final = pd.merge(
        df_merged,
        df_coords[['site_name', 'latitude', 'longitude']],
        on='site_name',
        how='left'
    )
    
    # Sort by site and time for consistent time-series analysis
    df_final = df_final.sort_values(['site_name', 'delivery_time']).reset_index(drop=True)
    
    return df_final
