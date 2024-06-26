# utils.py

from io import BytesIO 
import base64
import matplotlib.pyplot as plt
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')

    fig = plt.figure(figsize=(6, 3))

    if chart_type == 'bar-chart':
        plt.bar(data['name'], data['cooking_time'])

    elif chart_type == 'pie-chart':
        labels = kwargs.get('labels')
        def absolute_value(val):
            a  = int(np.round(val/100.*data['cooking_time'].sum(), 0))
            return f'{a} min'
        plt.pie(data['cooking_time'], labels=labels, autopct=absolute_value)

    elif chart_type == 'line-chart':
        plt.plot(data['name'], data['cooking_time'])
    else:
        print('unknown chart type')

    # layout settings
    plt.tight_layout()

    chart = get_graph()
    return chart

def rename_columns(df):
    column_mapping = {
        'name': 'Name',
        'cooking_time': 'Cooking Time',
        'ingredients': 'Ingredients',
        'difficulty': 'Difficulty'
    }
    return df.rename(columns=column_mapping)