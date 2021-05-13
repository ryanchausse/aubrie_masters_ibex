import pandas as pd, os, time, base64, pysftp, glob, datetime, pathlib
import matplotlib.pyplot as plt
from sklearn import preprocessing
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
print(ordered_data_frame)

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
print(ordered_data_frame_italian)

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


# # Create raw chart
# english_value_list = list(ratings.values())[::-1]
# italian_value_list = list(ratings_italian.values())[::-1]
# labels = [1, 2, 3, 4, 5, 6, 7]
# data_frame_combined = pd.DataFrame({'English': english_value_list, 'Italian': italian_value_list}, index=labels)
# ax = data_frame_combined.plot.bar(rot=0)
# ax.set_ylabel('Frequency')
# ax.set_xlabel('Responses (unnatural to perfectly natural)')
# ax.set_title('Likert Scores for Condition G')
# plt.ylim([0, 210])
# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars
# rects_english = ax.bar(x - width/2, english_value_list, width, label='English')
# rects_italian = ax.bar(x + width/2, italian_value_list, width, label='Italian')
# ax.bar_label(rects_english, padding=1, color='blue')
# ax.bar_label(rects_italian, padding=1, color='red')
# plt.savefig('./results/condition_g_combined.png')


print("Done.")
