######### Import your libraries #######
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly as py
import plotly.graph_objs as go


###### Define your variables #####
tabtitle = 'Titanic2'
color1='#92A5E8'
color2='#8E44AD'
color3='#FFC300'
sourceurl = 'https://www.kaggle.com/c/titanic'
githublink = 'https://github.com/plotly-dash-apps/304-titanic-dropdown'


###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/00%20resources/titanic.csv")
df['Female']=df['Sex'].map({'male':0, 'female':1})
df['Cabin Class'] = df['Pclass'].map({1:'first', 2: 'second', 3:'third'})
variables_list=['Survived', 'Female', 'Fare', 'Age']

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a continuous variable for summary statistics:'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in variables_list],
        value=variables_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
])


######### Interactive callbacks go here #########
@app.callback(Output('display-value', 'figure'),
              [Input('dropdown', 'value')])
def display_value(continuous_var):
    grouped_mean=df.groupby(['Cabin Class', 'Embarked'])[continuous_var].mean()
    results=pd.DataFrame(grouped_mean)

#     classname = ['Cherbourg', 'Queenstown','Southampton']
    
#     volume = [results.loc['Cherbourg'][continuous_var],
#               results.loc['Queenstown'][continuous_var],
#               results.loc['Southampton'][continuous_var]]

#     mydata = go.Pie(labels=classname,values=volume)
#     data = [mydata]
#     # # Create a grouped bar chart
#     # mydata1 = go.Bar(
#     #     x=results.loc['first'].index,
#     #     y=results.loc['first'][continuous_var],
#     #     name='First Class',
#     #     marker=dict(color=color1)
#     # )
#     # mydata2 = go.Bar(
#     #     x=results.loc['second'].index,
#     #     y=results.loc['second'][continuous_var],
#     #     name='Second Class',
#     #     marker=dict(color=color2)
#     # )
#     # mydata3 = go.Bar(
#     #     x=results.loc['third'].index,
#     #     y=results.loc['third'][continuous_var],
#     #     name='Third Class',
#     #     marker=dict(color=color3)
#     # )

#     mylayout = go.Layout(
#         title='Grouped pie chart'
#     )
#     fig = go.Figure(data=data, layout=mylayout)

 mylayout = go.Layout(
        title='Grouped pie chart 2',
    )
    classname1 = ['Cherbourg', 'Queenstown','Southampton']
    volume = [results.loc['Cherbourg'][continuous_var],results.loc['Queenstown'][continuous_var],results.loc['Southampton'][continuous_var]]

    data = [go.Pie(labels=classname1, 
               values=volume
              )]
    fig = go.Figure(data,layout=mylayout)
    return fig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
