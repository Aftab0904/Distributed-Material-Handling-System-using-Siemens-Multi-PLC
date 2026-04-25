import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Simulate PLC Data for Visualization
def generate_system_analytics():
    np.random.seed(42)
    time_series = [datetime.now() - timedelta(minutes=x) for x in range(60)]
    line1_flow = np.random.normal(25, 5, 60).clip(10, 40)
    line2_flow = np.random.normal(22, 4, 60).clip(10, 40)
    
    df = pd.DataFrame({
        'Timestamp': time_series,
        'Line_1_Throughput': line1_flow,
        'Line_2_Throughput': line2_flow
    })

    # Set style
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))
    
    # Plot Throughput
    plt.plot(df['Timestamp'], df['Line_1_Throughput'], label='Line 1 (Master Controller)', color='#2d5a27', linewidth=2)
    plt.plot(df['Timestamp'], df['Line_2_Throughput'], label='Line 2 (Sub Controller)', color='#1e3a5f', linewidth=2)
    
    plt.title('Real-time Material Handling Throughput (Items/Min)', fontsize=15)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Items Per Minute', fontsize=12)
    plt.legend()
    plt.tight_layout()
    
    # Save the chart for GitHub Readme
    plt.savefig('Distributed-Material-Handling-System-using-Siemens-Multi-PLC/assets/system_throughput_analytics.png')
    print("Analytics Chart Generated Successfully")

if __name__ == "__main__":
    generate_system_analytics()
