"""
EU ETS Carbon Price Analyzer
Author: Felix Okumo
Email: felix.1.okumo@gmail.com
GitHub: github.com/felixokumo1-stack/EU-ETS-Carbon-Analysis
Date: January 2026

Description:
This script analyzes European Emission Trading System (EU ETS) carbon allowance 
prices from 2022-2024. It performs statistical analysis, calculates key market 
indicators (moving averages, volatility, trends), and generates professional 
visualizations and automated market insight reports.

Features:
- Data loading and preprocessing with time series formatting
- Moving average calculations (30-day and 90-day)
- Price volatility and trend analysis using statistical methods
- Year-over-year comparison with percentage change calculations
- Automated generation of 4 professional visualizations
- Comprehensive market insights report generation

Technologies: Python 3.14, pandas, matplotlib, numpy

License: MIT License
Copyright (c) 2026 Felix Okumo
"""

# ============================================================================
# IMPORT LIBRARIES
# ============================================================================

import pandas as pd              # Data manipulation and analysis
import matplotlib.pyplot as plt  # Data visualization and charting
import matplotlib.dates as mdates  # Date formatting for charts
import numpy as np              # Numerical computations

# ============================================================================
# CONFIGURATION AND SETUP
# ============================================================================

print("="*60)
print("EU ETS Carbon Price Analyzer")
print("Author: Felix Okumo | January 2026")
print("="*60)

# ============================================================================
# DATA LOADING AND PREPROCESSING
# ============================================================================

print("\n1. Loading data...")

# Load carbon price data from CSV file
df = pd.read_csv('EU_ETS_Carbon_Prices_2022-2024.csv')

# Convert date strings to datetime objects (DD/MM/YYYY format)
# dayfirst=True handles European date format correctly
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Set Date as index for easier time series analysis
# This allows for date-based filtering and resampling operations
df.set_index('Date', inplace=True)

# Display basic information about the loaded dataset
print(f"✓ Data loaded successfully!")
print(f"  - Total trading days: {len(df)}")
print(f"  - Date range: {df.index.min().strftime('%Y-%m-%d')} to {df.index.max().strftime('%Y-%m-%d')}")
print(f"\n  First few rows:")
print(df.head())

# ============================================================================
# STATISTICAL ANALYSIS
# ============================================================================

print("\n" + "="*60)
print("2. Calculating Key Statistics...")
print("="*60)

# Extract key price metrics
current_price = df['Close'].iloc[-1]  # Most recent closing price
average_price = df['Close'].mean()     # Mean price over entire period
min_price = df['Close'].min()          # Minimum price in dataset
max_price = df['Close'].max()          # Maximum price in dataset

# Display price summary statistics
print(f"\n📊 Price Summary:")
print(f"  - Current Price: €{current_price:.2f} per ton")
print(f"  - Average Price: €{average_price:.2f} per ton")
print(f"  - Minimum Price: €{min_price:.2f} per ton")
print(f"  - Maximum Price: €{max_price:.2f} per ton")

# Calculate moving averages for trend analysis
# Moving averages smooth out short-term fluctuations to reveal longer-term trends
df['MA_30'] = df['Close'].rolling(window=30).mean()  # 30-day moving average
df['MA_90'] = df['Close'].rolling(window=90).mean()  # 90-day moving average

print(f"\n📈 Moving Averages (current):")
print(f"  - 30-day MA: €{df['MA_30'].iloc[-1]:.2f}")
print(f"  - 90-day MA: €{df['MA_90'].iloc[-1]:.2f}")

# Calculate price volatility using standard deviation
# Higher standard deviation indicates greater price variability/risk
volatility = df['Close'].std()
print(f"\n📉 Price Volatility:")
print(f"  - Standard Deviation: €{volatility:.2f}")

# Year-over-year comparison analysis
# Extract year from date index for grouping
df['Year'] = df.index.year
# Calculate average price for each year
yearly_avg = df.groupby('Year')['Close'].mean()

print(f"\n📅 Average Price by Year:")
for year, price in yearly_avg.items():
    print(f"  - {year}: €{price:.2f}")

# Calculate year-over-year percentage changes
if len(yearly_avg) > 1:
    print(f"\n📊 Year-over-Year Changes:")
    for i in range(1, len(yearly_avg)):
        prev_year = yearly_avg.index[i-1]
        curr_year = yearly_avg.index[i]
        # Calculate percentage change: ((new - old) / old) * 100
        change = ((yearly_avg.iloc[i] - yearly_avg.iloc[i-1]) / yearly_avg.iloc[i-1]) * 100
        print(f"  - {prev_year} to {curr_year}: {change:+.1f}%")

# ============================================================================
# DATA VISUALIZATION
# ============================================================================

print("\n" + "="*60)
print("3. Creating Visualizations...")
print("="*60)

