from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# ✅ Load CSV file properly
try:
    df = pd.read_csv('data/project.csv')  # Ensure the file exists in the 'data' folder
    print("✅ CSV file loaded successfully!")
except FileNotFoundError:
    print("❌ Error: CSV file not found. Check the file path.")
    exit()

@app.route('/get_remedy', methods=['GET'])
def get_remedy():
    disease = request.args.get('disease', '').strip().lower()

    # ✅ Ensure 'Disease' column exists
    if "Disease" not in df.columns:
        return jsonify({'error': "CSV file does not contain the required 'Disease' column."})

    # Convert column for case-insensitive search
    df["Disease"] = df["Disease"].astype(str).str.lower().str.strip()

    # ✅ Search for the disease in the dataset
    result = df[df["Disease"] == disease]

    if not result.empty:
        remedies = result[["Disease", "Remedy Name", "Ingredients", "Preparation Method", "Usage & Dosage", "Region", "Additional Notes"]].to_dict(orient='records')
        return jsonify({'remedies': remedies})
    else:
        return jsonify({'message': "No remedy found. Try another disease."})

if __name__ == '__main__':
    app.run(debug=True)
