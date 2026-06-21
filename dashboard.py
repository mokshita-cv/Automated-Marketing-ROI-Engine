import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector
import streamlit as st

# Set up the web page title and icon
st.set_page_config(page_title="Marketing ROI Engine", page_icon="📊", layout="wide")

st.title("📊 Automated Marketing ROI Engine")
st.markdown("### Real-Time AI Customer Segmentation & Cloud Automation Logs")
st.markdown("---")

# Load the hidden environment variables
load_dotenv()

def fetch_data_from_mysql():
    """
    Establishes a connection to the local MySQL server 
    and fetches all records from the marketing_logs table.
    """
    try:
        conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
        # Use pandas to read the SQL query directly into a DataFrame
        query = "SELECT * FROM marketing_logs ORDER BY timestamp DESC"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except mysql.connector.Error as err:
        st.error(f"❌ Database Connection Error: {err}")
        return pd.DataFrame()

# Fetch the live data
df = fetch_data_from_mysql()

if not df.empty:
    # 1. Top-level Key Performance Indicators (KPIs)
    total_actions = len(df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🚀 Total Automations Triggered", value=total_actions)
    with col2:
        # Count unique customers targeted
        unique_customers = df['customer_name'].nunique()
        st.metric(label="👥 Unique Customers Processed", value=unique_customers)
        
    st.markdown("---")
    
    # 2. Split view: Chart on the left, Raw Data table on the right
    col_chart, col_table = st.columns([1, 1])
    
    with col_chart:
        st.subheader("📈 Distribution of Customer Segments")
        segment_counts = df['segment'].value_counts()
        # Display a native Streamlit bar chart of the segments
        st.bar_chart(segment_counts)
        
    with col_table:
        st.subheader("📋 Live Automation Logs")
        # Display the interactive data table
        st.dataframe(df, use_container_width=True)

else:
    st.warning("⚠️ No logs found in the database. Run your 'app.py' script to generate a customer record!")