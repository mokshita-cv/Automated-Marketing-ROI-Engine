import pandas as pd
import os
from dotenv import load_dotenv
import joblib
import mysql.connector
from mock_aws import trigger_marketing_action

model = joblib.load('xgboost_marketing_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')
print("🧠 Model & Encoder loaded into memory.")
print("-" * 60)

# Simulate a new customer session data hitting our server
new_customer_features = {
    'Recency': [180],            # 6 months since last purchase
    'Frequency': [1],            # Only bought once
    'Monetary': [20],            # Only spent $20 total
    'Avg_Order_Value': [20],
    'Session_Count': [2],
    'Avg_Session_Duration': [1.5],
    'Pages_Viewed': [2],
    'Clicks': [5],
    'Campaign_Response': [0],    # Ignored the last marketing campaign
    'Wishlist_Adds': [0],
    'Cart_Abandon_Rate': [95.0], # Almost always abandons cart
    'Returns': [0]
}
customer_name = "Customer_B"     # Change name to Customer_B
customer_df = pd.DataFrame(new_customer_features)

# Predict the customer segment
encoded_prediction = model.predict(customer_df)
decoded_segment = label_encoder.inverse_transform(encoded_prediction)[0]
print(f" XGBoost Model Classification: '{decoded_segment}'")

# TRIGGER THE ACTION AND CAPTURE THE RESULT
# Because mock_aws now returns the text, this variable automatically holds the correct campaign message!
action_text = trigger_marketing_action(customer_name=customer_name, predicted_segment=decoded_segment)

print("-" * 60)
print("💾 Logging automation record to local MySQL Database...")

# Insert the record into MySQL
# Load the hidden environment variables
load_dotenv()
try:
    conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
    cursor = conn.cursor()
    
    insert_query = """
        INSERT INTO marketing_logs (customer_name, segment, action_executed) 
        VALUES (%s, %s, %s)
    """
    record_data = (customer_name, decoded_segment, action_text)
    
    cursor.execute(insert_query, record_data)
    conn.commit()
    
    print("✅ SQL Transaction Committed Successfully!")
    
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Database Logging Error: {err}")