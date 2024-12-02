import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load GPT-2 model and tokenizer
@st.cache_resource
def load_gpt2():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    return tokenizer, model

tokenizer, model = load_gpt2()

# Function to generate text with GPT-2
def generate_response(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# App title
st.title("Dynamic Data Visualization App with GPT-2 Integration")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Uploaded Dataset:")
    st.dataframe(df)

    # Text input for user prompt
    user_prompt = st.text_input("Describe the graph you want (e.g., 'Create a bar chart with X as Age and Y as Salary'):")

    # Generate graph button
    if st.button("Generate Graph"):
        if user_prompt:
            try:
                # Generate response using GPT-2
                prompt = f"The dataset columns are: {', '.join(df.columns)}. {user_prompt}. What type of chart is needed?"
                gpt2_response = generate_response(prompt)
                st.write("GPT-2's Interpretation:", gpt2_response)

                # Parse GPT-2's response (you may need to fine-tune this part based on response format)
                # Example response: "Bar chart with X as Age and Y as Salary"
                if "bar" in gpt2_response.lower():
                    chart_type = "Bar"
                elif "line" in gpt2_response.lower():
                    chart_type = "Line"
                elif "scatter" in gpt2_response.lower():
                    chart_type = "Scatter"
                elif "box" in gpt2_response.lower():
                    chart_type = "Boxplot"
                else:
                    st.warning("Could not determine chart type from GPT-2's response.")
                    chart_type = None

                # Extract columns (you may need additional NLP parsing for column names)
                x_axis = df.columns[0]  # Default to first column if GPT-2 doesn't specify
                y_axis = df.columns[1] if len(df.columns) > 1 else None

                # Generate the chart
                if chart_type == "Bar":
                    fig = px.bar(df, x=x_axis, y=y_axis)
                elif chart_type == "Line":
                    fig = px.line(df, x=x_axis, y=y_axis)
                elif chart_type == "Scatter":
                    fig = px.scatter(df, x=x_axis, y=y_axis)
                elif chart_type == "Boxplot":
                    fig = px.box(df, x=x_axis, y=y_axis)
                else:
                    st.error("Unable to generate chart due to insufficient details.")

                # Display the graph
                if chart_type:
                    st.plotly_chart(fig)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt to generate a graph.")

# Inform user to upload a file
else:
    st.info("Please upload a CSV file to proceed.")
