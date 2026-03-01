import plotly.express as px
import plotly.io as pio
from plotly.offline import plot
import plotly.graph_objects as go
from django.shortcuts import render



def plotly_charts(request):
 
    plot_html = []

    # Create Plotly plots
    df_plot = px.data.iris()
    fig = px.scatter(
        df_plot, x="sepal_width", y="sepal_length", color='petal_length',
        template='plotly_dark', title='Circle Plot'
    )
    plot_html.append(plot(fig, output_type='div', include_plotlyjs=False))

    df_plot2 = px.data.gapminder()
    fig = px.scatter(
        df_plot2.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop",
        color="continent", hover_name="country", log_x=True, size_max=60, 
        title='Bubble Plot', template='plotly_dark'
    )
    plot_html.append(plot(fig, output_type='div', include_plotlyjs=False))

    table_html = []
    values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'], #1st col
    ["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
    "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
    "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
    "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
    "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]


    fig = go.Figure(data=[go.Table(
    columnorder = [1,2],
    columnwidth = [80,400],
    header = dict(
        values = [['<b>EXPENSES</b><br>as of July 2017'],
                    ['<b>DESCRIPTION</b>']],
        line_color='darkslategray',
        fill_color='royalblue',
        align=['left','center'],
        font=dict(color='white', size=12),
        height=40
    ),
    cells=dict(
        values=values,
        line_color='darkslategray',
        fill=dict(color=['paleturquoise', 'white']),
        align=['left', 'center'],
        font = dict(color = 'darkblue', size = 11),
        height=30)
        )
    ], layout=go.Layout(title='Quarterly Expenses', template='plotly_dark'))
    table_html.append(pio.to_html(fig, full_html=False, include_plotlyjs=False))

    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'],
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center'],
        font=dict(color='white', size=12)
    ),
    cells=dict(
        values=[
        ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
        [1200000, 20000, 80000, 2000, 12120000],
        [1300000, 20000, 70000, 2000, 130902000],
        [1300000, 20000, 120000, 2000, 131222000],
        [1400000, 20000, 90000, 2000, 14102000]],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
        align = ['left', 'center'],
        font = dict(color = 'darkblue', size = 11),
        height = 30,
        ))
    ], layout=go.Layout(title='Quarterly Expenses', template='plotly_dark'))

    table_html.append(pio.to_html(fig, full_html=False, include_plotlyjs=False))

    return render(request, 'dashboard/plotly_charts.html', {
        'title': 'Plotly',
        'page_header': 'Plotly Charts & Tables',    
        'plot_html': plot_html,
        'table_html': table_html
    })
