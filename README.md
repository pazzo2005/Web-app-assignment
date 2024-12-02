Dynamic Data Visualization App with GPT-2 Integration
This project is a Streamlit-based web application that lets users upload a CSV file and dynamically generate data visualizations. Instead of relying on external APIs, it integrates GPT-2 (via Hugging Face Transformers) to interpret user prompts and create visualizations accordingly.

Features
Interactive File Upload: Upload CSV files to visualize your data dynamically.
AI-Powered Prompt Interpretation: Use GPT-2 to interpret natural language prompts like:
Create a bar chart with X as Age and Y as Salary.
Visualization Options:
Bar Charts
Line Charts
Scatter Plots
Boxplots

Installation
Prerequisites
Python 3.8 or later
Virtual environment (optional but recommended)

Steps
Clone the repository or copy the project files:

git clone https://github.com/your-repo/data-visualization-gpt2.git
cd data-visualization-gpt2



Create a virtual environment:

python -m venv venv
source venv/bin/activate



Install the required dependencies:

pip install -r requirements.txt


Run the application:

streamlit run app.py



Open your browser and navigate to the URL shown in the terminal (usually http://localhost:8501).

Usage
Upload a CSV File: Use the "Browse files" button to upload your dataset in CSV format.
Enter a Prompt: In the input box, describe the chart you want, e.g.:
Create a scatter plot with X as Years of Experience and Y as Salary.
Generate the Graph: Click "Generate Graph" to view the visualization.
Review the AI Response: The app will display the interpreted response from GPT-2 before rendering the chart.


Example Prompts
"Make a bar chart of Sales by Month."
"Create a line chart with Date on the X-axis and Revenue on the Y-axis."
"Show a scatter plot comparing Age and Salary."
"Generate a boxplot for Salary grouped by Department."


File Structure
data-visualization-gpt2/
│
├── app.py              # Main application code
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── sample_data.csv     # Optional: Example dataset


Dependencies
The following Python libraries are required:

streamlit: For building interactive web apps.
pandas: For data manipulation and analysis.
plotly: For creating rich, interactive visualizations.
transformers: To load and use GPT-2 for prompt interpretation.
torch: Backend library for running GPT-2.
These dependencies are included in the requirements.txt file.



Troubleshooting
Common Issues
Model Loading Errors:

Ensure the transformers and torch libraries are installed correctly.
Verify you have a stable internet connection for downloading the GPT-2 model on the first run.
Chart Generation Issues:

Double-check the column names in your dataset.
Provide a clear and concise prompt.
Performance:

GPT-2 inference may be slow on CPUs. For faster performance, install PyTorch with CUDA support if you have a compatible GPU.

Contact
For support or collaboration, feel free to reach out:

Name: Aditya NB
mail-id:adityanb.it2023@gmail.com
GitHub: https://github.com/pazzo2005
