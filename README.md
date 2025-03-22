📄 Company Brochure Generator

This project is an AI-powered tool that analyzes company websites and generates a short brochure in markdown format. It extracts relevant information such as company culture, careers, and customer details, making it useful for prospective customers, investors, and recruits.

🚀 Features

Website Scraping: Extracts website content, including title, text, and links.

AI-Powered Analysis: Uses OpenAI's API to generate a structured brochure.

Smart Link Filtering: Identifies and selects relevant links (e.g., About, Careers pages).

Streaming Output: Displays AI-generated content dynamically in the terminal.

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/company-brochure-generator.git
cd company-brochure-generator

2️⃣ Install Dependencies

pip install -r requirements.txt

🔧 Configuration

Set up OpenAI API access:

Add your OpenAI API key to a .env or config.py file.

Ensure the MODEL variable is correctly set.

Modify config.py (if applicable)

MODEL = "gpt-4o-mini"  # Adjust the model as needed

🏃 Usage

Run the script and follow the prompts:

python main.py

Example Input

Enter the company Name: OpenAI
Enter the company Website: openai.com

Example Output (Markdown Brochure)

# OpenAI

## About the Company
OpenAI is a research company dedicated to ensuring that artificial intelligence benefits all of humanity...

## Careers
OpenAI is hiring for various roles in AI research, engineering, and policy...

🛠️ Project Structure

📂 company-brochure-generator
├── 📜 main.py          # Main script to generate the brochure
├── 📜 llm.py           # AI processing and streaming logic
├── 📜 scraper.py       # Website scraping logic
├── 📜 config.py        # Configuration settings (e.g., API keys, model selection)
├── 📜 requirements.txt # Dependencies
└── 📜 README.md        # Project documentation

📝 TODO / Future Enhancements

✅ Improve link selection logic for better relevance.

✅ Implement multi-page scraping for more detailed brochures.

🚀 Add support for saving brochures as PDF or HTML.

🚀 Develop a web-based UI for user interaction.

📜 License

This project is open-source and available under the MIT License.

🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

📞 Contact

For questions or suggestions, reach out via your-email@example.com.

