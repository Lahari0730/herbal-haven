import pandas as pd

class RemedyRecommender:
    def __init__(self, file_path='project.csv'):
        try:
            self.df = pd.read_csv(file_path)
            print("✅ CSV file loaded successfully!")
        except FileNotFoundError:
            print("❌ Error: CSV file not found. Check the file path and name.")
            exit()

    def get_remedy(self, ailment):
        ailment = ailment.lower().strip()

        # Ensure required columns exist
        required_columns = ["Disease", "Remedy Name", "Ingredients", "Preparation Method", "Usage & Dosage", "Region", "Additional Notes"]
        for col in required_columns:
            if col not in self.df.columns:
                return f"❌ Error: CSV file does not contain required column '{col}'. Check CSV headers."

        # Convert Disease column to lowercase for case-insensitive search
        self.df["Disease"] = self.df["Disease"].astype(str).str.lower().str.strip()

        # Search for the ailment in the dataset
        result = self.df[self.df["Disease"] == ailment]

        if not result.empty:
            return result[['Remedy Name', 'Ingredients', 'Preparation Method', 'Usage & Dosage', 'Region', 'Additional Notes']].to_dict(orient='records')
        else:
            return "❌ No remedy found. Please try another ailment."

# Example usage
if __name__ == "__main__":
    recommender = RemedyRecommender()
    ailment = input("\nEnter a disease to find a traditional remedy: ")
    remedies = recommender.get_remedy(ailment)

    if isinstance(remedies, str):
        print(remedies)
    else:
        print("\n✅ Remedy Found:")
        for remedy in remedies:
            print(f"\n🌿 **Remedy Name:** {remedy['Remedy Name']}")
            print(f"🍵 **Ingredients:** {remedy['Ingredients']}")
            print(f"📝 **Preparation Method:** {remedy['Preparation Method']}")
            print(f"💊 **Usage & Dosage:** {remedy['Usage & Dosage']}")
            print(f"📍 **Region:** {remedy['Region']}")
            print(f"📌 **Additional Notes:** {remedy['Additional Notes']}\n")
