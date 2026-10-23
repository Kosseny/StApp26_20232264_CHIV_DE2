# French Presidential Election - Data Storytelling Dashboard

Individual Student Project - Data Visualization

## Description

This project is an interactive Streamlit dashboard analyzing the first round of the 2022 French presidential election.

The goal is to compare national and departmental election results and explore geographical differences in voting patterns across France.

## Live Dashboard

The dashboard is available online:

https://stapp26-20232264-chiv-de2.streamlit.app/

## Dataset

The dataset contains the results of the first round of the 2022 French presidential election.

It includes information about registered voters, votes cast, abstentions, and votes received by the 12 candidates.

The original dataset contains 69,682 rows and 105 columns.

## Data Limitations

The analysis focuses on the first round of the 2022 French presidential election.

The national results include all voting territories, while the map and the third visualization focus on the 96 departments of metropolitan France.

The dashboard describes geographical voting patterns but does not explain the reasons behind voters' choices.

## Visualizations

The dashboard includes three interactive visualizations:

1. **National and Departmental Election Results:** A bar chart showing the number of votes received by each candidate. Users can select a department using the sidebar filter.

2. **Department Election Map:** An interactive map showing the leading candidate in each of the 96 departments of metropolitan France.

3. **Candidates' Strongest Departments:** A bar chart showing the top 10 metropolitan departments where the selected candidate received the highest percentage of votes.

The dashboard also includes KPIs, data exploration, and data quality checks.

## Technologies

- Python
- Streamlit
- Pandas
- Plotly
- NumPy
- OpenPyXL

## Installation

Tested with Python 3.9.

1. Open a terminal in the project folder.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
python -m streamlit run app.py
```

4. Open the local URL displayed in the terminal to access the dashboard.

## Project Structure

```text
StApp26_20232264_CHIV_DE2/
├── app.py
├── README.md
├── requirements.txt
├── assets/
│   └── logo_efrei.png
├── data/
│   ├── resultats-par-niveau-burvot-t1-france-entiere.xlsx
│   └── departements.geojson
├── sections/
│   ├── intro.py
│   ├── overview.py
│   ├── deep_dives.py
│   └── conclusions.py
└── utils/
    ├── io.py
    ├── prep.py
    └── viz.py
```

## Data Source

The election results dataset was obtained from data.gouv.fr:

https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour

The geographical data used for the map is stored in `data/departements.geojson`.

Geographical data (GeoJSON):

https://github.com/gregoiredavid/france-geojson/blob/master/departements.geojson