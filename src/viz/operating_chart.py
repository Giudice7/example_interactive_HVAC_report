import plotly.graph_objects as go


def plot_operating_chart(df_operating_mode):
    df_plot = df_operating_mode.select_dtypes(include='number').round(2)
    df_plot = df_plot.drop_duplicates(keep='first')

    trace1 = go.Scatter(
        x=df_plot["OA_TEMP"],
        y=df_plot["OA_DMPR_DM"],
        mode='markers',
        marker=dict(symbol='circle', opacity=0.5),
        name='Outdoor damper command',
        hovertemplate=(
            'Datetime: %{customdata}<br>'
            'Outdoor Air Temperature: %{x}°F<br>'
            'Outdoor Damper Command: %{y}<extra></extra>'
        ),
        customdata=df_operating_mode.index.values
    )
    trace2 = go.Scatter(
        x=df_plot["OA_TEMP"],
        y=df_plot["CHWC_VLV_DM"],
        mode='markers',
        marker=dict(symbol='x', opacity=0.5),
        name='Cooling coil command',
        hovertemplate=(
            'Datetime: %{customdata}<br>'
            'Outdoor Air Temperature: %{x}°F<br>'
            'Cooling Coil Command: %{y}<extra></extra>'
        ),
        customdata=df_operating_mode.index.values
    )
    fig = go.Figure()
    fig.add_trace(trace1)
    fig.add_trace(trace2)
    fig.update_layout(
        title="",
        xaxis_title="Outdoor Air Temperature [°F]",
        yaxis_title="Command [-]",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.5)'
        ),
        margin=dict(t=50, b=40, l=40, r=40),
        template="plotly_white"
    )
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGray')

    return fig
