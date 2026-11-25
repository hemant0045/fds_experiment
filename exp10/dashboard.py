import streamlit as st
import requests

st.title("Student Performance Prediction")

st.write(
    "Predict student academic performance "
    "using Machine Learning."
)

age = st.number_input(
    "Age", 15, 22, 17
)

studytime = st.selectbox(
    "Study Time", [1, 2, 3, 4]
)

absences = st.number_input(
    "Absences", 0, 100, 2
)

G1 = st.number_input(
    "First Period Grade", 0, 20, 10
)

G2 = st.number_input(
    "Second Period Grade", 0, 20, 10
)

if st.button("Predict Performance"):

    data = {
        "age": age,
        "studytime": studytime,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:
        result = response.json()

        st.success(
            "Predicted Final Grade: "
            + str(result["predicted_final_grade"])
        )
    else:
        st.error(response.text)