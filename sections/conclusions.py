import streamlit as st

def show_conclusions():

    st.header("Conclusion")

    st.write("""
    The national results show that Emmanuel Macron received the most votes in the first round of the 2022 French presidential election,
    followed by Marine Le Pen and Jean-Luc Mélenchon.

    However, the geographical analysis shows important differences between departments.

    Emmanuel Macron came first in many departments, while Marine Le Pen received strong support in northern and eastern France.

    Jean-Luc Mélenchon came first in fewer departments but had high vote percentages in most departments of Île-de-France,
    which have the most population.

    This explains why his national vote total was pretty close to Marine Le Pen's, even by coming first in a lot fewer departments.

    Overall, national results don't tell the whole story.
    
    Looking at geographical differences provides a better understanding of voting patterns across France.
    """)