from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ✅ Set correct file path
file_path = "project.csv"  # Change to "data/project.csv" if needed

# ✅ Check if CSV file exists
if not os.path.exists(file_path):
    print("Error: CSV file not found. Check the file path.")
    exit()

try:
    df = pd.read_csv(file_path)
    print("✅ CSV file loaded successfully!")
except Exception as e:
    print(f" Error reading CSV file: {e}")
    exit()

@app.route('/get_remedy', methods=['GET'])
def get_remedy():
    disease = request.args.get('disease', '').strip().lower()

    # ✅ Ensure 'Disease' column exists
    expected_columns = ["Disease", "Remedy Name", "Ingredients", "Preparation Method", "Usage & Dosage", "Region", "Additional Notes"]
    for col in expected_columns:
        if col not in df.columns:
            return jsonify({'error': f"CSV file does not contain the required column: '{col}'"})

    # ✅ Convert column for case-insensitive search
    df["Disease"] = df["Disease"].astype(str).str.lower().str.strip()

    # ✅ Search for the disease in the dataset
    result = df[df["Disease"] == disease]

    if not result.empty:
        remedies = result[expected_columns].to_dict(orient='records')
        return jsonify({'remedies': remedies})
    else:
        return jsonify({'message': "No remedy found. Try another disease."})

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)