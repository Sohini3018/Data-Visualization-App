import pandas as pd
import json
import os
from streamlit.connections import ExperimentalBaseConnection


class CustomConnection(ExperimentalBaseConnection):
    def _connect(self, filepath, data_format='csv'):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file '{filepath}' does not exist.")

        if data_format == 'csv':
            return pd.read_csv(filepath)
        elif data_format == 'json':
            with open(filepath, 'r') as json_file:
                data = json.load(json_file)

                # Check if the data is a list of scalar values
                if all(isinstance(item, (int, float, str)) for item in data):
                    # If it is a list of scalar values, convert it into a Series
                    return pd.Series(data)
                else:
                    # If it is a list of dictionaries, convert it into a DataFrame
                    return pd.DataFrame.from_records(data)
        elif data_format == 'excel':
            return pd.read_excel(filepath)
        elif data_format == 'mysql':
            # Handle database connections (if needed)
            pass
        else:
            raise ValueError("Unsupported data format.")
