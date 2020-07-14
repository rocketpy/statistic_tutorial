#  Altair - declarative statistical visualization library for Python 
#  Examples of Charts , Histograms , Maps , Interactive Charts , Case Studies : https://altair-viz.github.io/gallery/index.html


# code example , area chart with Gradient , taked from : https://altair-viz.github.io/getting_started/overview.html

import altair as alt
from vega_datasets import data


source = data.stocks()

alt.Chart(source).transform_filter(
    'datum.symbol==="GOOG"'
).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X('date:T'),
    alt.Y('price:Q')
)
