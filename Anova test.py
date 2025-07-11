import pandas as pd
from scipy import stats

# Data for each sheet
maize_height_data = {
    "Treatment": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    "Replica": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Week1": [55.6, 54.4, 57.6, 55.6, 56.2, 55.2, 57.4, 57.5, 59.5, 60.8, 43, 43.6, 44.5, 44.7, 44.4],
    "Week2": [57.7, 55.6, 59.1, 57.2, 57.3, 57.8, 60.5, 60.7, 61.3, 60.5, 46.7, 46.8, 47.7, 48.1, 47.6],
    "Week3": [60.2, 60.2, 63.1, 61.2, 60.5, 64.6, 65.4, 65.6, 66.8, 65.4, 51.2, 52.1, 52.6, 53.6, 53.1],
    "Week4": [64.2, 64.7, 65.9, 66.6, 65.5, 66.8, 67.7, 67.4, 69.7, 67.5, 57.6, 57.1, 57.5, 57.8, 58.1],
    "Week5": [68.9, 67.8, 68.1, 69.1, 69.9, 73.2, 70.2, 70.9, 74.5, 73.4, 60.1, 60.4, 60.3, 60.5, 60.3],
    "Week6": [73.2, 72.1, 73.1, 73, 72.3, 75, 74.5, 74.2, 75.1, 73.3, 64.2, 65.3, 66.2, 65.2, 66.2],
    "Week7": [77.5, 76.5, 77.3, 77.6, 77.9, 78.3, 77.2, 77.9, 79.1, 78.1, 67.2, 68.2, 68.4, 68.7, 68.5],
    "Week8": [83.4, 84.2, 84.6, 86.7, 84.9, 85.6, 85.4, 86.7, 85.7, 87.9, 73.2, 74.2, 74.3, 73.3, 73.2],
    "Week9": [86.7, 87.6, 86.5, 86.3, 85.1, 88.1, 88.5, 88.7, 87.9, 88.9, 77.7, 76.4, 77.6, 77.5, 77.9],
    "Week10": [89.1, 89.5, 88.7, 88.8, 89.3, 94.3, 94.7, 93.5, 93.7, 94.6, 83.5, 84.2, 83.2, 84.4, 84.7],
    "Week11": [93.4, 95.7, 93.4, 94.5, 94.6, 96.2, 97.2, 95.6, 96.7, 95.2, 86.6, 86.7, 87.1, 87.3, 87.6],
    "Week12": [96.7, 97.5, 96.8, 97.6, 97.7, 102.1, 104.3, 103.3, 102.1, 103.4, 89.1, 89.5, 88.9, 89.3, 88.5]
}

number_of_leaves_data = {
    "Treatment": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    "Replica": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Week1": [4, 4, 3, 5, 5, 4, 5, 5, 5, 5, 3, 4, 4, 5, 4],
    "Week2": [4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 5, 4, 4, 5, 4],
    "Week3": [5, 6, 6, 5, 6, 6, 7, 7, 7, 7, 5, 5, 5, 6, 5],
    "Week4": [6, 5, 5, 6, 6, 7, 8, 9, 8, 8, 6, 6, 7, 6, 7],
    "Week5": [6, 7, 7, 7, 6, 8, 8, 9, 9, 8, 6, 7, 7, 7, 7],
    "Week6": [7, 8, 7, 8, 8, 9, 9, 10, 9, 10, 7, 8, 7, 8, 7],
    "Week7": [8, 8, 9, 9, 9, 11, 11, 12, 11, 11, 8, 8, 7, 8, 7],
    "Week8": [10, 9, 11, 11, 12, 11, 12, 12, 12, 13, 9, 9, 9, 8, 9],
    "Week9": [10, 13, 12, 12, 11, 12, 13, 13, 13, 13, 10, 9, 9, 9, 9],
    "Week10": [10, 13, 13, 11, 11, 13, 13, 12, 13, 14, 10, 9, 9, 10, 10],
    "Week11": [11, 11, 13, 12, 13, 14, 15, 14, 15, 15, 11, 10, 10, 11, 11],
    "Week12": [13, 14, 13, 13, 14, 14, 15, 15, 16, 16, 11, 12, 12, 11, 12]
}

stem_diameter_data = {
    "Treatment": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    "Replica": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Week1": [17.1, 17.9, 18.2, 18.1, 17.8, 19.73, 19.79, 19.9, 20.29, 20.32, 14.54, 14.75, 14.86, 14.92, 14.88],
    "Week2": [17.8, 18.2, 18.6, 18.7, 18.3, 20.21, 20.17, 20.23, 20.35, 20.31, 15.2, 15.29, 15.45, 15.51, 15.6],
    "Week3": [18.4, 18.8, 19.2, 19.1, 18.9, 20.36, 20.31, 20.41, 20.43, 20.37, 15.53, 15.71, 15.78, 15.84, 15.9],
    "Week4": [18.9, 19.3, 19.6, 19.4, 19.2, 20.66, 20.64, 20.61, 20.64, 20.56, 15.85, 15.96, 16.01, 16.18, 16.3],
    "Week5": [19.3, 19.6, 19.9, 19.8, 19.5, 21.13, 21.15, 21.2, 21.34, 21.15, 16.15, 16.25, 16.33, 16.45, 16.6],
    "Week6": [19.6, 19.8, 20.1, 20.1, 19.8, 21.23, 21.24, 21.26, 21.35, 21.34, 16.4, 16.51, 16.6, 16.7, 16.9],
    "Week7": [20.1, 20.4, 20.6, 20.7, 20.5, 21.78, 21.74, 21.81, 21.84, 21.85, 16.64, 16.81, 16.95, 17.12, 17.2],
    "Week8": [20.8, 21.2, 21.4, 21.5, 21.2, 22.45, 22.4, 22.36, 22.31, 22.35, 17.24, 17.34, 17.41, 17.5, 17.5],
    "Week9": [21.5, 21.8, 21.9, 21.9, 21.7, 23.17, 23.21, 23.19, 23.26, 23.15, 17.89, 17.85, 17.86, 17.91, 17.9],
    "Week10": [22.3, 22.5, 22.6, 22.5, 22.2, 23.71, 23.65, 23.71, 23.67, 23.54, 18.45, 18.32, 18.23, 18.27, 18.3],
    "Week11": [23, 23.1, 23.3, 23.1, 22.8, 24.15, 24.12, 24.25, 24.14, 24.12, 19.1, 18.75, 18.72, 18.67, 18.7],
    "Week12": [23.8, 24.3, 24.2, 23.9, 23.6, 25.2, 25.3, 25.1, 25.2, 25.1, 19.54, 19.24, 19.31, 19.26, 19.3]
}

