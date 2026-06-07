# FastAPI framework
from fastapi import FastAPI

# Used for request body validation
from pydantic import BaseModel

# Load saved ML model
import joblib

# ---------------------------------------------------
# Load trained model and vectorizer only once
# when server starts
# ---------------------------------------------------

model = joblib.load("spam_classifier_model.pkl")

vectorizer = joblib.load("count_vectorizer.pkl")

# ---------------------------------------------------
# Create FastAPI application
# ---------------------------------------------------

app = FastAPI(
    title="SMS Spam Detection API",
    description="Predict whether an SMS is Spam or Not Spam",
    version="1.0"
)

# ---------------------------------------------------
# Request body schema
#
# Expected JSON:
# {
#   "text":"Free recharge offer"
# }
# ---------------------------------------------------

class Message(BaseModel):
    text: str


# ---------------------------------------------------
# Home route
# Used to check whether API is running
# ---------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "SMS Spam Detection API Running Successfully"
    }


# ---------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------

@app.post("/predict")
def predict_spam(data: Message):

    # Convert text into numerical vector

    transformed_sms = vectorizer.transform(
        [data.text]
    )

    # Model prediction

    prediction = model.predict(
        transformed_sms
    )[0]

    # Convert numeric output to label

    result = (
        "Spam"
        if prediction == 1
        else "Not Spam"
    )

    return {
        "input_text": data.text,
        "prediction": result
    }