import pandas as pd


data = {
    'school_name': [
        'Stuyvesant High School', 'Bronx High School of Science', 'Brooklyn Technical High School',
        'Queens High School for Sciences', 'Staten Island Tech', 'Manhattan Science',
        'Brooklyn Latin School', 'Queens Collegiate', 'Bronx Academy', 'Staten Island Academy',
        'Manhattan Prep', 'Brooklyn Prep', 'Queens Prep', 'Bronx Prep', 'Staten Island Prep',
        'Manhattan West', 'Brooklyn East', 'Queens North', 'Bronx South', 'Staten Island West'
    ],
    'borough': [
        'Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island', 'Manhattan', 'Brooklyn',
        'Queens', 'Bronx', 'Staten Island', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx',
        'Staten Island', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'
    ],
    'average_math': [754, 745, 740, 730, 725, 720, 710, 700, 690, 680, 670, 660, 650, 640, 630, 620, 610, 600, 590, 580],
    'average_reading': [700, 695, 690, 680, 675, 670, 660, 650, 640, 630, 620, 610, 600, 590, 580, 570, 560, 550, 540, 530],
    'average_writing': [715, 710, 705, 695, 690, 685, 675, 665, 655, 645, 635, 625, 615, 605, 595, 585, 575, 565, 555, 545]
}

df = pd.DataFrame(data)
df.to_csv('schools.csv', index=False)
print("schools.csv created successfully!")

schools = pd.read_csv("schools.csv")

schools.head()


best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)

schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

top_10_schools = schools.sort_values("total_SAT", ascending=False)[["school_name", "total_SAT"]].head(10)

boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

largest_std_dev.reset_index(inplace= True)
print(schools)