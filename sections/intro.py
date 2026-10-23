import streamlit as st

def show_intro():

    st.header("Introduction")

    st.write("""
    This dashboard presents the results of the first round of the 2022 French presidential election.
    
    The goal is to compare candidates and explore geographical differences in voting patterns across France.
    """)

    st.subheader("Dataset Description")

    st.write("""
    The dataset contains results from polling stations across France.
    
    It has registered voters, abstentions, expressed votes and the results of the 12 candidates.
    """)

    st.subheader("Data Preparation")

    st.write("""
    The original dataset has 69 682 rows and 105 columns.
    
    We reorganized the candidate data into a format with one row per candidate and polling station, creating a new dataset with 836,184 rows.
    
    We also checked for missing values and duplicate rows and compared the total candidate votes with the total expressed votes to verify data consistency.
    """)
    
    st.subheader("Problematique")
    
    st.write("""
    How do voting patterns differ across French departments compared to the national results of the 2022 presidential election ?
    """)
    
    st.subheader("Storytelling Questions")
        
    st.write("""
    Who won the first round nationally or in the selected department?
    
    Did the same candidate win in every department ?
    
    Where did the leading candidates perform best ?
    """)
    
    st.subheader("Data Limitations")

    st.write("""
    The dashboard only analyzes the first round of the 2022 French presidential election.

    The national results include all voting territories while the map and the visualization 3 focus on the 96 departments of metropolitan France.

    The department filter applies to the KPIs and the first visualization.
    
    The other visualizations remain focused on metropolitan France.

    The results show geographical voting differences but don't explain why people voted for a particular candidate.
    """)
        
        
    