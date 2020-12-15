import streamlit as st
import pandas as pd
import altair as alt


# Get data from github (local is boring)
@st.cache
def get_iris_data():
    url = 'https://raw.githubusercontent.com/maxistaebler/streamlit/master/input/iris.csv'
    df = pd.read_csv(url)
    return df

try:
    df = get_iris_data()
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
    return



countries = st.multiselect(
    "Choose countries", list(df.index), ["China", "United States of America"]
)
if not countries:
    st.error("Please select at least one country.")
    return

data = df.loc[countries]
data /= 1000000.0
st.write("### Gross Agricultural Production ($B)", data.sort_index())

data = data.T.reset_index()
data = pd.melt(data, id_vars=["index"]).rename(
    columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
)
chart = (
    alt.Chart(data)
    .mark_area(opacity=0.3)
    .encode(
        x="year:T",
        y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
        color="Region:N",
    )
)
st.altair_chart(chart, use_container_width=True)