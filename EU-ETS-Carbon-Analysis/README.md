# EU ETS Carbon Price Analysis

A comprehensive data analysis project examining European Emission Trading System (EU ETS) carbon allowance prices from 2022-2024, featuring both interactive PowerBI dashboards and Python-based statistical analysis.

**Author:** Felix Okumo  
**Contact:** felix.1.okumo@gmail.com  
**GitHub:** [@felixokumo1-stack](https://github.com/felixokumo1-stack)

## 📊 Project Overview

This project analyzes three years of EU ETS carbon pricing data to identify trends, calculate key market indicators, and generate actionable insights for environmental market analysis. Built as part of preparation for working student positions in environmental markets and energy analysis.

## 🎯 Key Features

### PowerBI Dashboard
- Interactive visualization of carbon price trends (2022-2024)
- Real-time key metrics (current price, average price, total trading volume)
- Trading volume analysis over time
- Professional, clean dashboard design suitable for stakeholder presentations

### Python Analyzer
- Automated statistical analysis of carbon prices
- Moving average calculations (30-day and 90-day)
- Price volatility and trend analysis
- Year-over-year comparison with percentage changes
- Automated generation of professional charts and insights reports
- High-resolution visualizations (300 DPI) suitable for reports

## 📈 Key Findings

- **Overall Trend**: Upward trajectory with +27% price increase over 3 years
- **Current Price**: €101.73 per ton (as of analysis end date)
- **Price Range**: €78.17 - €111.49 over the analysis period
- **Volatility**: Standard deviation of €8.43
- **Yearly Growth**: Consistent year-over-year increases
  - 2022→2023: +10.8%
  - 2023→2024: +6.4%
- **Market Momentum**: Bullish, with short-term MA above long-term MA
- **Trading Activity**: 782 trading days analyzed with consistent volume

## 🛠️ Technologies Used

- **Python 3.14**
  - pandas (data manipulation and analysis)
  - matplotlib (data visualization)
  - numpy (numerical computations)
- **PowerBI Desktop** (interactive dashboards and business intelligence)
- **Data Processing**: Time series analysis, statistical calculations, trend modeling

## 📁 Project Structure

```
EU-ETS-Carbon-Analysis/
│
├── PowerBI/
│   └── EU_ETS_Carbon_Dashboard.pbix
│
├── Python/
│   ├── carbon_price_analyzer.py          # Main analysis script
│   ├── EU_ETS_Carbon_Prices_2022-2024.csv # Sample dataset
│   ├── EU_ETS_Analysis_Charts.png        # Generated visualizations
│   └── EU_ETS_Analysis_Report.txt        # Analysis report
│
├── README.md                              # This file
└── LICENSE                                # MIT License
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- PowerBI Desktop (for dashboard viewing)
- Basic understanding of command line operations

### Installation

1. **Clone this repository**
```bash
git clone https://github.com/felixokumo1-stack/EU-ETS-Carbon-Analysis.git
cd EU-ETS-Carbon-Analysis
```

2. **Install required Python packages**
```bash
pip install pandas matplotlib numpy
```

Or use pip3 if you have multiple Python versions:
```bash
pip3 install pandas matplotlib numpy
```

3. **Run the Python analyzer**
```bash
cd Python
python carbon_price_analyzer.py
```

### Viewing the PowerBI Dashboard
1. Open PowerBI Desktop
2. Navigate to `PowerBI/EU_ETS_Carbon_Dashboard.pbix`
3. Click "Open"
4. Explore the interactive visualizations

## 📊 Visualizations

The Python analyzer generates four key visualizations:

1. **Price Trend with Moving Averages** - Line chart showing daily closing prices with 30-day and 90-day moving averages overlay for trend identification
2. **Average Price by Year** - Bar chart comparing annual average prices across 2022-2024
3. **Price Distribution** - Histogram showing price frequency distribution with average price indicator
4. **Monthly Trading Volume** - Bar chart of aggregated monthly trading volumes over time

All charts are saved as high-resolution PNG (300 DPI) suitable for professional reports and presentations.

## 📄 Output Files

The Python script automatically generates:
- `EU_ETS_Analysis_Charts.png` - High-resolution visualization (300 DPI, suitable for printing)
- `EU_ETS_Analysis_Report.txt` - Detailed text report with:
  - Executive summary
  - Key findings and statistics
  - Trend analysis
  - Year-over-year comparisons
  - Market insights and recommendations

## 🎓 Skills Demonstrated

- **Data Analysis**: Statistical analysis, time series modeling, trend identification
- **Programming**: Clean, well-documented Python code with proper structure
- **Data Visualization**: Creating clear, professional charts and dashboards
- **Business Intelligence**: PowerBI dashboard design and interactive reporting
- **Market Analysis**: Understanding emission trading mechanisms and price dynamics
- **Technical Documentation**: Comprehensive README and code comments
- **Problem Solving**: Identifying insights from raw data

## 💡 Use Cases

This analysis framework can be applied to:
- Environmental market monitoring and surveillance
- Carbon trading strategy development
- Regulatory impact assessment and policy analysis
- Investment decision support for carbon-intensive industries
- Market trend forecasting and price prediction
- Academic research in environmental economics
- Corporate sustainability reporting

## 📚 Learning Outcomes

Through building this project, I gained experience in:
- Working with real-world financial time series data
- Implementing moving averages and volatility calculations
- Creating professional data visualizations
- Automating report generation
- Understanding EU ETS market dynamics
- Building reproducible analysis pipelines

## 🔮 Future Enhancements

Potential improvements and extensions:
- [ ] Add UK ETS data for comparative analysis
- [ ] Implement predictive modeling (ARIMA, Prophet)
- [ ] Create web dashboard using Streamlit or Dash
- [ ] Add correlation analysis with energy prices
- [ ] Include regulatory event markers
- [ ] Automate data updates from live sources
- [ ] Add export functionality for different formats (PDF, Excel)

## 📧 Contact

**Felix Okumo**  
- Email: felix.1.okumo@gmail.com
- GitHub: [@felixokumo1-stack](https://github.com/felixokumo1-stack)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile)

Feel free to reach out for:
- Questions about the project
- Collaboration opportunities
- Feedback and suggestions
- Job opportunities in environmental markets or data analysis

## 📝 License

This project is open source and available under the MIT License. See LICENSE file for details.

## 🙏 Acknowledgments

- Data analysis methodology inspired by environmental market research
- Project developed as part of job application preparation for working student positions in environmental markets analysis
- Built with guidance from modern data science best practices

## 📌 Project Status

**Status:** Complete and fully functional ✅  
**Last Updated:** January 2026  
**Version:** 1.0

---

⭐ **If you found this project helpful or interesting, please consider giving it a star!**

💬 **Questions or feedback?** Open an issue or reach out directly via email.

🤝 **Looking for collaboration?** I'm open to working on environmental markets, climate tech, or data analysis projects.