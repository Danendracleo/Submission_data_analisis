import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    data_df = pd.read_csv("https://raw.githubusercontent.com/Danendracleo/Guanyuan.csv/main/PRSA_Data_Guanyuan_20130301-20170228.csv")
    return data_df

data_df = load_data()

# Sidebar
analysis_type = st.sidebar.selectbox("Select Analysis Type:", ["Mean for 5 Years", "Mean for Specific Year"])

# JUDUL STREAMLIT
st.title("Guanyuan Air Quality")

# Main content
if analysis_type == "Mean for 5 Years":
    st.subheader("Mean Pollution and Temperature/Pressure Trend for 5 Years")

    # Air Pollution
    air_polution_5_years = data_df.groupby('month')[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
    fig_air_5_years, air_5_years = plt.subplots(figsize=(10, 5))
    for column in air_polution_5_years.columns:
        air_5_years.plot(air_polution_5_years.index, air_polution_5_years[column], label=column, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Average Pollution Level')
    plt.legend(title='Pollutant')
    st.pyplot(fig_air_5_years)

    # Mean Temperature and Pressure
    mean_air_5_years = data_df.groupby('month').agg({
        'TEMP': 'mean',
        'PRES': 'mean'}).reset_index()

    fig_temp_pressure_5_years, ax_5_years = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax_5_years[0].plot(mean_air_5_years['month'], mean_air_5_years['TEMP'], marker='o', linewidth=2, color="#39064B")
    ax_5_years[0].tick_params(axis='y', labelsize=20)
    ax_5_years[0].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax_5_years[0].set_ylabel("Temperature (°C)", fontsize=25)
    ax_5_years[0].set_title("Mean Temperature", loc="center", fontsize=35)

    ax_5_years[1].plot(mean_air_5_years['month'], mean_air_5_years['PRES'], marker='o', linewidth=2, color="#39064B")
    ax_5_years[1].tick_params(axis='y', labelsize=20)
    ax_5_years[1].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax_5_years[1].set_ylabel("Pressure (hPa)", fontsize=25)
    ax_5_years[1].set_title("Mean Pressure", loc="center", fontsize=35)

    fig_temp_pressure_5_years.tight_layout(pad=2.0)
    plt.suptitle("Mean Trend of Temperature and Pressure for 5 Years in Guanyuan", fontsize=45, y=1.05)
    st.pyplot(fig_temp_pressure_5_years)

elif analysis_type == "Mean for Specific Year":
    selected_year = st.sidebar.selectbox("Select Year:", data_df["year"].unique())
    selected_year_data = data_df[data_df["year"] == selected_year]

    st.subheader(f"Mean Pollution and Temperature/Pressure Trend for {selected_year}")

    # Air Pollution
    air_polution_specific_year = selected_year_data.groupby('month')[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
    fig_air_specific_year, air_specific_year = plt.subplots(figsize=(10, 5))
    for column in air_polution_specific_year.columns:
        air_specific_year.plot(air_polution_specific_year.index, air_polution_specific_year[column], label=column, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Average Pollution Level')
    plt.legend(title='Pollutant')
    st.pyplot(fig_air_specific_year)

    # Mean Temperature and Pressure
    mean_air_specific_year = selected_year_data.groupby('month').agg({
        'TEMP': 'mean',
        'PRES': 'mean'}).reset_index()

    fig_temp_pressure_specific_year, ax_specific_year = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax_specific_year[0].plot(mean_air_specific_year['month'], mean_air_specific_year['TEMP'], marker='o', linewidth=2, color="#39064B")
    ax_specific_year[0].tick_params(axis='y', labelsize=20)
    ax_specific_year[0].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax_specific_year[0].set_ylabel("Temperature (°C)", fontsize=25)
    ax_specific_year[0].set_title("Mean Temperature", loc="center", fontsize=35)

    ax_specific_year[1].plot(mean_air_specific_year['month'], mean_air_specific_year['PRES'], marker='o', linewidth=2, color="#39064B")
    ax_specific_year[1].tick_params(axis='y', labelsize=20)
    ax_specific_year[1].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax_specific_year[1].set_ylabel("Pressure (hPa)", fontsize=25)
    ax_specific_year[1].set_title("Mean Pressure", loc="center", fontsize=35)

    fig_temp_pressure_specific_year.tight_layout(pad=2.0)
    plt.suptitle(f"Mean Trend of Temperature and Pressure for {selected_year} in Guanyuan", fontsize=45, y=1.05)
    st.pyplot(fig_temp_pressure_specific_year)
