import os, time
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Directory containing the Excel files
directory = 'NEISS_All_Data/Fact Tables/'

start_time = time.time()
neiss_2022 = pd.read_excel('NEISS_All_Data/Fact Tables/NEISS_2022.XLSX')
end_time = time.time()
table_load_time = end_time - start_time
print(table_load_time)

dim_directory = 'NEISS_All_Data/Dimension Tables/'
dataframes = {}

for filename in os.listdir(dim_directory):
    if filename.endswith('.xlsx'):
        filepath = os.path.join(dim_directory, filename)
        dataframe_name = filename.split('.')[0]  # Use the filename as the dataframe name
        dataframes[dataframe_name] = pd.read_excel(filepath)

for dataframe_name, dataframe in dataframes.items():
    globals()[dataframe_name] = dataframe

# The dim tables names are:
'''
FireDim
BdypartDim
DiagnosisDim
RaceDim
Alc_DrugDim
GenderDim
ProductDim
LocationDim
DispositionDim
HispanicDim
AgeLTwoDim
'''

    

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run_server(debug=True)

'''

# Initialize an empty list to store the DataFrames
dataframes = []
# Iterate over the files in the directory
for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        df = pd.read_excel(filepath)
        dataframes.append(df)

# Check if any valid files were found
if len(dataframes) == 0:
    print("No valid Excel files found in the directory.")
else:
    # Concatenate all the DataFrames into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Print the combined DataFrame
    print(combined_df)
'''