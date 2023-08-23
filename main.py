import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

num_inputs = 5  # Number of input text boxes

app.layout = html.Div([
    html.Div([
        dcc.Input(id=f'input{i}', type='text', placeholder=f'Input {i}')
        for i in range(1, num_inputs + 1)
    ], style={'display': 'flex'}),
    
    html.Div(id='error-msg', style={'color': 'red'}),
    
    html.Div(id='output')
])

@app.callback(
    [Output(f'input{i}', 'style') for i in range(1, num_inputs + 1)] +
    [Output('error-msg', 'children')],
    [Input(f'input{i}', 'value') for i in range(1, num_inputs + 1)]
)
def update_output(*inputs):
    styles = [{'border': '1px solid black'} for _ in range(num_inputs)]
    error_msg = ""

    for i, value in enumerate(inputs):
        if value:
            try:
                num = int(value)
                if 1 <= num <= 49:
                    styles[i]['border'] = '1px solid black'
                    #We check that there are not two times same number
                else:
                    styles[i]['border'] = '1px solid red'
                    error_msg = "Invalid input. Enter a number between 1 and 49."

            except ValueError:
                styles[i]['border'] = '1px solid red'
                error_msg = "Invalid input. Enter a number between 1 and 49."

    return styles + [error_msg]

if __name__ == '__main__':
    app.run_server(debug=True)