surface_area_data = {
    "Treatment": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    "Replica": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Week1": [137, 135, 137, 138, 136, 134, 134, 135, 135, 134, 98, 98, 99, 98, 97],
    "Week2": [139, 140, 138, 140, 139, 136, 135, 137, 138, 135, 100, 100, 101, 101, 100],
    "Week3": [142, 143, 140, 141, 141, 138, 137, 138, 140, 137, 105, 105, 105, 106, 105],
    "Week4": [145, 145, 143, 144, 143, 140, 140, 141, 143, 140, 112, 112, 112, 112, 112],
    "Week5": [148, 148, 146, 147, 146, 145, 144, 144, 147, 145, 118, 117, 118, 118, 117],
    "Week6": [151, 151, 149, 149, 148, 148, 147, 147, 150, 147, 121, 121, 122, 121, 122],
    "Week7": [154, 153, 152, 153, 153, 152, 151, 152, 153, 152, 126, 126, 126, 126, 125],
    "Week8": [157, 156, 156, 156, 156, 155, 154, 155, 156, 154, 132, 133, 132, 131, 131],
    "Week9": [160, 160, 159, 159, 158, 158, 157, 157, 159, 158, 139, 139, 140, 139, 138],
    "Week10": [162, 163, 162, 162, 161, 162, 160, 161, 162, 161, 146, 146, 146, 146, 145],
    "Week11": [165, 166, 164, 164, 164, 165, 164, 163, 164, 164, 150, 150, 151, 150, 150],
    "Week12": [168, 168, 166, 167, 167, 168, 167, 167, 169, 167, 155, 155, 155, 155, 155]
}

# DataFrames for each sheet
maize_height_df = pd.DataFrame(maize_height_data)
number_of_leaves_df = pd.DataFrame(number_of_leaves_data)
stem_diameter_df = pd.DataFrame(stem_diameter_data)
surface_area_df = pd.DataFrame(surface_area_data)

# Reshape the data for ANOVA
maize_height_long = pd.melt(maize_height_df, id_vars=["Treatment", "Replica"], var_name="Week", value_name="Height")
number_of_leaves_long = pd.melt(number_of_leaves_df, id_vars=["Treatment", "Replica"], var_name="Week", value_name="NumberOfLeaves")
stem_diameter_long = pd.melt(stem_diameter_df, id_vars=["Treatment", "Replica"], var_name="Week", value_name="StemDiameter")
surface_area_long = pd.melt(surface_area_df, id_vars=["Treatment", "Replica"], var_name="Week", value_name="SurfaceArea")

# ANOVA for each metric
maize_height_anova = stats.f_oneway(
    maize_height_long[maize_height_long["Treatment"] == 1]["Height"],
    maize_height_long[maize_height_long["Treatment"] == 2]["Height"],
    maize_height_long[maize_height_long["Treatment"] == 3]["Height"]
)

number_of_leaves_anova = stats.f_oneway(
    number_of_leaves_long[number_of_leaves_long["Treatment"] == 1]["NumberOfLeaves"],
    number_of_leaves_long[number_of_leaves_long["Treatment"] == 2]["NumberOfLeaves"],
    number_of_leaves_long[number_of_leaves_long["Treatment"] == 3]["NumberOfLeaves"]
)

stem_diameter_anova = stats.f_oneway(
    stem_diameter_long[stem_diameter_long["Treatment"] == 1]["StemDiameter"],
    stem_diameter_long[stem_diameter_long["Treatment"] == 2]["StemDiameter"],
    stem_diameter_long[stem_diameter_long["Treatment"] == 3]["StemDiameter"]
)

surface_area_anova = stats.f_oneway(
    surface_area_long[surface_area_long["Treatment"] == 1]["SurfaceArea"],
    surface_area_long[surface_area_long["Treatment"] == 2]["SurfaceArea"],
    surface_area_long[surface_area_long["Treatment"] == 3]["SurfaceArea"]
)

# Results of the ANOVA tests
maize_height_anova, number_of_leaves_anova, stem_diameter_anova, surface_area_anova

print("The maize height anova is", maize_height_anova)
print("The number of leaves anova is", number_of_leaves_anova)
print("The stem diameter anova is", stem_diameter_anova)

print("The surface area anova is", surface_area_anova)