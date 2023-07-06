import pandas as pd
import plotly.express as px
solar_df = pd.read_csv('data/Solar Data.csv',delimiter=',')
# Convert 'Date' column to datetime type
solar_df['Date'] = pd.to_datetime(solar_df['Time'], format='%m/%d/%Y %H:%M')

# Extract year from 'Date' column
solar_df['Year'] = solar_df['Date'].dt.year

# Extract year from 'Month' column
solar_df['Month'] = solar_df['Date'].dt.strftime('%b')


# Extract year and month, and format month as three-letter abbreviation
solar_df['Year_Month'] = solar_df['Date'].dt.strftime('%b-%Y')

solar_line = px.line (solar_df,x='Time',y='gen',title = f'Solar Generation')

