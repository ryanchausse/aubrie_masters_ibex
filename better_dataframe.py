import pandas as pd, numpy as np, os, time, base64, pysftp, glob, datetime, pathlib
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
from scipy.stats import zscore
from dateutil import tz
from itertools import islice
from dotenv import load_dotenv

print("This script will process the Likert scale results from Ibex Farm, categorize into three groups (acceptable, "
      "neutral, and unnatural) and display them/save them to a file in the 'results' directory")

# Assigning env variables for SFTP url, username, and password based on ENV variables
load_dotenv(dotenv_path='.env')

# Load all .env variables
results_location = str(os.environ.get('RESULTS_LOCATION'))
results_location_italian = str(os.environ.get('RESULTS_LOCATION_ITALIAN'))
results_processed_location = str(os.environ.get('RESULTS_PROCESSED_LOCATION'))

# First, create giant 2D matrix of all data in a pandas dataframe, then do operations on that matrix
# Should look like:
# MD5 hash, response_a_1, response_a_2, ... response_h_4

# English group first
user_md5_buffer = ''
user_results = {}
all_user_results = []
user_add_time_taken = 0
a_counter = 1
b_counter = 1
c_counter = 1
d_counter = 1
e_counter = 1
f_counter = 1
g_counter = 1
h_counter = 1

with open(results_location) as f:
    for line in f:
        likert_score = 0
        if ',Form,2,0,intro,NULL,age,' in line:
            # first line of relevant results for user
            timestamp_and_md5 = line[:43:1]
            user_md5 = timestamp_and_md5.split(',')[1]
            if not user_md5_buffer:
                user_md5_buffer = user_md5
                user_results = {'md5_hash': user_md5, 'total_time': 0}
            if user_md5 != user_md5_buffer:
                # Save user_results into list of dicts; start recording new experimental subject's results
                user_results['total_time'] = round(user_add_time_taken / 1000 / 60, 2)  # Outputs minutes
                all_user_results.append(user_results)
                user_results = {'md5_hash': user_md5, 'total_time': 0}
                a_counter = 1
                b_counter = 1
                c_counter = 1
                d_counter = 1
                e_counter = 1
                f_counter = 1
                g_counter = 1
                h_counter = 1
                user_add_time_taken = 0
            # Find age and add to user_results for this user
            user_results['age'] = int(line.split('age,')[-1].strip())
        if ',Form,2,0,intro,NULL,bilingual_languages,' in line:
            user_results['bilingual_languages'] = line.split('bilingual_languages,')[-1].strip()
        if ',Form,2,0,intro,NULL,bilingual,' in line:
            user_results['bilingual'] = line.split('bilingual,')[-1].strip()
        if ',Form,2,0,intro,NULL,EdL,' in line:
            user_results['education_level'] = line.split('EdL,')[-1].strip()
        if ',Form,2,0,intro,NULL,AoA,' in line:
            user_results['age_of_acquisition'] = "=\"" + line.split('AoA,')[-1].strip() + "\""
        if ',Form,5,0,feedback,NULL,fdbk_problems_difficulties,' in line:
            user_results['problems_difficulties'] = line.split('fdbk_problems_difficulties,')[-1].strip()
        if ',Form,5,0,feedback,NULL,fdbk_experiment_about,' in line:
            user_results['experiment_about'] = line.split('fdbk_experiment_about,')[-1].strip()
        if ',Form,5,0,feedback,NULL,fdbk_other_notes_questions,' in line:
            user_results['other_notes_questions'] = line.split('fdbk_other_notes_questions,')[-1].strip()
        if 'https://ryanchausse.com/aubrie_masters/images/conversation_pics/' in line:
            value_line = ''.join(islice(f, 1))
            likert_score_location = int(value_line.find(',NULL,NULL,'))
            if int(likert_score_location) != -1:
                likert_point_location = 11 + likert_score_location
            else:
                likert_score_location = int(value_line.find(',NULL,'))
                likert_point_location = 6 + likert_score_location
            likert_score += int(value_line[likert_point_location])
            user_add_time_taken += int(value_line.split(',')[-1])
            # print(line)
            # print('value line: ' + value_line)
            if 'cond=a' in line:
                user_results['response_a' + str(a_counter)] = likert_score
                a_counter += 1
            if 'cond=b' in line:
                user_results['response_b' + str(b_counter)] = likert_score
                b_counter += 1
            if 'cond=c' in line:
                user_results['response_c' + str(c_counter)] = likert_score
                c_counter += 1
            if 'cond=d' in line:
                user_results['response_d' + str(d_counter)] = likert_score
                d_counter += 1
            if 'cond=e' in line:
                user_results['response_e' + str(e_counter)] = likert_score
                e_counter += 1
            if 'cond=f' in line:
                user_results['response_f' + str(f_counter)] = likert_score
                f_counter += 1
            if 'cond=g' in line:
                user_results['response_g' + str(g_counter)] = likert_score
                g_counter += 1
            if 'cond=h' in line:
                user_results['response_h' + str(h_counter)] = likert_score
                h_counter += 1
            user_md5_buffer = user_md5
f.close()

data_frame = pd.DataFrame(data=all_user_results)
ordered_data_frame = data_frame[[
    'md5_hash', 'total_time', 'age', 'age_of_acquisition',
    'education_level', 'bilingual', 'bilingual_languages',
    'problems_difficulties', 'experiment_about', 'other_notes_questions',
    'response_a1', 'response_a2', 'response_a3', 'response_a4',
    'response_b1', 'response_b2', 'response_b3', 'response_b4',
    'response_c1', 'response_c2', 'response_c3', 'response_c4',
    'response_d1', 'response_d2', 'response_d3', 'response_d4',
    'response_e1', 'response_e2', 'response_e3', 'response_e4',
    'response_f1', 'response_f2', 'response_f3', 'response_f4',
    'response_g1', 'response_g2', 'response_g3', 'response_g4',
    'response_h1', 'response_h2', 'response_h3', 'response_h4'
]]
ordered_data_frame.to_csv('./results/full_data.csv')
# print(ordered_data_frame)

# Italian group now

