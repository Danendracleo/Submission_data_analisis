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
analysis_type = st.sidebar.selectbox("Select Analysis Type:", ["Average Pollution Levels and Temperature/Pressure Trend for Each Year", "Mean for Specific Year"])

# JUDUL STREAMLIT
st.title("Guanyuan Air Quality")

# Main content
if analysis_type == "Average Pollution Levels and Temperature/Pressure Trend for Each Year":
    st.subheader("Average Pollution Levels and Temperature/Pressure Trend for Each Year")

    for year in data_df["year"].unique():
        st.subheader(f"Year {year}")
        
        # Air Pollution
        air_polution = data_df[data_df["year"] == year].groupby('month')[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
        fig_air, air = plt.subplots(figsize=(10, 5))
        for column in air_polution.columns:
            air.plot(air_polution.index, air_polution[column], label=column, marker='o')
        plt.xlabel('Month')
        plt.ylabel('Average Pollution Level')
        plt.legend(title='Pollutant')
        st.pyplot(fig_air)

        # Mean Temperature and Pressure
        mean_air_for_year = data_df[data_df["year"] == year].groupby('month').agg({
            'TEMP': 'mean',
            'PRES': 'mean'}).reset_index()

        fig_temp_pressure, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
        ax[0].plot(mean_air_for_year['month'], mean_air_for_year['TEMP'], marker='o', linewidth=2, color="#39064B")
        ax[0].tick_params(axis='y', labelsize=20)
        ax[0].tick_params(axis='x', labelsize=20, labelrotation=45)
        ax[0].set_ylabel("Temperature (°C)", fontsize=25)
        ax[0].set_title("Mean Temperature", loc="center", fontsize=35)

        ax[1].plot(mean_air_for_year['month'], mean_air_for_year['PRES'], marker='o', linewidth=2, color="#39064B")
        ax[1].tick_params(axis='y', labelsize=20)
        ax[1].tick_params(axis='x', labelsize=20, labelrotation=45)
        ax[1].set_ylabel("Pressure (hPa)", fontsize=25)
        ax[1].set_title("Mean Pressure", loc="center", fontsize=35)

        fig_temp_pressure.tight_layout(pad=2.0)
        plt.suptitle(f"Mean Trend of Temperature and Pressure for Year {year} in Guanyuan", fontsize=45, y=1.05)
        st.pyplot(fig_temp_pressure)

elif analysis_type == "Mean for Specific Year":
    selected_year = st.sidebar.selectbox("Select Year:", data_df["year"].unique())
    selected_year_data = data_df[data_df["year"] == selected_year]

    st.subheader(f"Mean Temperature and Pressure for {selected_year}")
    mean_air_for_year = selected_year_data.groupby('month').agg({
        'TEMP': 'mean',
        'PRES': 'mean'}).reset_index()

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax[0].plot(mean_air_for_year['month'], mean_air_for_year['TEMP'], marker='o', linewidth=2, color="#39064B")
    ax[0].tick_params(axis='y', labelsize=20)
    ax[0].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax[0].set_ylabel("Temperature (°C)", fontsize=25)
    ax[0].set_title("Mean Temperature", loc="center", fontsize=35)

    ax[1].plot(mean_air_for_year['month'], mean_air_for_year['PRES'], marker='o', linewidth=2, color="#39064B")
    ax[1].tick_params(axis='y', labelsize=20)
    ax[1].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax[1].set_ylabel("Pressure (hPa)", fontsize=25)
    ax[1].set_title("Mean Pressure", loc="center", fontsize=35)

    fig.tight_layout(pad=2.0)
    plt.suptitle(f"Mean Trend of Temperature and Pressure for {selected_year} in Guanyuan", fontsize=45, y=1.05)
    st.pyplot(fig)

