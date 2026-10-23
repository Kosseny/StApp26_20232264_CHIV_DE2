import streamlit as st
from utils.io import load_data
from utils.prep import make_tables
from sections.intro import show_intro
from sections.overview import visualisation1, visualisation2, show_kpis
from sections.deep_dives import visualisation3
from sections.conclusions import show_conclusions

st.set_page_config(page_title="2022 First Round French Presidential Election", layout="wide")

@st.cache_data(show_spinner=False)
def get_data():
    df_raw = load_data()
    tables = make_tables(df_raw)
    return df_raw, tables

st.title("2022 French Presidential Election")

st.caption(
    "Source: 2022 French Presidential Election - First Round - "
    "[data.gouv.fr](https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour)"
)

raw, tables = get_data()

#Sidebar
st.sidebar.header("Student Information")

st.sidebar.write("**Name:** Kosseny CHIV")
st.sidebar.write("**Email:** kosseny.chiv@efrei.net")
st.sidebar.write("**Class:** DE02")
st.sidebar.write("**Academic Year:** 2026-2027")

st.sidebar.divider()

#sidebar filters
st.sidebar.header("Filters")

departments = sorted(raw["Libellé du département"].unique())

selected_department = st.sidebar.selectbox(
    "Select a department:",
    ["All France"] + departments
)

st.sidebar.divider()

# Course information
st.sidebar.write("**Course:** Data Analysis and Visualization")
st.sidebar.write("**Professor:** Mano Mathew")
st.sidebar.image("assets/logo_efrei.png", width=200)

#by department
if selected_department == "All France":
    filtered_raw = raw
else:
    filtered_raw = raw[
        raw["Libellé du département"] == selected_department
    ]
    
#KPI
show_kpis(filtered_raw, tables)

#intro
with st.expander("Introduction"):
    show_intro()

#Data Exploration
with st.expander("Data Exploration and Data Cleaning"):

    #dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(raw.head())

    st.write("Number of rows:", raw.shape[0])
    st.write("Number of columns:", raw.shape[1])

    #data exploration
    st.subheader("Data Exploration")

    st.write("Column names:")
    st.write(tables["columns"])

    st.write("Data types:")
    st.dataframe(tables["data_types"])

    st.write("Missing values:")
    st.dataframe(tables["missing_values"])

    st.write("Duplicate rows:", tables["duplicates"])

    #cleaned candidate data
    st.subheader("Cleaned Candidate Data")
    st.dataframe(tables["candidates"].head())
    st.write("Number of candidate rows:", tables["candidates"].shape[0])

    #consistency check
    st.subheader("Vote Consistency Check")

    st.write("Total candidate votes:", tables["total_votes"])
    st.write("Total expressed votes:", tables["total_expressed"])
    st.write("Votes match:", tables["votes_match"])

#Visualization 1
with st.expander("Visualization 1: National and Departmental Election Results"):
    visualisation1(tables, selected_department)

#Visualization 2
with st.expander("Visualization 2 : Department Election Map"):
    visualisation2(tables)

#Visualization 3
with st.expander("Visualization 3 : Where Were the Candidates Strongest ?"):
    visualisation3(tables)

#Conclusion
with st.expander("Conclusion"):
    show_conclusions()