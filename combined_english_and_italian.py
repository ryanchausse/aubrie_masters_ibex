import pandas as pd, os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore
from scipy.stats import f_oneway
from itertools import islice
from dotenv import load_dotenv

print("This script will process the results from Ibex farm and display them/save them to a file"
      "in the 'results' directory")

# Assigning env variables for SFTP url, username, and password based on ENV variables
load_dotenv(dotenv_path='.env')

# Load all .env variables
results_location = str(os.environ.get('RESULTS_LOCATION'))
results_location_italian = str(os.environ.get('RESULTS_LOCATION_ITALIAN'))
results_processed_location = str(os.environ.get('RESULTS_PROCESSED_LOCATION'))

response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition A (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=a' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition A (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=a' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition A English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition A')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_a_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition A')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_a_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition B (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=b' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition B (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=b' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition B English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition B')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_b_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition B')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_b_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition C (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=c' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition C (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=c' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition C English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition C')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_c_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition C')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_c_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition D (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=d' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition D (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=d' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition D English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition D')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_d_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition D')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_d_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition E (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=e' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition E (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=e' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition E English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition E')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_e_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition E')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_e_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition F (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=f' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition F (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=f' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition F English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition F')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_f_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition F')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_f_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition G (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=g' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition G (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=g' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition G English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition G')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_g_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition G')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_g_combined.png')


response_7 = 0
response_6 = 0
response_5 = 0
response_4 = 0
response_3 = 0
response_2 = 0
response_1 = 0
ratings = {}
response_7_italian = 0
response_6_italian = 0
response_5_italian = 0
response_4_italian = 0
response_3_italian = 0
response_2_italian = 0
response_1_italian = 0
ratings_italian = {}

print('Condition H (English):')
with open(results_location) as f:
    for line in f:
        if 'cond=h' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7 += 1
            if 'NULL,6,NULL' in value_line:
                response_6 += 1
            if 'NULL,5,NULL' in value_line:
                response_5 += 1
            if 'NULL,4,NULL' in value_line:
                response_4 += 1
            if 'NULL,3,NULL' in value_line:
                response_3 += 1
            if 'NULL,2,NULL' in value_line:
                response_2 += 1
            if 'NULL,1,NULL' in value_line:
                response_1 += 1

f.close()
ratings = {7: response_7,
           6: response_6,
           5: response_5,
           4: response_4,
           3: response_3,
           2: response_2,
           1: response_1}

print(ratings)

print('Condition H (Italian):')
with open(results_location_italian) as f:
    for line in f:
        if 'cond=h' in line:
            # print(line)
            value_line = ''.join(islice(f, 1))
            if 'NULL,7,NULL' in value_line:
                response_7_italian += 1
            if 'NULL,6,NULL' in value_line:
                response_6_italian += 1
            if 'NULL,5,NULL' in value_line:
                response_5_italian += 1
            if 'NULL,4,NULL' in value_line:
                response_4_italian += 1
            if 'NULL,3,NULL' in value_line:
                response_3_italian += 1
            if 'NULL,2,NULL' in value_line:
                response_2_italian += 1
            if 'NULL,1,NULL' in value_line:
                response_1_italian += 1
f.close()
ratings_italian = {
    7: response_7_italian,
    6: response_6_italian,
    5: response_5_italian,
    4: response_4_italian,
    3: response_3_italian,
    2: response_2_italian,
    1: response_1_italian
}

print(ratings_italian)

data_frame = pd.DataFrame.from_dict(data=ratings, orient='index', dtype=int)
data_frame_italian = pd.DataFrame.from_dict(data=ratings_italian, orient='index', dtype=int)

english_value_list = list(ratings.values())[::-1]
italian_value_list = list(ratings_italian.values())[::-1]
labels = [1, 2, 3, 4, 5, 6, 7]
data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
one_way_anova = f_oneway(english_value_list, italian_value_list)
print('One-Way ANOVA for Condition H English/Italian speakers:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Create raw chart
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Frequency')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Likert Scores for Condition H')
plt.ylim([0, 210])
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
ax.bar_label(rects_english, padding=1, color='blue')
ax.bar_label(rects_italian, padding=1, color='red')
plt.savefig('./results/condition_h_combined.png')

# Create z-scored chart
z_scored_data_frame = data_frame.apply(zscore)
z_scored_data_frame_italian = data_frame_italian.apply(zscore)
labels = [1, 2, 3, 4, 5, 6, 7]
z_scores = [z_scored_data_frame.iloc[6][0], z_scored_data_frame.iloc[5][0], z_scored_data_frame.iloc[4][0],
            z_scored_data_frame.iloc[3][0], z_scored_data_frame.iloc[2][0], z_scored_data_frame.iloc[1][0],
            z_scored_data_frame.iloc[0][0]]
z_scores_italian = [z_scored_data_frame_italian.iloc[6][0], z_scored_data_frame_italian.iloc[5][0],
                    z_scored_data_frame_italian.iloc[4][0], z_scored_data_frame_italian.iloc[3][0],
                    z_scored_data_frame_italian.iloc[2][0], z_scored_data_frame_italian.iloc[1][0],
                    z_scored_data_frame_italian.iloc[0][0]]
rounded_z_scores = [round(num, 2) for num in z_scores[::-1]]
rounded_z_scores_italian = [round(num, 2) for num in z_scores_italian[::-1]]
data_frame_combined = pd.DataFrame({'English': rounded_z_scores[::-1], 'Italian': rounded_z_scores_italian[::-1]}, index=labels)
ax = data_frame_combined.plot.bar(rot=0)
ax.set_ylabel('Z-Score')
ax.set_xlabel('Responses (unnatural to perfectly natural)')
ax.set_title('Z-Scores for Condition H')
plt.ylim([-2.45, 2.45])
plt.savefig('./results/z_scores_condition_h_combined.png')
