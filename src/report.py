import os
import pandas as pd
from src.utils import stats
from src.viz.operating_chart import plot_operating_chart
from jinja2 import Environment, FileSystemLoader


def run_report(df: pd.DataFrame, dataset_name: str):
    """
    Generate the report for a specific dataset, saving it into the folder `reports`.
    :param df: the dataset with the AHU data
    :param dataset_name: the name of the dataset
    """

    # Set up the Jinja2 environment for report
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html')

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df_hourly = df.set_index('Datetime').resample('h').mean()

    # Visualize the operating chart
    fig_om = plot_operating_chart(df_hourly)

    # Calculate the top k coldest days
    top_k_days_table = stats.calculate_top_coldest_days(df, k=5).reset_index(names=['Date'])

    context = {
        'title': 'Fault Detection and Diagnosis report',
        'subtitle': f'Report for the {dataset_name} dataset',
        'coldest_days': {
            'title': 'List of the top 5 coldest days in the dataset',
            'description': 'This section provides the list of the top 5 coldest days in the dataset purchased.',
            'plot': top_k_days_table.to_html(classes='table table-striped table-hover', index=False, border=0)
        },
        'operating_chart': {
            'title': 'Operating chart',
            'description': 'This section shows the operating chart. In particular, the x-axis shows the Outdoor Air Temperature,'
                           ' while the y-axis shows both the damper operation and the cooling coil valve operating',
            'plot': fig_om.to_html(full_html=False, include_plotlyjs='cdn'),
        }
    }

    html_content = template.render(context)

    # Save the rendered HTML to a file (optional, for inspection)
    with open(os.path.join('reports', f'{dataset_name}.html'), 'w') as file:
        file.write(html_content)
