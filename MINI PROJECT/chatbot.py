import pandas as pd

class RemedyChatbot:
    def __init__(self, file_path='../data/project.csv'):
        try:
            self.df = pd.read_csv(file_path)
            print("✅ CSV file loaded successfully!")
        except FileNotFoundError:
            print("❌ Error: CSV file not found. Check the file path.")
            exit()

    def get_remedy(self, disease):
        disease = disease.strip().lower()

        # ✅ Ensure 'Disease' column exists
        if "Disease" not in self.df.columns:
            return " Error: CSV file does not contain the required 'Disease' column."

        # Convert column for case-insensitive search
        self.df["Disease"] = self.df["Disease"].astype(str).str.lower().str.strip()

        # ✅ Search for the disease in the dataset
        result = self.df[self.df["Disease"] == disease]

        if not result.empty:
            responses = []
            for _, row in result.iterrows():
                response = (
                    f"\n👉 **Disease:** {row['Disease'].capitalize()}\n"
                    f"💊 **Remedy Name:** {row['Remedy Name']}\n"
                    f"🌿 **Ingredients:** {row['Ingredients']}\n"
                    f"📝 **Preparation Method:** {row['Preparation Method']}\n"
                    f"⚖️ **Usage & Dosage:** {row['Usage & Dosage']}\n"
                    f"🌍 **Region:** {row['Region']}\n"
                    f"📌 **Additional Notes:** {row['Additional Notes']}\n"
                )
                responses.append(response)
            return "\n".join(responses)
        else:
            return "No remedy found for this disease. Try another one."

# ✅ Interactive Chatbot
if __name__ == "__main__":
    chatbot = RemedyChatbot()
    print("💬 Remedy Chatbot is ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter a disease to find a remedy: ")
        if user_input.lower() == 'exit':
            print("👋 Exiting chatbot. Stay healthy!")
            break
        print(chatbot.get_remedy(user_input))