user_md5_buffer = ''
user_results = {}
all_user_results = []
user_add_time_taken = 0
a_counter = 1
b_counter = 1
c_counter = 1
d_counter = 1
e_counter = 1
f_counter = 1
g_counter = 1
h_counter = 1
eng_activity_counter = 0

with open(results_location_italian) as f:
    for line in f:
        likert_score = 0
        if ',Form,2,0,intro,NULL,age,' in line:
            # first line of relevant results for user
            timestamp_and_md5 = line[:43:1]
            user_md5 = timestamp_and_md5.split(',')[1]
            if not user_md5_buffer:
                user_md5_buffer = user_md5
                user_results = {'md5_hash': user_md5, 'total_time': 0}
            if user_md5 != user_md5_buffer:
                # Save user_results into list of dicts; start recording new experimental subject's results
                user_results['total_time'] = round(user_add_time_taken / 1000 / 60, 2)  # Outputs minutes
                all_user_results.append(user_results)
                user_results = {'md5_hash': user_md5, 'total_time': 0}
                a_counter = 1
                b_counter = 1
                c_counter = 1
                d_counter = 1
                e_counter = 1
                f_counter = 1
                g_counter = 1
                h_counter = 1
                eng_activity_counter = 0
                user_add_time_taken = 0
            # Find age and add to user_results for this user
            user_results['age'] = int(line.split('age,')[-1].strip())
        if ',Form,2,0,intro,NULL,bilingual_languages,' in line:
            user_results['bilingual_languages'] = line.split('bilingual_languages,')[-1].strip()
        if ',Form,2,0,intro,NULL,bilingual,' in line:
            user_results['bilingual'] = line.split('bilingual,')[-1].strip()
        if ',Form,2,0,intro,NULL,EngL,' in line:
            user_results['english_level'] = line.split('EngL,')[-1].strip()
        if ',Form,2,0,intro,NULL,EngC,' in line:
            user_results['time_in_english_country'] = line.split('EngC,')[-1].strip()
        if ',Form,2,0,intro,NULL,AoA,' in line:
            user_results['age_of_acquisition'] = "=\"" + line.split('AoA,')[-1].strip() + "\""
        if ',Form,2,0,intro,NULL,EngHist,' in line:
            user_results['english_history'] = line.split('EngHist,')[-1].strip()
        if ',Form,5,0,feedback,NULL,fdbk_problems_difficulties,' in line:
            user_results['problems_difficulties'] = line.split('fdbk_problems_difficulties,')[-1].strip()
        if ',Form,5,0,feedback,NULL,fdbk_experiment_about,' in line:
            user_results['experiment_about'] = line.split('fdbk_experiment_about,')[-1].strip()
        if ',Form,5,0,feedback,NULL,fdbk_other_notes_questions,' in line:
            user_results['other_notes_questions'] = line.split('fdbk_other_notes_questions,')[-1].strip()
        if ',Form,5,0,feedback,NULL,above_ability,' in line:
            user_results['above_ability'] = line.split('above_ability,')[-1].strip()
        # Assumption here that web form inputs came across in order due to Ibexfarm platform
        if ',Form,2,0,intro,NULL,EngAct,' in line:
            if eng_activity_counter == 0:
                # traditional classes
                user_results['traditional_classes'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 1:
                # private tutoring
                user_results['private_tutoring'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 2:
                # language learning tech (Duolingo et Al.)
                user_results['language_learning_tech'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 3:
                # social media
                user_results['social_media'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 4:
                # video games
                user_results['video_games'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 5:
                # in-person conversations
                user_results['in_person_conversations'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 6:
                # private messaging
                user_results['private_messaging'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 7:
                # emails with native english speakers
                user_results['emails_with_native_english'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 8:
                # media in english
                user_results['media_in_english'] = line.split('EngAct,')[-1].strip()
            if eng_activity_counter == 9:
                # books in english
                user_results['books_in_english'] = line.split('EngAct,')[-1].strip()
            eng_activity_counter += 1
        if 'https://ryanchausse.com/aubrie_masters_italian/images/conversation_pics/' in line:
            value_line = ''.join(islice(f, 1))
            likert_score_location = int(value_line.find(',NULL,NULL,'))
            if int(likert_score_location) != -1:
                likert_point_location = 11 + likert_score_location
            else:
                likert_score_location = int(value_line.find(',NULL,'))
                likert_point_location = 6 + likert_score_location
            likert_score += int(value_line[likert_point_location])
            user_add_time_taken += int(value_line.split(',')[-1])
            # print(line)
            # print('value line: ' + value_line)
            if 'cond=a' in line:
                user_results['response_a' + str(a_counter)] = likert_score
                a_counter += 1
            if 'cond=b' in line:
                user_results['response_b' + str(b_counter)] = likert_score
                b_counter += 1
            if 'cond=c' in line:
                user_results['response_c' + str(c_counter)] = likert_score
                c_counter += 1
            if 'cond=d' in line:
                user_results['response_d' + str(d_counter)] = likert_score
                d_counter += 1
            if 'cond=e' in line:
                user_results['response_e' + str(e_counter)] = likert_score
                e_counter += 1
            if 'cond=f' in line:
                user_results['response_f' + str(f_counter)] = likert_score
                f_counter += 1
            if 'cond=g' in line:
                user_results['response_g' + str(g_counter)] = likert_score
                g_counter += 1
            if 'cond=h' in line:
                user_results['response_h' + str(h_counter)] = likert_score
                h_counter += 1
            user_md5_buffer = user_md5
f.close()

data_frame = pd.DataFrame(data=all_user_results)
ordered_data_frame_italian = data_frame[[
    'md5_hash', 'total_time', 'age', 'english_level',
    'age_of_acquisition', 'bilingual', 'bilingual_languages',
    'time_in_english_country', 'english_history',
    'traditional_classes', 'private_tutoring', 'language_learning_tech',
    'social_media', 'video_games', 'in_person_conversations',
    'private_messaging', 'emails_with_native_english', 'media_in_english',
    'books_in_english', 'problems_difficulties',
    'experiment_about', 'other_notes_questions', 'above_ability',
    'response_a1', 'response_a2', 'response_a3', 'response_a4',
    'response_b1', 'response_b2', 'response_b3', 'response_b4',
    'response_c1', 'response_c2', 'response_c3', 'response_c4',
    'response_d1', 'response_d2', 'response_d3', 'response_d4',
    'response_e1', 'response_e2', 'response_e3', 'response_e4',
    'response_f1', 'response_f2', 'response_f3', 'response_f4',
    'response_g1', 'response_g2', 'response_g3', 'response_g4',
    'response_h1', 'response_h2', 'response_h3', 'response_h4'
]]
ordered_data_frame_italian.to_csv('./results/full_data_italian.csv')
# print(ordered_data_frame_italian)

# Now make a chart for each condition with three groups:
# english native speakers
# low competence english speaking italians (= A1-A2, B1-B2)
# high competence english speaking italians (= C1-C2)

# Create new dataframe like:
# english_competence_level avg_score_a avg_score_b ... avg_score_h

ordered_data_frame['avg_a'] = ordered_data_frame[['response_a1', 'response_a2', 'response_a3', 'response_a4']].mean(axis=1)
ordered_data_frame['avg_b'] = ordered_data_frame[['response_b1', 'response_b2', 'response_b3', 'response_b4']].mean(axis=1)
ordered_data_frame['avg_c'] = ordered_data_frame[['response_c1', 'response_c2', 'response_c3', 'response_c4']].mean(axis=1)
ordered_data_frame['avg_d'] = ordered_data_frame[['response_d1', 'response_d2', 'response_d3', 'response_d4']].mean(axis=1)
ordered_data_frame['avg_e'] = ordered_data_frame[['response_e1', 'response_e2', 'response_e3', 'response_e4']].mean(axis=1)
ordered_data_frame['avg_f'] = ordered_data_frame[['response_f1', 'response_f2', 'response_f3', 'response_f4']].mean(axis=1)
ordered_data_frame['avg_g'] = ordered_data_frame[['response_g1', 'response_g2', 'response_g3', 'response_g4']].mean(axis=1)
ordered_data_frame['avg_h'] = ordered_data_frame[['response_h1', 'response_h2', 'response_h3', 'response_h4']].mean(axis=1)

ordered_data_frame_italian['avg_a'] = ordered_data_frame_italian[['response_a1', 'response_a2', 'response_a3', 'response_a4']].mean(axis=1)
ordered_data_frame_italian['avg_b'] = ordered_data_frame_italian[['response_b1', 'response_b2', 'response_b3', 'response_b4']].mean(axis=1)
ordered_data_frame_italian['avg_c'] = ordered_data_frame_italian[['response_c1', 'response_c2', 'response_c3', 'response_c4']].mean(axis=1)
ordered_data_frame_italian['avg_d'] = ordered_data_frame_italian[['response_d1', 'response_d2', 'response_d3', 'response_d4']].mean(axis=1)
ordered_data_frame_italian['avg_e'] = ordered_data_frame_italian[['response_e1', 'response_e2', 'response_e3', 'response_e4']].mean(axis=1)
ordered_data_frame_italian['avg_f'] = ordered_data_frame_italian[['response_f1', 'response_f2', 'response_f3', 'response_f4']].mean(axis=1)
ordered_data_frame_italian['avg_g'] = ordered_data_frame_italian[['response_g1', 'response_g2', 'response_g3', 'response_g4']].mean(axis=1)
ordered_data_frame_italian['avg_h'] = ordered_data_frame_italian[['response_h1', 'response_h2', 'response_h3', 'response_h4']].mean(axis=1)

low_competence_italian = ordered_data_frame_italian.loc[ordered_data_frame_italian['english_level'].isin(['A1-A2', 'B1-B2'])]
high_competence_italian = ordered_data_frame_italian.loc[ordered_data_frame_italian['english_level'] == 'C1-C2']

competence_vs_avg_score_condition = [
    {
        'english_competence_level': 'Native',
        'condition_a': ordered_data_frame["avg_a"].mean(),
        'condition_b': ordered_data_frame["avg_b"].mean(),
        'condition_c': ordered_data_frame["avg_c"].mean(),
        'condition_d': ordered_data_frame["avg_d"].mean(),
        'condition_e': ordered_data_frame["avg_e"].mean(),
        'condition_f': ordered_data_frame["avg_f"].mean(),
        'condition_g': ordered_data_frame["avg_g"].mean(),
        'condition_h': ordered_data_frame["avg_h"].mean()
     },
    {
        'english_competence_level': 'Low competence',
        'condition_a': low_competence_italian["avg_a"].mean(),
        'condition_b': low_competence_italian["avg_b"].mean(),
        'condition_c': low_competence_italian["avg_c"].mean(),
        'condition_d': low_competence_italian["avg_d"].mean(),
        'condition_e': low_competence_italian["avg_e"].mean(),
        'condition_f': low_competence_italian["avg_f"].mean(),
        'condition_g': low_competence_italian["avg_g"].mean(),
        'condition_h': low_competence_italian["avg_h"].mean()
    },
    {
        'english_competence_level': 'High competence',
        'condition_a': high_competence_italian["avg_a"].mean(),
        'condition_b': high_competence_italian["avg_b"].mean(),
        'condition_c': high_competence_italian["avg_c"].mean(),
        'condition_d': high_competence_italian["avg_d"].mean(),
        'condition_e': high_competence_italian["avg_e"].mean(),
        'condition_f': high_competence_italian["avg_f"].mean(),
        'condition_g': high_competence_italian["avg_g"].mean(),
        'condition_h': high_competence_italian["avg_h"].mean()
    }
]

# Create chart
data_frame_combined = {
    'Native': [
        ordered_data_frame["avg_a"].mean(),
        ordered_data_frame["avg_b"].mean(),
        ordered_data_frame["avg_c"].mean(),
        ordered_data_frame["avg_d"].mean(),
        ordered_data_frame["avg_e"].mean(),
        ordered_data_frame["avg_f"].mean(),
        ordered_data_frame["avg_g"].mean(),
        ordered_data_frame["avg_h"].mean()
    ],
    'High competence (C1-C2)': [
        high_competence_italian["avg_a"].mean(),
        high_competence_italian["avg_b"].mean(),
        high_competence_italian["avg_c"].mean(),
        high_competence_italian["avg_d"].mean(),
        high_competence_italian["avg_e"].mean(),
        high_competence_italian["avg_f"].mean(),
        high_competence_italian["avg_g"].mean(),
        high_competence_italian["avg_h"].mean()
    ],
    'Low competence (A1-B2)': [
        low_competence_italian["avg_a"].mean(),
        low_competence_italian["avg_b"].mean(),
        low_competence_italian["avg_c"].mean(),
        low_competence_italian["avg_d"].mean(),
        low_competence_italian["avg_e"].mean(),
        low_competence_italian["avg_f"].mean(),
        low_competence_italian["avg_g"].mean(),
        low_competence_italian["avg_h"].mean()
    ]
}

labels = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
]

chart_data_frame = pd.DataFrame(data_frame_combined, index=labels)
ax = chart_data_frame.plot.bar(rot=0)
ax.set_ylabel('Average Response Score')
ax.set_xlabel('Condition')
ax.set_title('Likert Scores by English Level per Condition')
plt.ylim([3, 7])
plt.savefig('./results/english_competence_and_condition_combined.png')

# Try to create a minmax scaled score for each likert score per user in order to
# fit responses on a normalized Gaussian distribution, then chart.
ordered_data_frame['response_a1_normalized'] = ''
ordered_data_frame['response_a2_normalized'] = ''
ordered_data_frame['response_a3_normalized'] = ''
ordered_data_frame['response_a4_normalized'] = ''
ordered_data_frame['response_b1_normalized'] = ''
ordered_data_frame['response_b2_normalized'] = ''
ordered_data_frame['response_b3_normalized'] = ''
ordered_data_frame['response_b4_normalized'] = ''
ordered_data_frame['response_c1_normalized'] = ''
ordered_data_frame['response_c2_normalized'] = ''
ordered_data_frame['response_c3_normalized'] = ''
ordered_data_frame['response_c4_normalized'] = ''
ordered_data_frame['response_d1_normalized'] = ''
ordered_data_frame['response_d2_normalized'] = ''
ordered_data_frame['response_d3_normalized'] = ''
ordered_data_frame['response_d4_normalized'] = ''
ordered_data_frame['response_e1_normalized'] = ''
ordered_data_frame['response_e2_normalized'] = ''
ordered_data_frame['response_e3_normalized'] = ''
ordered_data_frame['response_e4_normalized'] = ''
ordered_data_frame['response_f1_normalized'] = ''
ordered_data_frame['response_f2_normalized'] = ''
ordered_data_frame['response_f3_normalized'] = ''
ordered_data_frame['response_f4_normalized'] = ''
ordered_data_frame['response_g1_normalized'] = ''
ordered_data_frame['response_g2_normalized'] = ''
ordered_data_frame['response_g3_normalized'] = ''
ordered_data_frame['response_g4_normalized'] = ''
ordered_data_frame['response_h1_normalized'] = ''
ordered_data_frame['response_h2_normalized'] = ''
ordered_data_frame['response_h3_normalized'] = ''
ordered_data_frame['response_h4_normalized'] = ''

for index, row in ordered_data_frame.iterrows():
    rowwise_raw_scores = list()
    rowwise_raw_scores.append([row['response_a1'], row['response_a2'], row['response_a3'], row['response_a4']])
    rowwise_raw_scores.append([row['response_b1'], row['response_b2'], row['response_b3'], row['response_b4']])
    rowwise_raw_scores.append([row['response_c1'], row['response_c2'], row['response_c3'], row['response_c4']])
    rowwise_raw_scores.append([row['response_d1'], row['response_d2'], row['response_d3'], row['response_d4']])
    rowwise_raw_scores.append([row['response_e1'], row['response_e2'], row['response_e3'], row['response_e4']])
    rowwise_raw_scores.append([row['response_f1'], row['response_f2'], row['response_f3'], row['response_f4']])
    rowwise_raw_scores.append([row['response_g1'], row['response_g2'], row['response_g3'], row['response_g4']])
    rowwise_raw_scores.append([row['response_h1'], row['response_h2'], row['response_h3'], row['response_h4']])
    # Now normalize these scores (in this per-user range/variance context) and append to dataframe
    scalar = preprocessing.StandardScaler().fit(rowwise_raw_scores)
    x_scaled = scalar.transform(rowwise_raw_scores)
    ordered_data_frame.loc[index, 'response_a1_normalized'] = x_scaled[0][0]
    ordered_data_frame.loc[index, 'response_a2_normalized'] = x_scaled[0][1]
    ordered_data_frame.loc[index, 'response_a3_normalized'] = x_scaled[0][2]
    ordered_data_frame.loc[index, 'response_a4_normalized'] = x_scaled[0][3]
    ordered_data_frame.loc[index, 'response_b1_normalized'] = x_scaled[1][0]
    ordered_data_frame.loc[index, 'response_b2_normalized'] = x_scaled[1][1]
    ordered_data_frame.loc[index, 'response_b3_normalized'] = x_scaled[1][2]
    ordered_data_frame.loc[index, 'response_b4_normalized'] = x_scaled[1][3]
    ordered_data_frame.loc[index, 'response_c1_normalized'] = x_scaled[2][0]
    ordered_data_frame.loc[index, 'response_c2_normalized'] = x_scaled[2][1]
    ordered_data_frame.loc[index, 'response_c3_normalized'] = x_scaled[2][2]
    ordered_data_frame.loc[index, 'response_c4_normalized'] = x_scaled[2][3]
    ordered_data_frame.loc[index, 'response_d1_normalized'] = x_scaled[3][0]
    ordered_data_frame.loc[index, 'response_d2_normalized'] = x_scaled[3][1]
    ordered_data_frame.loc[index, 'response_d3_normalized'] = x_scaled[3][2]
    ordered_data_frame.loc[index, 'response_d4_normalized'] = x_scaled[3][3]
    ordered_data_frame.loc[index, 'response_e1_normalized'] = x_scaled[4][0]
    ordered_data_frame.loc[index, 'response_e2_normalized'] = x_scaled[4][1]
    ordered_data_frame.loc[index, 'response_e3_normalized'] = x_scaled[4][2]
    ordered_data_frame.loc[index, 'response_e4_normalized'] = x_scaled[4][3]
    ordered_data_frame.loc[index, 'response_f1_normalized'] = x_scaled[5][0]
    ordered_data_frame.loc[index, 'response_f2_normalized'] = x_scaled[5][1]
    ordered_data_frame.loc[index, 'response_f3_normalized'] = x_scaled[5][2]
    ordered_data_frame.loc[index, 'response_f4_normalized'] = x_scaled[5][3]
    ordered_data_frame.loc[index, 'response_g1_normalized'] = x_scaled[6][0]
    ordered_data_frame.loc[index, 'response_g2_normalized'] = x_scaled[6][1]
    ordered_data_frame.loc[index, 'response_g3_normalized'] = x_scaled[6][2]
    ordered_data_frame.loc[index, 'response_g4_normalized'] = x_scaled[6][3]
    ordered_data_frame.loc[index, 'response_h1_normalized'] = x_scaled[7][0]
    ordered_data_frame.loc[index, 'response_h2_normalized'] = x_scaled[7][1]
    ordered_data_frame.loc[index, 'response_h3_normalized'] = x_scaled[7][2]
    ordered_data_frame.loc[index, 'response_h4_normalized'] = x_scaled[7][3]

ordered_data_frame['avg_a_normalized'] = ordered_data_frame[['response_a1_normalized', 'response_a2_normalized', 'response_a3_normalized', 'response_a4_normalized']].mean(axis=1)
ordered_data_frame['avg_b_normalized'] = ordered_data_frame[['response_b1_normalized', 'response_b2_normalized', 'response_b3_normalized', 'response_b4_normalized']].mean(axis=1)
ordered_data_frame['avg_c_normalized'] = ordered_data_frame[['response_c1_normalized', 'response_c2_normalized', 'response_c3_normalized', 'response_c4_normalized']].mean(axis=1)
ordered_data_frame['avg_d_normalized'] = ordered_data_frame[['response_d1_normalized', 'response_d2_normalized', 'response_d3_normalized', 'response_d4_normalized']].mean(axis=1)
ordered_data_frame['avg_e_normalized'] = ordered_data_frame[['response_e1_normalized', 'response_e2_normalized', 'response_e3_normalized', 'response_e4_normalized']].mean(axis=1)
ordered_data_frame['avg_f_normalized'] = ordered_data_frame[['response_f1_normalized', 'response_f2_normalized', 'response_f3_normalized', 'response_f4_normalized']].mean(axis=1)
ordered_data_frame['avg_g_normalized'] = ordered_data_frame[['response_g1_normalized', 'response_g2_normalized', 'response_g3_normalized', 'response_g4_normalized']].mean(axis=1)
ordered_data_frame['avg_h_normalized'] = ordered_data_frame[['response_h1_normalized', 'response_h2_normalized', 'response_h3_normalized', 'response_h4_normalized']].mean(axis=1)

# print(ordered_data_frame)
ordered_data_frame.to_csv('./results/full_data_english_native.csv')

# Create chart
data_frame_combined = {
    'Native': [
        ordered_data_frame["avg_a_normalized"].mean(),
        ordered_data_frame["avg_b_normalized"].mean(),
        ordered_data_frame["avg_c_normalized"].mean(),
        ordered_data_frame["avg_d_normalized"].mean(),
        ordered_data_frame["avg_e_normalized"].mean(),
        ordered_data_frame["avg_f_normalized"].mean(),
        ordered_data_frame["avg_g_normalized"].mean(),
        ordered_data_frame["avg_h_normalized"].mean()
    ]
}

labels = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
]

chart_data_frame = pd.DataFrame(data_frame_combined, index=labels)
ax = chart_data_frame.plot.bar(rot=0)
ax.set_ylabel('Average Normalized Response Score per User')
ax.set_xlabel('Condition')
ax.set_title('Average Normalized Scores per Condition for English Speakers')
plt.savefig('./results/english_normalized_by_competence_and_condition_combined.png')


# PoC for English native speakers complete. Now, do High and Low competence english speaking Italian groups
# and plot on same chart

high_competence_italian['response_a1_normalized'] = ''
high_competence_italian['response_a2_normalized'] = ''
high_competence_italian['response_a3_normalized'] = ''
high_competence_italian['response_a4_normalized'] = ''
high_competence_italian['response_b1_normalized'] = ''
high_competence_italian['response_b2_normalized'] = ''
high_competence_italian['response_b3_normalized'] = ''
high_competence_italian['response_b4_normalized'] = ''
high_competence_italian['response_c1_normalized'] = ''
high_competence_italian['response_c2_normalized'] = ''
high_competence_italian['response_c3_normalized'] = ''
high_competence_italian['response_c4_normalized'] = ''
high_competence_italian['response_d1_normalized'] = ''
high_competence_italian['response_d2_normalized'] = ''
high_competence_italian['response_d3_normalized'] = ''
high_competence_italian['response_d4_normalized'] = ''
high_competence_italian['response_e1_normalized'] = ''
high_competence_italian['response_e2_normalized'] = ''
high_competence_italian['response_e3_normalized'] = ''
high_competence_italian['response_e4_normalized'] = ''
high_competence_italian['response_f1_normalized'] = ''
high_competence_italian['response_f2_normalized'] = ''
high_competence_italian['response_f3_normalized'] = ''
high_competence_italian['response_f4_normalized'] = ''
high_competence_italian['response_g1_normalized'] = ''
high_competence_italian['response_g2_normalized'] = ''
high_competence_italian['response_g3_normalized'] = ''
high_competence_italian['response_g4_normalized'] = ''
high_competence_italian['response_h1_normalized'] = ''
high_competence_italian['response_h2_normalized'] = ''
high_competence_italian['response_h3_normalized'] = ''
high_competence_italian['response_h4_normalized'] = ''

for index, row in high_competence_italian.iterrows():
    rowwise_raw_scores = list()
    rowwise_raw_scores.append([row['response_a1'], row['response_a2'], row['response_a3'], row['response_a4']])
    rowwise_raw_scores.append([row['response_b1'], row['response_b2'], row['response_b3'], row['response_b4']])
    rowwise_raw_scores.append([row['response_c1'], row['response_c2'], row['response_c3'], row['response_c4']])
    rowwise_raw_scores.append([row['response_d1'], row['response_d2'], row['response_d3'], row['response_d4']])
    rowwise_raw_scores.append([row['response_e1'], row['response_e2'], row['response_e3'], row['response_e4']])
    rowwise_raw_scores.append([row['response_f1'], row['response_f2'], row['response_f3'], row['response_f4']])
    rowwise_raw_scores.append([row['response_g1'], row['response_g2'], row['response_g3'], row['response_g4']])
    rowwise_raw_scores.append([row['response_h1'], row['response_h2'], row['response_h3'], row['response_h4']])
    # Now normalize these scores (in this per-user range/variance context) and append to dataframe
    scalar = preprocessing.StandardScaler().fit(rowwise_raw_scores)
    x_scaled = scalar.transform(rowwise_raw_scores)
    high_competence_italian.loc[index, 'response_a1_normalized'] = x_scaled[0][0]
    high_competence_italian.loc[index, 'response_a2_normalized'] = x_scaled[0][1]
    high_competence_italian.loc[index, 'response_a3_normalized'] = x_scaled[0][2]
    high_competence_italian.loc[index, 'response_a4_normalized'] = x_scaled[0][3]
    high_competence_italian.loc[index, 'response_b1_normalized'] = x_scaled[1][0]
    high_competence_italian.loc[index, 'response_b2_normalized'] = x_scaled[1][1]
    high_competence_italian.loc[index, 'response_b3_normalized'] = x_scaled[1][2]
    high_competence_italian.loc[index, 'response_b4_normalized'] = x_scaled[1][3]
    high_competence_italian.loc[index, 'response_c1_normalized'] = x_scaled[2][0]
    high_competence_italian.loc[index, 'response_c2_normalized'] = x_scaled[2][1]
    high_competence_italian.loc[index, 'response_c3_normalized'] = x_scaled[2][2]
    high_competence_italian.loc[index, 'response_c4_normalized'] = x_scaled[2][3]
    high_competence_italian.loc[index, 'response_d1_normalized'] = x_scaled[3][0]
    high_competence_italian.loc[index, 'response_d2_normalized'] = x_scaled[3][1]
    high_competence_italian.loc[index, 'response_d3_normalized'] = x_scaled[3][2]
    high_competence_italian.loc[index, 'response_d4_normalized'] = x_scaled[3][3]
    high_competence_italian.loc[index, 'response_e1_normalized'] = x_scaled[4][0]
    high_competence_italian.loc[index, 'response_e2_normalized'] = x_scaled[4][1]
    high_competence_italian.loc[index, 'response_e3_normalized'] = x_scaled[4][2]
    high_competence_italian.loc[index, 'response_e4_normalized'] = x_scaled[4][3]
    high_competence_italian.loc[index, 'response_f1_normalized'] = x_scaled[5][0]
    high_competence_italian.loc[index, 'response_f2_normalized'] = x_scaled[5][1]
    high_competence_italian.loc[index, 'response_f3_normalized'] = x_scaled[5][2]
    high_competence_italian.loc[index, 'response_f4_normalized'] = x_scaled[5][3]
    high_competence_italian.loc[index, 'response_g1_normalized'] = x_scaled[6][0]
    high_competence_italian.loc[index, 'response_g2_normalized'] = x_scaled[6][1]
    high_competence_italian.loc[index, 'response_g3_normalized'] = x_scaled[6][2]
    high_competence_italian.loc[index, 'response_g4_normalized'] = x_scaled[6][3]
    high_competence_italian.loc[index, 'response_h1_normalized'] = x_scaled[7][0]
    high_competence_italian.loc[index, 'response_h2_normalized'] = x_scaled[7][1]
    high_competence_italian.loc[index, 'response_h3_normalized'] = x_scaled[7][2]
    high_competence_italian.loc[index, 'response_h4_normalized'] = x_scaled[7][3]

high_competence_italian['avg_a_normalized'] = high_competence_italian[['response_a1_normalized', 'response_a2_normalized', 'response_a3_normalized', 'response_a4_normalized']].mean(axis=1)
high_competence_italian['avg_b_normalized'] = high_competence_italian[['response_b1_normalized', 'response_b2_normalized', 'response_b3_normalized', 'response_b4_normalized']].mean(axis=1)
high_competence_italian['avg_c_normalized'] = high_competence_italian[['response_c1_normalized', 'response_c2_normalized', 'response_c3_normalized', 'response_c4_normalized']].mean(axis=1)
high_competence_italian['avg_d_normalized'] = high_competence_italian[['response_d1_normalized', 'response_d2_normalized', 'response_d3_normalized', 'response_d4_normalized']].mean(axis=1)
high_competence_italian['avg_e_normalized'] = high_competence_italian[['response_e1_normalized', 'response_e2_normalized', 'response_e3_normalized', 'response_e4_normalized']].mean(axis=1)
high_competence_italian['avg_f_normalized'] = high_competence_italian[['response_f1_normalized', 'response_f2_normalized', 'response_f3_normalized', 'response_f4_normalized']].mean(axis=1)
high_competence_italian['avg_g_normalized'] = high_competence_italian[['response_g1_normalized', 'response_g2_normalized', 'response_g3_normalized', 'response_g4_normalized']].mean(axis=1)
high_competence_italian['avg_h_normalized'] = high_competence_italian[['response_h1_normalized', 'response_h2_normalized', 'response_h3_normalized', 'response_h4_normalized']].mean(axis=1)

# print(high_competence_italian)
high_competence_italian.to_csv('./results/full_data_high_competence.csv')

low_competence_italian['response_a1_normalized'] = ''
low_competence_italian['response_a2_normalized'] = ''
low_competence_italian['response_a3_normalized'] = ''
low_competence_italian['response_a4_normalized'] = ''
low_competence_italian['response_b1_normalized'] = ''
low_competence_italian['response_b2_normalized'] = ''
low_competence_italian['response_b3_normalized'] = ''
low_competence_italian['response_b4_normalized'] = ''
low_competence_italian['response_c1_normalized'] = ''
low_competence_italian['response_c2_normalized'] = ''
low_competence_italian['response_c3_normalized'] = ''
low_competence_italian['response_c4_normalized'] = ''
low_competence_italian['response_d1_normalized'] = ''
low_competence_italian['response_d2_normalized'] = ''
low_competence_italian['response_d3_normalized'] = ''
low_competence_italian['response_d4_normalized'] = ''
low_competence_italian['response_e1_normalized'] = ''
low_competence_italian['response_e2_normalized'] = ''
low_competence_italian['response_e3_normalized'] = ''
low_competence_italian['response_e4_normalized'] = ''
low_competence_italian['response_f1_normalized'] = ''
low_competence_italian['response_f2_normalized'] = ''
low_competence_italian['response_f3_normalized'] = ''
low_competence_italian['response_f4_normalized'] = ''
low_competence_italian['response_g1_normalized'] = ''
low_competence_italian['response_g2_normalized'] = ''
low_competence_italian['response_g3_normalized'] = ''
low_competence_italian['response_g4_normalized'] = ''
low_competence_italian['response_h1_normalized'] = ''
low_competence_italian['response_h2_normalized'] = ''
low_competence_italian['response_h3_normalized'] = ''
low_competence_italian['response_h4_normalized'] = ''

for index, row in low_competence_italian.iterrows():
    rowwise_raw_scores = list()
    rowwise_raw_scores.append([row['response_a1'], row['response_a2'], row['response_a3'], row['response_a4']])
    rowwise_raw_scores.append([row['response_b1'], row['response_b2'], row['response_b3'], row['response_b4']])
    rowwise_raw_scores.append([row['response_c1'], row['response_c2'], row['response_c3'], row['response_c4']])
    rowwise_raw_scores.append([row['response_d1'], row['response_d2'], row['response_d3'], row['response_d4']])
    rowwise_raw_scores.append([row['response_e1'], row['response_e2'], row['response_e3'], row['response_e4']])
    rowwise_raw_scores.append([row['response_f1'], row['response_f2'], row['response_f3'], row['response_f4']])
    rowwise_raw_scores.append([row['response_g1'], row['response_g2'], row['response_g3'], row['response_g4']])
    rowwise_raw_scores.append([row['response_h1'], row['response_h2'], row['response_h3'], row['response_h4']])
    # Now normalize these scores (in this per-user range/variance context) and append to dataframe
    scalar = preprocessing.StandardScaler().fit(rowwise_raw_scores)
    x_scaled = scalar.transform(rowwise_raw_scores)
    low_competence_italian.loc[index, 'response_a1_normalized'] = x_scaled[0][0]
    low_competence_italian.loc[index, 'response_a2_normalized'] = x_scaled[0][1]
    low_competence_italian.loc[index, 'response_a3_normalized'] = x_scaled[0][2]
    low_competence_italian.loc[index, 'response_a4_normalized'] = x_scaled[0][3]
    low_competence_italian.loc[index, 'response_b1_normalized'] = x_scaled[1][0]
    low_competence_italian.loc[index, 'response_b2_normalized'] = x_scaled[1][1]
    low_competence_italian.loc[index, 'response_b3_normalized'] = x_scaled[1][2]
    low_competence_italian.loc[index, 'response_b4_normalized'] = x_scaled[1][3]
    low_competence_italian.loc[index, 'response_c1_normalized'] = x_scaled[2][0]
    low_competence_italian.loc[index, 'response_c2_normalized'] = x_scaled[2][1]
    low_competence_italian.loc[index, 'response_c3_normalized'] = x_scaled[2][2]
    low_competence_italian.loc[index, 'response_c4_normalized'] = x_scaled[2][3]
    low_competence_italian.loc[index, 'response_d1_normalized'] = x_scaled[3][0]
    low_competence_italian.loc[index, 'response_d2_normalized'] = x_scaled[3][1]
    low_competence_italian.loc[index, 'response_d3_normalized'] = x_scaled[3][2]
    low_competence_italian.loc[index, 'response_d4_normalized'] = x_scaled[3][3]
    low_competence_italian.loc[index, 'response_e1_normalized'] = x_scaled[4][0]
    low_competence_italian.loc[index, 'response_e2_normalized'] = x_scaled[4][1]
    low_competence_italian.loc[index, 'response_e3_normalized'] = x_scaled[4][2]
    low_competence_italian.loc[index, 'response_e4_normalized'] = x_scaled[4][3]
    low_competence_italian.loc[index, 'response_f1_normalized'] = x_scaled[5][0]
    low_competence_italian.loc[index, 'response_f2_normalized'] = x_scaled[5][1]
    low_competence_italian.loc[index, 'response_f3_normalized'] = x_scaled[5][2]
    low_competence_italian.loc[index, 'response_f4_normalized'] = x_scaled[5][3]
    low_competence_italian.loc[index, 'response_g1_normalized'] = x_scaled[6][0]
    low_competence_italian.loc[index, 'response_g2_normalized'] = x_scaled[6][1]
    low_competence_italian.loc[index, 'response_g3_normalized'] = x_scaled[6][2]
    low_competence_italian.loc[index, 'response_g4_normalized'] = x_scaled[6][3]
    low_competence_italian.loc[index, 'response_h1_normalized'] = x_scaled[7][0]
    low_competence_italian.loc[index, 'response_h2_normalized'] = x_scaled[7][1]
    low_competence_italian.loc[index, 'response_h3_normalized'] = x_scaled[7][2]
    low_competence_italian.loc[index, 'response_h4_normalized'] = x_scaled[7][3]

low_competence_italian['avg_a_normalized'] = low_competence_italian[['response_a1_normalized', 'response_a2_normalized', 'response_a3_normalized', 'response_a4_normalized']].mean(axis=1)
low_competence_italian['avg_b_normalized'] = low_competence_italian[['response_b1_normalized', 'response_b2_normalized', 'response_b3_normalized', 'response_b4_normalized']].mean(axis=1)
low_competence_italian['avg_c_normalized'] = low_competence_italian[['response_c1_normalized', 'response_c2_normalized', 'response_c3_normalized', 'response_c4_normalized']].mean(axis=1)
low_competence_italian['avg_d_normalized'] = low_competence_italian[['response_d1_normalized', 'response_d2_normalized', 'response_d3_normalized', 'response_d4_normalized']].mean(axis=1)
low_competence_italian['avg_e_normalized'] = low_competence_italian[['response_e1_normalized', 'response_e2_normalized', 'response_e3_normalized', 'response_e4_normalized']].mean(axis=1)
low_competence_italian['avg_f_normalized'] = low_competence_italian[['response_f1_normalized', 'response_f2_normalized', 'response_f3_normalized', 'response_f4_normalized']].mean(axis=1)
low_competence_italian['avg_g_normalized'] = low_competence_italian[['response_g1_normalized', 'response_g2_normalized', 'response_g3_normalized', 'response_g4_normalized']].mean(axis=1)
low_competence_italian['avg_h_normalized'] = low_competence_italian[['response_h1_normalized', 'response_h2_normalized', 'response_h3_normalized', 'response_h4_normalized']].mean(axis=1)

# print(low_competence_italian)
low_competence_italian.to_csv('./results/full_data_low_competence.csv')

# Create chart
data_frame_combined = {
    'Native': [
        ordered_data_frame["avg_a_normalized"].mean(),
        ordered_data_frame["avg_b_normalized"].mean(),
        ordered_data_frame["avg_c_normalized"].mean(),
        ordered_data_frame["avg_d_normalized"].mean(),
        ordered_data_frame["avg_e_normalized"].mean(),
        ordered_data_frame["avg_f_normalized"].mean(),
        ordered_data_frame["avg_g_normalized"].mean(),
        ordered_data_frame["avg_h_normalized"].mean()
    ],
    'High competence (C1-C2)': [
        high_competence_italian["avg_a_normalized"].mean(),
        high_competence_italian["avg_b_normalized"].mean(),
        high_competence_italian["avg_c_normalized"].mean(),
        high_competence_italian["avg_d_normalized"].mean(),
        high_competence_italian["avg_e_normalized"].mean(),
        high_competence_italian["avg_f_normalized"].mean(),
        high_competence_italian["avg_g_normalized"].mean(),
        high_competence_italian["avg_h_normalized"].mean()
    ],
    'Low competence (A1-B2)': [
        low_competence_italian["avg_a_normalized"].mean(),
        low_competence_italian["avg_b_normalized"].mean(),
        low_competence_italian["avg_c_normalized"].mean(),
        low_competence_italian["avg_d_normalized"].mean(),
        low_competence_italian["avg_e_normalized"].mean(),
        low_competence_italian["avg_f_normalized"].mean(),
        low_competence_italian["avg_g_normalized"].mean(),
        low_competence_italian["avg_h_normalized"].mean()
    ]
}

chart_data_frame = pd.DataFrame(data_frame_combined, index=labels)
ax = chart_data_frame.plot.bar(rot=0)
ax.set_ylabel('Average Group Score')
ax.set_xlabel('Condition')
ax.set_title('Average User-Normalized Scores per Condition')
plt.savefig('./results/all_normalized_by_competence_and_condition_combined.png')

# Do one-way ANOVA for each category
print('One-way ANOVAs. Going to combine High and Low Competence Italians so we can get a P statistic for the '
      'difference between native speakers and Italians. Our English control group has the least, '
      'at 66, so we will subtract 6 Italians from the high-competence group (the bigger one) '
      'to match the numbers between groups')

# Condition A
print('One-Way ANOVA for Condition A English/Italian speakers:')
english_value_list = ordered_data_frame['avg_a_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_a_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_a_normalized'].tolist()

print('Number of English native speakers: ' + str(len(english_value_list)))
print('Number of High competence English speakers: ' + str(len(high_italian_value_list)))
print('Number of Low competence English speakers: ' + str(len(low_italian_value_list)))

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition B
print('One-Way ANOVA for Condition B English/Italian speakers:')
english_value_list = ordered_data_frame['avg_b_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_b_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_b_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition C
print('One-Way ANOVA for Condition C English/Italian speakers:')
english_value_list = ordered_data_frame['avg_c_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_c_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_c_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition D
print('One-Way ANOVA for Condition D English/Italian speakers:')
english_value_list = ordered_data_frame['avg_d_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_d_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_d_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition E
print('One-Way ANOVA for Condition E English/Italian speakers:')
english_value_list = ordered_data_frame['avg_e_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_e_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_e_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition F
print('One-Way ANOVA for Condition F English/Italian speakers:')
english_value_list = ordered_data_frame['avg_f_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_f_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_f_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition G
print('One-Way ANOVA for Condition G English/Italian speakers:')
english_value_list = ordered_data_frame['avg_g_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_g_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_g_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

# Condition H
print('One-Way ANOVA for Condition H English/Italian speakers:')
english_value_list = ordered_data_frame['avg_h_normalized'].tolist()
high_italian_value_list = high_competence_italian['avg_h_normalized'].tolist()
low_italian_value_list = low_competence_italian['avg_h_normalized'].tolist()

combined_italian_value_list = low_italian_value_list[6:]
combined_italian_value_list.extend(high_italian_value_list)

one_way_anova = f_oneway(english_value_list, combined_italian_value_list)
t_test_dataframe = pd.DataFrame({'English': english_value_list, 'Italian': combined_italian_value_list})
t_test_result = ttest_ind(t_test_dataframe['English'], t_test_dataframe['Italian'])
print('t-test results:')
print('Statistic: ' + str(t_test_result.statistic) + ', P Value: ' + str(t_test_result.pvalue))
print('ANOVA results:')
print('F Statistic = ' + str(one_way_anova[0]))
print('P Value = ' + str(one_way_anova[1]))
print()

print("Done.")
