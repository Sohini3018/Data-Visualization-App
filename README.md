# Data Visualizer App

This Streamlit app allows you to upload CSV, JSON, or XLSX files and visualize the data in an interactive way.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Supported Data Formats](#supported-data-formats)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the Data Visualizer App, you need to have Python and Streamlit installed on your system. You can install Streamlit using pip:

```bash
pip install streamlit
```
Next, clone this repository and navigate to the project directory:
```bash
git clone https://github.com/Sohini3018/Data-Visualization-App
cd Data-Visualization-App
```
## Usage
To launch the app, run the following command in the project directory:
```bash
streamlit run app.py
```
This will start the app, and you can access it in your web browser by opening the provided URL (usually http://localhost:8501).

## Supported Data Formats

The Data Visualizer App supports the following data formats for upload:

- CSV (Comma-separated values)
- JSON (JavaScript Object Notation)
- XLSX (Microsoft Excel)

## Dependencies

The app uses the following dependencies:

- pandas: For data manipulation and analysis.
- streamlit: For building the interactive web app.
- os: For handling file paths and directories.
- tempfile: For creating temporary directories to save uploaded files.

All the dependencies are listed in the `requirements.txt` file.

---

Happy hacking! If you have any questions or need any assistance, please don't hesitate to contact the project maintainers. Thank you for using the Data Visualizer App!
