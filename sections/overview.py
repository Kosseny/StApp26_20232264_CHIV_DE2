import streamlit as st
from utils.viz import bar_chart
from utils.io import load_geojson
from utils.viz import election_map


def visualisation1(tables, selected_department):

    if selected_department == "All France":
        st.subheader("Who won the first round nationally?")
    else:
        st.subheader(f"Who won the first round in {selected_department}?")

    if selected_department == "All France":
        st.write("""
        Let's start by looking at the national results of the first round of the 2022 French presidential election.
        """)
    else:
        st.write(f"""
        Let's explore the results of the first round of the 2022 French presidential election in {selected_department}.
        """)

    #filter candidate results
    if selected_department == "All France":
        results = tables["national_results"]
        
    else:
        results = tables["candidates"]

        results = results[results["Libellé du département"] == selected_department]

        results = results.groupby(["Nom", "Prénom"], as_index=False)["Voix"].sum()

        results = results.sort_values(by="Voix", ascending=False)

    #Create the chart
    fig = bar_chart(results)

    if selected_department != "All France":
        fig.update_layout(
            title=f"2022 Presidential Election - {selected_department}"
        )

    st.plotly_chart(fig, use_container_width=True)

    if selected_department == "All France":
        st.write("""
        Emmanuel Macron received the most votes nationally followed by Marine Le Pen and Jean-Luc Mélenchon.

        However, these national results don't show how voting preferences differ across French departments.
        """)
    else:
        st.write(f"""
        In {selected_department}, {results.iloc[0]["Nom"]} received the highest number of votes.

        This shows that the leading candidate can change with the selected department.
        """)


def visualisation2(tables):

    st.subheader("Did the Same Candidate Win Everywhere?")

    st.write("""
    The national results show that Emmanuel Macron received the most votes.
    
    However, voting preferences can change across departments.

    The map below shows the candidate who received the most votes in each department of metropolitan France.
    """)

    geojson = load_geojson()

    fig = election_map(tables["map_winners"], geojson)

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    The map shows that voting preferences were different across metropolitan France.
    """)

    for _, row in tables["metro_departments_won"].iterrows():
        st.write(f'{row["Nom"]}: {row["Departments Won"]} / 96')

    st.write("""
    Emmanuel Macron came first in more departments, especially in western France.

    Marine Le Pen came first in several departments in northern, eastern and southeastern France.

    Jean-Luc Mélenchon came first in a lot less departments than Emmanuel Macron and Marine Le Pen.

    However, the gap in the total number of votes is much smaller.

    This can be explained by his strong results in highly populated departments especially in Île-de-France region.

    This shows that winning more departments doesn't necessarily mean receiving proportionally more votes.
    """)


def show_kpis(raw, tables):

    registered = raw["Inscrits"].sum()
    voters = raw["Votants"].sum()
    turnout = voters / registered * 100

    candidate_votes = tables["candidates"]

    candidate_votes = candidate_votes[
        candidate_votes["Libellé du département"].isin(
            raw["Libellé du département"].unique()
        )
    ]

    leading_candidate = candidate_votes.groupby("Nom")["Voix"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Registered Voters", f"{registered:,}")

    with col2:
        st.metric("Total Votes Cast", f"{voters:,}")

    with col3:
        st.metric("Turnout Rate", f"{turnout:.2f}%")

    with col4:
        st.metric("Leading Candidate", leading_candidate)