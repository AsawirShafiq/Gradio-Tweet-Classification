import gradio as gr
import requests
import pandas as pd

# FastAPI endpoint URL
url = "http://127.0.0.1:8000/predict/"

# Function to send a tweet to the FastAPI endpoint and get the prediction
def predict(tweet_text):
    payload = {"tweet_text": tweet_text}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['predicted_label']
    else:
        return "Error in prediction"

# Create the Gradio interface
predict_iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=2, placeholder="Enter a tweet..."),
    outputs=gr.Textbox(),
    title="Cyberbullying Detection",
    description="Enter a tweet to detect if it contains cyberbullying."
)

def fetch_all_predictions():
  try:
    response = requests.get('http://127.0.0.1:8000/prediction')
    response.raise_for_status()

    predictions = response.json()
    formatted_predictions = "\n".join(
      [f"Tweet: {pred['tweet_text']}, Prediction: {pred['predicted_label']}" for pred in predictions]
    )
    return formatted_predictions
  except requests.exceptions.RequestException as e:
   return f"An error occurred: {str(e)}"


show_all_iface = gr.Interface(

    fn=fetch_all_predictions,
    inputs=None,  # No user input required
    outputs="textbox",  # Display predictions in a textbox
    title="Cyberbullying Detection Predictions",
    description="View all predictions made by the cyberbullying detection model."
)

# Define the Gradio function to handle file upload and call the API
def predict_from_csv(file):
    #print(file)
    df = pd.read_csv(file)


     # Convert the uploaded file to a format suitable for the API
    file_data = {"file": (file.name, file, "text/csv")}

    # Make a POST request to your FastAPI endpoint
    response = requests.post("http://127.0.0.1:8000/predictfromcsv/", files= file_data)

    # Check for errors in the response
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    # Parse the response from JSON to a Python list of dictionaries
    try:
        predictions = response.json()

        # Check if the response contains error information
        if 'error' in predictions:
            return f"Error: {predictions['error']}"

        # Convert the predictions to a pandas DataFrame
        if isinstance(predictions, list):
            df = pd.DataFrame(predictions)
            return df
        else:
            return "Error: Unexpected response format."

    except ValueError:
        return "Error: Unable to parse response."
# Create the Gradio interface
predictcsv_iface = gr.Interface(
    fn=predict_from_csv,  # The function to call when a file is uploaded
    inputs=gr.File(label="Upload a CSV file"),  # CSV file input
    outputs=gr.Dataframe(headers=["tweet_text", "Predicted Label"]),  # Display the DataFrame with predictions
    title="Cyberbullying Detection",
    description="Upload a CSV file to predict cyberbullying labels."
)


# Launch the Gradio interface
iface = gr.TabbedInterface([predict_iface, show_all_iface, predictcsv_iface], ["Predictions", "Show all Predictions", "Predict from csv"])
iface.launch(share=True)
