# 📌 Import required libraries
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 📌 Load dataset
file_path = r"C:\Users\Vigasini\Downloads\Updated_HDHI_Admission_Data_Cleaned.csv"
df = pd.read_csv(file_path)

# 📌 Define features and target
features = ["AGE", "SMOKING ", "ALCOHOL", "DM", "HTN", "CAD", "PRIOR CMP", "CKD", "HB", "TLC",
            "PLATELETS", "GLUCOSE", "UREA", "CREATININE", "BNP", "RAISED CARDIAC ENZYMES", "EF",
            "SEVERE ANAEMIA", "ANAEMIA", "STABLE ANGINA", "ACS", "STEMI", "ATYPICAL CHEST PAIN",
            "HEART FAILURE", "HFREF", "HFNEF", "VALVULAR", "CHB", "SSS", "AKI", "CVA INFRACT",
            "CVA BLEED", "AF", "VT", "PSVT", "CONGENITAL", "UTI", "NEURO CARDIOGENIC SYNCOPE",
            "ORTHOSTATIC", "INFECTIVE ENDOCARDITIS", "DVT", "CARDIOGENIC SHOCK", "SHOCK",
            "PULMONARY EMBOLISM", "CHEST INFECTION", "HIGH_RISK_SCORE", "GENDER_M", "RURAL_U",
            "TYPE OF ADMISSION-EMERGENCY/OPD_O", "Internal_Bleeding_Location_None"]

target = "INJURY_LABEL"

# 📌 Remove missing values
df = df.dropna(subset=features + [target])

# 📌 Initialize label encoder
label_encoder = None  # Ensures it exists even if not used

# 📌 Encode target variable if categorical
if df[target].dtype == 'object':
    label_encoder = LabelEncoder()
    df[target] = label_encoder.fit_transform(df[target])
    joblib.dump(label_encoder, "injury_label_encoder.pkl")
    class_labels = label_encoder.classes_
else:
    class_labels = sorted(df[target].unique())  # Use numerical labels directly

# 📌 Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df[features], df[target], test_size=0.2, random_state=42, stratify=df[target]
)

# 📌 Train RandomForest Model
rf_model = RandomForestClassifier(n_estimators=300, max_depth=15, min_samples_split=5, random_state=42)
rf_model.fit(X_train, y_train)

# 📌 Predictions & Accuracy
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2%}")
print(classification_report(y_test, y_pred))

# 📌 Save model
joblib.dump(rf_model, "injury_severity_model.pkl")
print("🚀 Model saved as 'injury_severity_model.pkl'")

# 📌 Confusion Matrix Visualization (Fixed)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

# 📌 Feature Importance Analysis
feature_importance = rf_model.feature_importances_
feature_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
feature_df = feature_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=feature_df['Importance'], y=feature_df['Feature'], palette="coolwarm")
plt.xlabel("Feature Importance Score")
plt.ylabel("Features")
plt.title("Feature Importance Ranking")
plt.show()

# 📌 Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df[features].corr(), cmap="coolwarm", annot=False, linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# 📌 Cross-Validation for Model Stability
cross_val_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
print(f"📊 Cross-Validation Accuracy: {np.mean(cross_val_scores):.2%} ± {np.std(cross_val_scores):.2%}")
