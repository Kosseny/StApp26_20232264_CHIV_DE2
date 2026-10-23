import streamlit as st
from utils.viz import candidate_department_chart

def visualisation3(tables):

    st.header("Where Were the Candidates Strongest?")

    st.write("""
    The national results and the map show that voting preferences were different across France.

    Let's explore the departments where each candidate received their highest percentage of votes.
    """)

    df = tables["department_votes"]

    #Selection of a candidate
    candidate = st.selectbox(
        "Select a candidate:",
        sorted(df["Nom"].unique())
    )

    #selected candidate
    filtered_df = df[df["Nom"] == candidate]

    #top 10 departments
    top_10 = filtered_df.nlargest(10, "Vote Percentage")

    #Display
    fig = candidate_department_chart(top_10)

    st.plotly_chart(fig, use_container_width=True)
    
    if candidate == "MÉLENCHON":
        st.write("""
        Jean-Luc Mélenchon received some of his highest vote percentages in Île-de-France region.

        Indeed, 7 of his top 10 departments are located in this region.

        This helps explain why he received a large number of votes nationally even though he came first in a lot few departments.

        It shows that the number of departments where a candidate comes first does not necessarily reflect their total number of votes.
        """)
        
    elif candidate == "MACRON":
        st.write("""
        Emmanuel Macron received his highest vote percentages in several departments in western France and the Paris region.

        Unlike Jean-Luc Mélenchon, whose strongest results are concentrated mainly in Île-de-France, Macron's top departments are spread across many regions.

        This shows that candidates can have different geographical voting patterns.
        """)
        
    elif candidate == "LE PEN":
        st.write("""
        Marine Le Pen received her highest vote percentages mainly in northern and eastern France.

        Her strongest results include Aisne, Pas-de-Calais and Haute-Marne.

        Compared to Macron and Mélenchon, her top departments are concentrated in different geographical areas.

        This shows that the three leading candidates have different geographical voting patterns.
        """)