# Create a figure with 4 subplots in a 2x2 grid
# figsize=(16, 11) creates a large, high-quality figure
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle('EU ETS Carbon Price Analysis (2022-2024)', fontsize=18, fontweight='bold', y=0.98)

# Adjust spacing between subplots for better readability
plt.subplots_adjust(hspace=0.35, wspace=0.25, top=0.94, bottom=0.06, left=0.08, right=0.96)

# ----------------------------------------------------------------------------
# Chart 1: Price Trend with Moving Averages (Top Left)
# ----------------------------------------------------------------------------
# This chart shows daily closing prices along with smoothed trend lines

axes[0, 0].plot(df.index, df['Close'], label='Close Price', linewidth=2, color='darkblue')
axes[0, 0].plot(df.index, df['MA_30'], label='30-day MA', linewidth=1.5, color='orange', linestyle='--')
axes[0, 0].plot(df.index, df['MA_90'], label='90-day MA', linewidth=1.5, color='red', linestyle='--')
axes[0, 0].set_title('Price Trend with Moving Averages', fontweight='bold', fontsize=12, pad=10)
axes[0, 0].set_xlabel('Date', fontsize=10)
axes[0, 0].set_ylabel('Price (€/ton)', fontsize=10)
axes[0, 0].legend(loc='best')
axes[0, 0].grid(True, alpha=0.3)

