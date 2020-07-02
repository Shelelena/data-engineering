# %%
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "notebook"

# %%
'''
## Report on unprofitable categories ##
### Dec 2019 ###
'''

# %%
df: pd.DataFrame = pd.read_excel(
    Path().cwd().parent
    / 'Lab'
    / 'Sample - Superstore.xls',
    parse_dates=True)

df = (
    df
    .rename(
        columns=lambda x:
        x.lower()
        .replace(' ', '_')
        .replace('-', '_')
    )
    .set_index('row_id')
)

# %%
last_month = (
    df
    .query(
        'order_date.dt.year == order_date.max().year '
        'and order_date.dt.month == order_date.max().month')
)

# %%
category_summary = (
    last_month
    .groupby(['category', 'sub_category'], as_index=False)
    .agg({
        'sales': 'sum',
        'quantity': 'sum',
        'discount': 'mean',
        'profit': 'sum',
    })
)

(
    category_summary
    .set_index(['category', 'sub_category'])
    .style
    .set_caption('Category metrics in Dec 2019')
    .format(
        '{:.2f}',
        subset=['sales', 'profit', 'discount'])
    .applymap(
        func=lambda x: 'background-color: yellow' if x < 0 else '',
        subset='profit'
    )
)

# %%
layout = dict(
    title_font_size=20,
    font_size=10,
    xaxis_tickfont_size=15,
    xaxis_tickangle=270,
    yaxis_tickfont_size=15,
    autosize=False,
    width=800,
    height=600,
)

# %%
fig = go.Figure(layout=layout)

fig.add_trace(
    go.Bar(
        x=category_summary.sub_category,
        y=category_summary.profit,
        textposition='outside',
        texttemplate='%{y:.0f}',
        marker_color=category_summary.profit.map(
            lambda x: 'blue' if x >= 0 else 'red'
        ),
        hovertemplate='Category: %{x}<br>Profit: %{y:.1f}',
    )
)
fig.update_layout(
    title_text='Profit by category in Dec 2019',
)

# %%
fig = go.Figure(layout=layout)

fig.add_trace(
    go.Bar(
        x=category_summary.sub_category,
        y=category_summary.discount,
        textposition='outside',
        texttemplate='%{y:.02f}',
        marker_color=category_summary.profit.map(
            lambda x: 'blue' if x >= 0 else 'red'
        ),
        hovertemplate='Category: %{x}<br>Average Discount: %{y:.2f}',
    )
)
fig.update_layout(
    title_text='Average discount by category in Dec 2019',
)

# %%
fig = go.Figure(layout=layout)

fig.add_trace(
    go.Scatter(
        x=category_summary.discount,
        y=category_summary.profit,
        text=category_summary.sub_category,
        mode='markers',
        marker=dict(
            color=category_summary.profit.map(
                lambda x: 'blue' if x >= 0 else 'red'
            ),
            size=15,
        ),
        hovertemplate=(
            'Category: %{text}'
            '<br>Average Discount: %{y:.2f}'
            '<br>Profit: %{x:.1f}'
        ),
    )
)
fig.update_layout(
    title_text='Discount-Profit dependency in Dec 2019',
    height=800,
)

# %%
