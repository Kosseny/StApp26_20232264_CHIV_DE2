import pandas as pd

def make_tables(df):

    #dataset informations
    columns = df.columns.tolist()
    data_types = df.dtypes.astype(str)
    missing_values = df.isnull().sum()
    duplicates = df.duplicated().sum()
    df_candidates = prepare_candidates(df)
    
    #National results per candidate
    national_results = df_candidates.groupby(
        ["Nom", "Prénom"], as_index=False
    )["Voix"].sum()

    national_results = national_results.sort_values(
        by="Voix", ascending=False
    )
    
    national_results = national_results.reset_index(drop=True)
    
    #results for the map
    map_results = df_candidates.groupby(
        ["Code du département", "Libellé du département", "Nom"],
        as_index=False
    )["Voix"].sum()
    
    #the winning candidate in each department
    map_winners = map_results.loc[
        map_results.groupby("Code du département")["Voix"].idxmax()
    ].copy()
    
    # metropolitan departments only
    map_winners["Code du département"] = (
        map_winners["Code du département"].astype(str).str.zfill(2)
    )

    map_winners = map_winners[
        map_winners["Code du département"].str.match(r"^(0[1-9]|[1-8][0-9]|9[0-5]|2A|2B)$")
    ]
    
    #candidate results by metropolitan department
    department_votes = map_results.copy()

    #total expressed votes by department
    department_expressed = df.groupby(
        "Code du département", as_index=False
    )["Exprimés"].sum()

    #both tables
    department_votes = department_votes.merge(
        department_expressed,
        on="Code du département"
    )

    #vote percentage
    department_votes["Vote Percentage"] = (
        department_votes["Voix"] / department_votes["Exprimés"] * 100
    )

    # metropolitan departments only
    metro_codes = set(map_winners["Code du département"])

    department_votes = department_votes[
        department_votes["Code du département"].isin(metro_codes)
    ]
    
    #Number of metropolitan departments won by candidate
    metro_departments_won = map_winners.groupby(
        "Nom", as_index=False
    ).size()

    metro_departments_won = metro_departments_won.rename(
        columns={"size": "Departments Won"}
    )
    
    #consistency check
    total_votes = df_candidates["Voix"].sum()
    total_expressed = df["Exprimés"].sum()
    votes_match = total_votes == total_expressed

    tables = {
        "columns": columns,
        "data_types": data_types,
        "missing_values": missing_values,
        "duplicates": duplicates,
        "candidates": df_candidates,
        "total_votes": total_votes,
        "total_expressed": total_expressed,
        "votes_match": votes_match,
        "national_results": national_results,
        "map_winners": map_winners,
        "metro_departments_won": metro_departments_won,
        "department_votes": department_votes
    }

    return tables

def prepare_candidates(df):

    #All election information
    general = df.iloc[:, :21]

    #candidate informations
    candidates = []

    for i in range(12):
        start = 21 + i * 7
        candidate = df.iloc[:, start:start+7].copy()
        candidate.columns = ["N°Panneau", "Sexe", "Nom", "Prénom", "Voix", "% Voix/Ins", "% Voix/Exp"]

        # Add general information
        candidate = pd.concat([general, candidate], axis=1)

        candidates.append(candidate)

    #All candidates
    df_candidates = pd.concat(candidates, ignore_index=True)

    return df_candidates