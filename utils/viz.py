import plotly.express as px

def bar_chart(df):

    fig = px.bar(
        df,
        x="Nom",
        y="Voix",
        title="2022 Presidential Election - National Results"
    )

    return fig

def election_map(df, geojson):

    fig = px.choropleth(
        df,
        geojson=geojson,
        locations="Code du département",
        featureidkey="properties.code",
        color="Nom",
        hover_name="Libellé du département",
        hover_data={"Voix": True, "Code du département": False},
        title="Winning Candidate by Department - Metropolitan France"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0)
    )

    return fig

def candidate_department_chart(df):
    fig = px.bar(
        df,
        x="Vote Percentage",
        y="Libellé du département",
        orientation="h",
        title="Top 10 Departments by Vote Percentage",
        labels={
            "Vote Percentage": "Vote Percentage (%)",
            "Libellé du département": "Department"
        }
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    return fig