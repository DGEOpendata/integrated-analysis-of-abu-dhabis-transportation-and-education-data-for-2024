python
import pandas as pd

# Load the datasets
transport_df = pd.read_csv('public_transport_usage_2024.csv')
school_df = pd.read_excel('student_enrollment_grade_2024_0.xlsx')

# Merge datasets on common fields for integrated analysis
# Assume there is a common field 'municipality' for merging
merged_df = pd.merge(transport_df, school_df, on='municipality', how='inner')

# Example analysis: Identify peak transport times for schools
peak_transport_times = transport_df.groupby('route')['peak_time'].value_counts()
print("Peak transport times for popular routes:", peak_transport_times)

# Example analysis: School enrollment by municipality
school_enrollment_by_municipality = school_df.groupby('municipality')['enrollment'].sum()
print("School enrollment by municipality:", school_enrollment_by_municipality)

# Further analysis can be conducted as needed
