# fds experiment

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hemant0045/fds_experiment.git
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```


4. Install dependencies:

```bash
pip install -r requirements.txt
```


# FDS Experiment 10

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hemant0045/fds_experiment.git
```

2. Navigate to the project directory:

```bash
cd exp10
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Process for exp10

1. Run the Jupyter Notebook:

```bash
jupyter notebook
```

Open `exp10.ipynb` and execute all cells to train the model and save the required files.

2. Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

3. Open a new terminal and activate the virtual environment:

```bash
venv\Scripts\activate
```

4. Run the Streamlit dashboard:

```bash
python -m streamlit run dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```
