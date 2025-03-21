from dash import html
import dash_mantine_components as dmc
from Stocks_layout import create_layout_stocks
from Comparison_layout import create_layout_comparison
from Crypto_layout import create_layout_crypto

def create_layout():
    layout1 = html.Div(children=[
        html.H1(children='Capital Market Analytics', style={'textAlign': 'center'}),


    dmc.Tabs( 
    [
        dmc.TabsList(
            
            [
                dmc.Tab("Comparison", value="comparison"),
                dmc.Tab("Stocks", value="stocks"),
                dmc.Tab("Crypto", value="crypto"),
            ],
            position="center",
            grow=True,
        ),
        dmc.TabsPanel([create_layout_comparison()], value="comparison"),
        dmc.TabsPanel([create_layout_stocks()] , value='stocks'),
        dmc.TabsPanel([create_layout_crypto()], value='crypto'),
    ],
    color="blue",
    orientation="horizontal",
    value= 'comparison'
),

    ])
        

    return layout1


# [
#                 dmc.Grid(
#                 children=[
#                 dmc.Col(html.Div([
#                         html.P("Stocks",  style={'textAlign': 'center', 'fontSize': 24, 'margin-top': -10}),


#                         dmc.Select(
#                                 # data=symbols_list, 
#                                 data=[{'value': key, 'label': value} for key, value in symbols_dict.items()],
#                                         value=symbols_list[0],
#                                         id='left-dropdown',
#                                         searchable=True,
#                                         nothingFound="No options found",
#                                         clearable=True,
#                                         style={'backgroundColor': 'lightgrey', 'position': 'absolute', 'z-index': '3', 'height': 'auto', 'width': '49%'}
#                                 # data=[{'value': key, 'label': value} for key, value in symbols_dict.items()],
#                                 # id =  'left-dropdown',
#                                 # value=list(symbols_dict.keys())[0],
                        
                                
#                         ),
#                         # dcc.Graph(
#                         #         id= 'current-left',
#                         #         style={'width': '15vh', 'height': '10vh'}),


#                 ]), span="auto"),



#                 dmc.Col(html.Div([
#                         html.P("Cryptocurrencies", style={'textAlign': 'center', 'fontSize': 24, 'margin-top': -10,}),
#                         dmc.Select(
#                                 # data=crypto_symbols,
#                                  data=[{'value': key, 'label': value} for key, value in crypto_dict.items()],
#                                         id='right-dropdown', 
#                                         value=crypto_symbols[0],
#                                         searchable=True,
#                                         nothingFound="No options found",
#                                         clearable=True,
#                                         style={'backgroundColor': 'lightgrey', 'position': 'absolute', 'z-index': '3', 'width': '49%'}    # Specify the desired width}
                                        
                        
#                         ),

#                 ]), span='auto'),
#                 ],
#                 gutter="sm",
#                 # style={'margin-bottom': -10}
#         ),
#                 dmc.SimpleGrid(
#                         cols=2,
#                         spacing='lg',
#                         children=[
#                                 html.Div([
#                                 dcc.Graph(
#                                         id='current-left',
#                                         style={'width': '15vh', 'height': '9vh', 'position': 'absolute', 'z-index': '2', 'margin-left': 65, 'margin-top':40}
#                                 ),
                                
#                                 dmc.RadioGroup(
#                                         [dmc.Radio(l, value=k) for k, l in data],
#                                         id="left-time",
#                                         value="5d",
#                                         # label="Select your favorite framework/library",
#                                         size="sm",
#                                         mt=10,
#                                         style={'margin-left':200, 'margin-top': 40, 'position': 'absolute', 'z-index': '2'}
#                                 ),

#                                 ]),
                                
#                                 html.Div([
#                                 dcc.Graph(
#                                         id='current-right',
#                                         style={'width': '15vh', 'height': '9vh', 'position': 'absolute', 'z-index': '2', 'margin-left': 65, 'margin-top':40}
#                                 ),

#                                   dmc.RadioGroup(
#                                         [dmc.Radio(l, value=k) for k, l in data],
#                                         id="right-time",
#                                         value="5d",
#                                         # label="Select your favorite framework/library",
#                                         size="sm",
#                                         mt=10,
#                                         style={'margin-left':200, 'margin-top': 40, 'position': 'absolute', 'z-index': '2'}
#                                 ),
#                                 ]),
#         ]
#         ),



#         dmc.SimpleGrid(
#         cols=2,
#         spacing='xs',
#         children=[
#                 html.Div([
#                         dcc.Graph(
#                                 id='scatter-left'
#                         ),

#                 ],style={'width': '100%', 'height': '500px','margin-bottom':-100, 'z-index': '1', 'margin-top': 25}),

#                 html.Div([         
#                         dcc.Graph(
#                                 id='scatter-right'
#                         ),
  
#                 ],style={'width': '100%', 'height': '500px','margin-bottom':-100, 'z-index': '1', 'margin-top': 25}),
#         ],
#         # style={'width': '50%', 'height': '400px'}
#           # style={'display': 'flex', 'justifyContent': 'center'}),
#           style={'margin': '0 auto'}
#         #   style={ 'margin-bottom': -80,'margin': '0 auto'}

#         ),
#         # html.Div(style={'margin-bottom': '-70x'}),
   

#         dmc.Grid(
#                 children=[
#                 dmc.Col(html.Div([
#                         dmc.Card(
#                         children=[
#                                 dmc.CardSection(
#                                 children=[
                               
#                                         dmc.SimpleGrid(
#                                         cols = 1,
#                                         spacing="sm",

#                                         children=[
                                                
                                            
#                                                 dcc.Graph(
#                                                 id= 'table-left',
#                                                 style={'width': '70vh', 'height': '30vh', 'margin': '0 auto', 'z-index': '2'}
#                                                 ),

                        
#                                         ]
#                                         )
#                                 ]
#                                 )


#                         ]
                        

#                         ),

#                 ]), span="auto"),


#                 dmc.Col(html.Div([
#                         dmc.Card(
#                         children=[
#                                 dmc.CardSection(
#                                 children=[
  
#                                         dmc.SimpleGrid(
#                                         cols = 1,
#                                         spacing="sm",

#                                         children=[
#                                                 dcc.Graph(
#                                                 id= 'table-right',
#                                                 style={'width': '70vh', 'height': '30vh', 'margin': '0 auto 0 auto', 'z-index': '2'}

#                                                 ),


#                                         ]
#                                         )
#                                 ]
#                                 )


#                         ]
                        

#                         ),
                        

#                 ]), span='auto'),
#                 ],
#         # gutter="sm",
#         ),

                

#             ]