# Format x-axis to show years clearly
axes[0, 0].xaxis.set_major_locator(mdates.YearLocator())
axes[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
axes[0, 0].tick_params(axis='x', rotation=0, labelsize=9)

# ----------------------------------------------------------------------------
# Chart 2: Average Price by Year (Top Right)
# ----------------------------------------------------------------------------
# Bar chart comparing annual average carbon prices

bars = axes[0, 1].bar(yearly_avg.index.astype(str), yearly_avg.values, 
                      color=['#2E86AB', '#A23B72', '#F18F01'], width=0.6)
axes[0, 1].set_title('Average Price by Year', fontweight='bold', fontsize=12, pad=10)
axes[0, 1].set_xlabel('Year', fontsize=10)
axes[0, 1].set_ylabel('Average Price (€/ton)', fontsize=10)
axes[0, 1].tick_params(axis='x', rotation=0)
axes[0, 1].grid(True, alpha=0.3, axis='y')

# ----------------------------------------------------------------------------
# Chart 3: Price Distribution Histogram (Bottom Left)
# ----------------------------------------------------------------------------
# Shows frequency distribution of prices across different price ranges

axes[1, 0].hist(df['Close'], bins=30, color='#06A77D', edgecolor='black', alpha=0.7)
# Add vertical line showing average price for reference
axes[1, 0].axvline(average_price, color='red', linestyle='--', linewidth=2, 
                   label=f'Average: €{average_price:.2f}')
axes[1, 0].set_title('Price Distribution', fontweight='bold', fontsize=12, pad=10)
axes[1, 0].set_xlabel('Price (€/ton)', fontsize=10)
axes[1, 0].set_ylabel('Frequency (Days)', fontsize=10)
axes[1, 0].legend(loc='best')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# ----------------------------------------------------------------------------
# Chart 4: Monthly Trading Volume (Bottom Right)
# ----------------------------------------------------------------------------
# Aggregates daily volumes into monthly totals

# Resample data to monthly frequency and sum volumes
monthly_volume = df.resample('ME')['Volume'].sum()
axes[1, 1].bar(monthly_volume.index, monthly_volume.values, color='#D90368', alpha=0.7, width=20)
axes[1, 1].set_title('Monthly Trading Volume', fontweight='bold', fontsize=12, pad=10)
axes[1, 1].set_xlabel('Date', fontsize=10)
axes[1, 1].set_ylabel('Volume', fontsize=10)
axes[1, 1].grid(True, alpha=0.3, axis='y')

# Format x-axis dates
axes[1, 1].xaxis.set_major_locator(mdates.YearLocator())
axes[1, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
axes[1, 1].tick_params(axis='x', rotation=0, labelsize=9)

# Save figure as high-resolution PNG (300 DPI for professional quality)
plt.savefig('EU_ETS_Analysis_Charts.png', dpi=300, bbox_inches='tight')
print("✓ Charts created and saved as 'EU_ETS_Analysis_Charts.png'")

# Display the interactive chart window
plt.show()
print("\n✓ Analysis complete! Check the charts window.")

# ============================================================================
# REPORT GENERATION
# ============================================================================

print("\n" + "="*60)
print("4. Generating Summary Report...")
print("="*60)

# Initialize report as list of strings (will be joined later)
report = []
report.append("="*60)
report.append("EU ETS CARBON PRICE ANALYSIS REPORT")
report.append("European Emission Trading System (2022-2024)")
report.append("="*60)
report.append("")

# Executive Summary Section
report.append("EXECUTIVE SUMMARY")
report.append("-" * 60)
report.append(f"Analysis Period: {df.index.min().strftime('%Y-%m-%d')} to {df.index.max().strftime('%Y-%m-%d')}")
report.append(f"Total Trading Days Analyzed: {len(df)}")
report.append("")

# Key Findings Section
report.append("KEY FINDINGS")
report.append("-" * 60)
report.append(f"1. Current Carbon Price: €{current_price:.2f} per ton")
report.append(f"2. Average Price (3-year): €{average_price:.2f} per ton")
report.append(f"3. Price Range: €{min_price:.2f} - €{max_price:.2f}")
report.append(f"4. Price Volatility (Std Dev): €{volatility:.2f}")
report.append("")

# Trend Analysis Section
report.append("TREND ANALYSIS")
report.append("-" * 60)

# Calculate overall price change from start to end
price_change_total = ((current_price - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100

# Determine trend direction based on price change
if price_change_total > 0:
    trend = "UPWARD"
elif price_change_total < 0:
    trend = "DOWNWARD"
else:
    trend = "STABLE"

report.append(f"Overall Trend: {trend}")
report.append(f"Total Price Change: {price_change_total:+.2f}% (from start to end)")
report.append(f"30-day Moving Average: €{df['MA_30'].iloc[-1]:.2f}")
report.append(f"90-day Moving Average: €{df['MA_90'].iloc[-1]:.2f}")
report.append("")

# Yearly Comparison Section
report.append("YEARLY COMPARISON")
report.append("-" * 60)
for year, price in yearly_avg.items():
    report.append(f"{year}: €{price:.2f} average")

# Calculate and display year-over-year changes
if len(yearly_avg) > 1:
    report.append("")
    report.append("Year-over-Year Changes:")
    for i in range(1, len(yearly_avg)):
        prev_year = yearly_avg.index[i-1]
        curr_year = yearly_avg.index[i]
        change = ((yearly_avg.iloc[i] - yearly_avg.iloc[i-1]) / yearly_avg.iloc[i-1]) * 100
        report.append(f"  {prev_year} → {curr_year}: {change:+.1f}%")

# Market Insights Section
report.append("")
report.append("MARKET INSIGHTS")
report.append("-" * 60)

# Generate insights based on current vs average price
if current_price > average_price:
    report.append("• Current price is ABOVE the 3-year average, indicating recent price strength")
else:
    report.append("• Current price is BELOW the 3-year average, indicating recent price weakness")

# Analyze moving average crossover for momentum indication
if df['MA_30'].iloc[-1] > df['MA_90'].iloc[-1]:
    report.append("• Short-term trend (30-day MA) is ABOVE long-term trend (90-day MA)")
    report.append("  suggesting bullish momentum")
else:
    report.append("• Short-term trend (30-day MA) is BELOW long-term trend (90-day MA)")
    report.append("  suggesting bearish momentum")

# Identify dates of highest and lowest prices
max_date = df['Close'].idxmax().strftime('%Y-%m-%d')
min_date = df['Close'].idxmin().strftime('%Y-%m-%d')
report.append(f"• Highest price recorded: €{max_price:.2f} on {max_date}")
report.append(f"• Lowest price recorded: €{min_price:.2f} on {min_date}")

# Report Footer
report.append("")
report.append("="*60)
report.append("Report generated by EU ETS Carbon Price Analyzer")
report.append("Author: Felix Okumo")
report.append("GitHub: github.com/felixokumo1-stack/EU-ETS-Carbon-Analysis")
report.append("="*60)

# Convert report list to single string with newlines
report_text = "\n".join(report)

# Save report to text file with UTF-8 encoding (supports special characters)
with open('EU_ETS_Analysis_Report.txt', 'w', encoding='utf-8') as f:
    f.write(report_text)

print("✓ Summary report saved as 'EU_ETS_Analysis_Report.txt'")

# ============================================================================
# COMPLETION SUMMARY
# ============================================================================

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print("\nGenerated Files:")
print("  1. EU_ETS_Analysis_Charts.png - Visualization charts")
print("  2. EU_ETS_Analysis_Report.txt - Detailed text report")
print("\n✓ All files saved in the current directory")
print("\nAuthor: Felix Okumo")
print("Contact: felix.1.okumo@gmail.com")
print("GitHub: github.com/felixokumo1-stack/EU-ETS-Carbon-Analysis")

# ============================================================================
# END OF SCRIPT
# ============================================================================
# For questions, feedback, or collaboration opportunities:
# Email: felix.1.okumo@gmail.com
# GitHub: github.com/felixokumo1-stack
# 
# This project demonstrates skills in:
# - Python programming and data analysis
# - Statistical analysis and time series modeling
# - Data visualization and reporting
# - Environmental market analysis
# ============================================================================