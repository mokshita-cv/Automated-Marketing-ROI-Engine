import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import xgboost as xgb

# 1. Load the dataset
file_name = 'ecommerce_data.csv'  
df = pd.read_csv(file_name)

print("⚙️ Preparing data for training...")

# 2. Separate our Features (X) from our Target Label (y)
# We drop 'Customer_ID' because it's just a random string name, not a mathematical clue.
# We drop 'Segment_Label' because that's what we are trying to predict!
X = df.drop(columns=['Customer_ID', 'Segment_Label'])
y = df['Segment_Label']

# 3. Convert text labels (Gold, Silver, etc.) into numbers (0, 1, 2, 3, 4)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 4. Split data into Training set (80%) and Testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

print(f"📈 Split complete. Training rows: {X_train.shape[0]} | Testing rows: {X_test.shape[0]}")
print("🧠 Training the XGBoost Classifier model (this might take a few seconds)...")

# 5. Initialize and train the high-performance XGBoost model
model = xgb.XGBClassifier(
    objective='multi:softprob', 
    num_class=5, 
    random_state=42,
    eval_metric='mlogloss'
)
model.fit(X_train, y_train)

# 6. Evaluate how well our model performs on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n🎯 MODEL TRAINING COMPLETED!")
print("=" * 50)
print(f"📊 Overall Model Accuracy: {accuracy * 100:.2f}%")
print("=" * 50)

# Print a breakdown of performance per segment
print("📋 Detailed Class Performance Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# 7. Save the trained model and the label encoder to disk
joblib.dump(model, 'xgboost_marketing_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
print("💾 Model and Label Encoder saved successfully to your folder!")