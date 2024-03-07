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
analysis_type = st.sidebar.selectbox("Select Analysis Type:", ["Average Pollution Levels by Year", "Mean Temperature and Pressure over 5 Years", "Mean for Specific Year"])

# JUDUL STREAMLIT
st.title("Guanyuan Air Quality")

# Main content
if analysis_type == "Average Pollution Levels by Year":
    st.subheader("Average Pollution Levels by Year")
    air_polution = data_df.groupby('year')[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]].mean()
    fig, air = plt.subplots(figsize=(10, 5))
    for column in air_polution.columns:
        air.plot(air_polution.index, air_polution[column], label=column, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Average Pollution Level')
    plt.legend(title='Pollutant')
    st.pyplot(fig)

    # Polusi Udara
    def airpolution_show(df):
        pm25 = round(df['PM2.5'].mean(), 1)
        pm10 = round(df['PM10'].mean(), 0)
        SO2 = round(df['SO2'].mean(), 2)
        NO2 = round(df['NO2'].mean(), 2)
        CO = round(df['CO'].mean(), 2)
        O3 = round(df['O3'].mean(), 2)

        classification_results = []

        if (pm25 <= 15.5):
            classification_results.append("BAIK")
        elif ((pm25 >= 15.6) & (pm25 <= 55.4)):
            classification_results.append("SEDANG")
        elif ((pm25 >= 55.5) & (pm25 <= 150.4)):
            classification_results.append("TIDAK SEHAT")
        elif ((pm25 >= 150.5) & (pm25 <= 250.4)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        if (pm10 <= 50):
            classification_results.append("BAIK")
        elif ((pm10 >= 51) & (pm10 <= 150)):
            classification_results.append("SEDANG")
        elif ((pm10 >= 151) & (pm10 <= 350)):
            classification_results.append("TIDAK SEHAT")
        elif ((pm10 >= 351) & (pm10 <= 420)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        if (SO2 <= 50):
            classification_results.append("BAIK")
        elif ((SO2 >= 51) & (SO2 <= 180)):
            classification_results.append("SEDANG")
        elif ((SO2 >= 181) & (SO2 <= 400)):
            classification_results.append("TIDAK SEHAT")
        elif ((SO2 >= 401) & (SO2 <= 800)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        if (CO <= 4000):
            classification_results.append("BAIK")
        elif ((CO >= 4001) & (CO <= 8000)):
            classification_results.append("SEDANG")
        elif ((CO >= 8001) & (CO <= 15000)):
            classification_results.append("TIDAK SEHAT")
        elif ((CO >= 15001) & (CO <= 30000)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        if (O3 <= 120):
            classification_results.append("BAIK")
        elif ((O3 >= 121) & (O3 <= 235)):
            classification_results.append("SEDANG")
        elif ((O3 >= 236) & (O3 <= 400)):
            classification_results.append("TIDAK SEHAT")
        elif ((O3 >= 401) & (O3 <= 800)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        if (NO2 <= 80):
            classification_results.append("BAIK")
        elif ((NO2 >= 81) & (NO2 <= 200)):
            classification_results.append("SEDANG")
        elif ((NO2 >= 201) & (NO2 <= 1130)):
            classification_results.append("TIDAK SEHAT")
        elif ((NO2 >= 1131) & (NO2 <= 2260)):
            classification_results.append("SANGAT TIDAK SEHAT")
        else:
            classification_results.append("BERBAHAYA")

        return classification_results

elif analysis_type == "Mean Temperature and Pressure over 5 Years":
    st.subheader("Mean Temperature and Pressure over 5 Years")
    mean_air_over_5_years = data_df.groupby('year').agg({
        'TEMP': 'mean',
        'PRES': 'mean'}).reset_index()

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
    ax[0].plot(mean_air_over_5_years['year'], mean_air_over_5_years['TEMP'], marker='o', linewidth=2, color="#39064B")
    ax[0].tick_params(axis='y', labelsize=20)
    ax[0].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax[0].set_ylabel("Temperature (°C)", fontsize=25)
    ax[0].set_title("Mean Temperature", loc="center", fontsize=35)

    ax[1].plot(mean_air_over_5_years['year'], mean_air_over_5_years['PRES'], marker='o', linewidth=2, color="#39064B")
    ax[1].tick_params(axis='y', labelsize=20)
    ax[1].tick_params(axis='x', labelsize=20, labelrotation=45)
    ax[1].set_ylabel("Pressure (hPa)", fontsize=25)
    ax[1].set_title("Mean Pressure", loc="center", fontsize=35)

    fig = plt.gcf()
    st.pyplot(fig)

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
