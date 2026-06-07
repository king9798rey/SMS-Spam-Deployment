# Streamlit UI
import streamlit as st

# To call FastAPI endpoint
import requests

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------

st.title("📩 SMS Spam Detection")

st.write(
    "Enter a message and check whether it is Spam or Not Spam."
)

# ---------------------------------------------------
# User Input
# ---------------------------------------------------

message = st.text_area(
    "Enter SMS Message"
)

# ---------------------------------------------------
# Predict Button
# ---------------------------------------------------

if st.button("Predict"):

    # Validation

    if message.strip() == "":
        st.warning(
            "Please enter a message."
        )

    else:

        # FastAPI endpoint

        url = (
            "http://127.0.0.1:8000/predict"
        )

        # Request body

        payload = {
            "text": message
        }

        try:

            # Send POST request

            response = requests.post(
                url,
                json=payload
            )

            # Convert response to JSON

            result = response.json()

            prediction = result[
                "prediction"
            ]

            # Display result

            if prediction == "Spam":

                st.error(
                    f"🚨 {prediction}"
                )

            else:

                st.success(
                    f"✅ {prediction}"
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )