import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd


########### Define your variables ######
myheading = "Best Craft Beers in DC"
mysubheading = "August 2019"
tabtitle = 'Top Breweries'
filename = 'dc-breweries.csv'
mytitle = 'Brewery Comparison'
label1 = 'Brewery Ratings (AVG)'
label2 = 'Alcohol by Volume (ABV)'
color1='#92A5E8'
color2='#FFC300'
sourceurl = 'https://www.beeradvocate.com/beer/top-rated/us/dc/'
githublink = 'https://github.com/ktemsupa/dash-table-example'


########### Set up the data
df = pd.read_csv(filename)
brewery_name = df['Brewery']
abv = df['Alcohol By Volume (ABV)']
ratings = df['Ratings (Averag)']

########### Set up the chart
brewery_ratings = go.Bar(
    x=brewery_name,
    y=ratings,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=brewery_name,
    y=abv,
    name=label2,
    marker={'color':color2}
)

beer_data = [brewery_ratings, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.Br(),
    dcc.Graph(
        id = 'brewery_compare',
        figure = beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Plotly Dash", href='https://plot.ly/python/pie-charts/')
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
