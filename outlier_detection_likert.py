import os
import matplotlib.pyplot as plt
from itertools import islice
from dotenv import load_dotenv

print("This script will detect users who answer significantly differently in terms of likert score vs. "
      "the average on the condition across multiple questions.")

# Assigning env variables based on ENV variables
load_dotenv(dotenv_path='.env')

# Load all .env variables
results_location = str(os.environ.get('RESULTS_LOCATION'))
results_location_italian = str(os.environ.get('RESULTS_LOCATION_ITALIAN'))

all_user_results = {}
user_results = {}
user_md5_buffer = ''
judgements = 0
likert_score_cond_a = 0
likert_score_cond_b = 0
likert_score_cond_c = 0
likert_score_cond_d = 0
likert_score_cond_e = 0
likert_score_cond_f = 0
likert_score_cond_g = 0
likert_score_cond_h = 0
likert_avg_a = 0
likert_avg_b = 0
likert_avg_c = 0
likert_avg_d = 0
likert_avg_e = 0
likert_avg_f = 0
likert_avg_g = 0
likert_avg_h = 0
counter_cond_a = 0
counter_cond_b = 0
counter_cond_c = 0
counter_cond_d = 0
counter_cond_e = 0
counter_cond_f = 0
counter_cond_g = 0
counter_cond_h = 0
user_likert_score_cond_a = 0
user_likert_score_cond_b = 0
user_likert_score_cond_c = 0
user_likert_score_cond_d = 0
user_likert_score_cond_e = 0
user_likert_score_cond_f = 0
user_likert_score_cond_g = 0
user_likert_score_cond_h = 0
user_likert_avg_a = 0
user_likert_avg_b = 0
user_likert_avg_c = 0
user_likert_avg_d = 0
user_likert_avg_e = 0
user_likert_avg_f = 0
user_likert_avg_g = 0
user_likert_avg_h = 0
user_counter_cond_a = 0
user_counter_cond_b = 0
user_counter_cond_c = 0
user_counter_cond_d = 0
user_counter_cond_e = 0
user_counter_cond_f = 0
user_counter_cond_g = 0
user_counter_cond_h = 0
value_line = ''

# First, get avg. likert for all conditions. Then, calculate each user's avg for each condition. Then display.
# Data structure like:
# user_results = {"md5 hash": {"cond_a": avg likert, "cond_b": avg likert...}}
# all_user_results = {"cond_a" : avg likert, "cond_b": avg_likert...}
# Display like:
# User: md5 hash
#   Condition A:
#     User's Score: avg_likert_for_user_cond_a
#     Everyone's Score: avg_likert_for_all_cond_a
#   Condition B:
#     ...


with open(results_location) as f:
    for line in f:
        if 'https://ryanchausse.com/aubrie_masters/images/conversation_pics/' in line:
            timestamp_and_md5 = line[:43:1]
            user_md5 = timestamp_and_md5.split(',')[1]
            if not user_md5_buffer:
                user_md5_buffer = user_md5
            if user_md5 != user_md5_buffer:
                user_likert_score_cond_a = 0
                user_likert_score_cond_b = 0
                user_likert_score_cond_c = 0
                user_likert_score_cond_d = 0
                user_likert_score_cond_e = 0
                user_likert_score_cond_f = 0
                user_likert_score_cond_g = 0
                user_likert_score_cond_h = 0
                user_likert_avg_a = 0
                user_likert_avg_b = 0
                user_likert_avg_c = 0
                user_likert_avg_d = 0
                user_likert_avg_e = 0
                user_likert_avg_f = 0
                user_likert_avg_g = 0
                user_likert_avg_h = 0
                user_counter_cond_a = 0
                user_counter_cond_b = 0
                user_counter_cond_c = 0
                user_counter_cond_d = 0
                user_counter_cond_e = 0
                user_counter_cond_f = 0
                user_counter_cond_g = 0
                user_counter_cond_h = 0
            value_line = ''.join(islice(f, 1))
            likert_score_location = int(value_line.find(',NULL,NULL,'))

            # Condition A
            if 'cond=a' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_a += int(value_line[likert_point_location])
                counter_cond_a += 1
                # Find user's likert score, add to user's cond A likert judgements
                user_likert_score_cond_a += int(value_line[likert_point_location])
                user_counter_cond_a += 1
                if user_counter_cond_a == 4:
                    user_likert_avg_a = user_likert_score_cond_a / user_counter_cond_a
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_a'] = user_likert_avg_a
                    else:
                        user_results[user_md5_buffer]['cond_a'] = user_likert_avg_a

            # Condition B
            if 'cond=b' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_b += int(value_line[likert_point_location])
                counter_cond_b += 1
                # Find user's likert score, add to user's cond B likert judgements
                user_likert_score_cond_b += int(value_line[likert_point_location])
                user_counter_cond_b += 1
                if user_counter_cond_b == 4:
                    user_likert_avg_b = user_likert_score_cond_b / user_counter_cond_b
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_b'] = user_likert_avg_b
                    else:
                        user_results[user_md5_buffer]['cond_b'] = user_likert_avg_b

            # Condition C
            if 'cond=c' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_c += int(value_line[likert_point_location])
                counter_cond_c += 1
                # Find user's likert score, add to user's cond C likert judgements
                user_likert_score_cond_c += int(value_line[likert_point_location])
                user_counter_cond_c += 1
                if user_counter_cond_c == 4:
                    user_likert_avg_c = user_likert_score_cond_c / user_counter_cond_c
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_c'] = user_likert_avg_c
                    else:
                        user_results[user_md5_buffer]['cond_c'] = user_likert_avg_c

            # Condition D
            if 'cond=d' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_d += int(value_line[likert_point_location])
                counter_cond_d += 1
                # Find user's likert score, add to user's cond D likert judgements
                user_likert_score_cond_d += int(value_line[likert_point_location])
                user_counter_cond_d += 1
                if user_counter_cond_d == 4:
                    user_likert_avg_d = user_likert_score_cond_d / user_counter_cond_d
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_d'] = user_likert_avg_d
                    else:
                        user_results[user_md5_buffer]['cond_d'] = user_likert_avg_d

            # Condition E
            if 'cond=e' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_e += int(value_line[likert_point_location])
                counter_cond_e += 1
                # Find user's likert score, add to user's cond E likert judgements
                user_likert_score_cond_e += int(value_line[likert_point_location])
                user_counter_cond_e += 1
                if user_counter_cond_e == 4:
                    user_likert_avg_e = user_likert_score_cond_e / user_counter_cond_e
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_e'] = user_likert_avg_e
                    else:
                        user_results[user_md5_buffer]['cond_e'] = user_likert_avg_e

            # Condition F
            if 'cond=f' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_f += int(value_line[likert_point_location])
                counter_cond_f += 1
                # Find user's likert score, add to user's cond F likert judgements
                user_likert_score_cond_f += int(value_line[likert_point_location])
                user_counter_cond_f += 1
                if user_counter_cond_f == 4:
                    user_likert_avg_f = user_likert_score_cond_f / user_counter_cond_f
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_f'] = user_likert_avg_f
                    else:
                        user_results[user_md5_buffer]['cond_f'] = user_likert_avg_f

            # Condition G
            if 'cond=g' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_g += int(value_line[likert_point_location])
                counter_cond_g += 1
                # Find user's likert score, add to user's cond G likert judgements
                user_likert_score_cond_g += int(value_line[likert_point_location])
                user_counter_cond_g += 1
                if user_counter_cond_g == 4:
                    user_likert_avg_g = user_likert_score_cond_g / user_counter_cond_g
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_g'] = user_likert_avg_g
                    else:
                        user_results[user_md5_buffer]['cond_g'] = user_likert_avg_g

            # Condition H
            if 'cond=h' in line and ',practice,' not in line:
                if int(likert_score_location) != -1:
                    likert_point_location = 11 + likert_score_location
                else:
                    likert_score_location = int(value_line.find(',NULL,'))
                    likert_point_location = 6 + likert_score_location
                # Collect scores for likert avg across users
                likert_score_cond_h += int(value_line[likert_point_location])
                counter_cond_h += 1
                # Find user's likert score, add to user's cond H likert judgements
                user_likert_score_cond_h += int(value_line[likert_point_location])
                user_counter_cond_h += 1
                if user_counter_cond_h == 4:
                    user_likert_avg_h = user_likert_score_cond_h / user_counter_cond_h
                    if user_md5_buffer not in user_results:
                        user_results[user_md5_buffer] = {}
                        user_results[user_md5_buffer]['cond_h'] = user_likert_avg_h
                    else:
                        user_results[user_md5_buffer]['cond_h'] = user_likert_avg_h

            user_md5_buffer = user_md5
f.close()

all_user_results['cond_a'] = round(likert_score_cond_a / counter_cond_a, 2)
all_user_results['cond_b'] = round(likert_score_cond_b / counter_cond_b, 2)
all_user_results['cond_c'] = round(likert_score_cond_c / counter_cond_c, 2)
all_user_results['cond_d'] = round(likert_score_cond_d / counter_cond_d, 2)
all_user_results['cond_e'] = round(likert_score_cond_e / counter_cond_e, 2)
all_user_results['cond_f'] = round(likert_score_cond_f / counter_cond_f, 2)
all_user_results['cond_g'] = round(likert_score_cond_g / counter_cond_g, 2)
all_user_results['cond_h'] = round(likert_score_cond_h / counter_cond_h, 2)


print('Average Likert scores per condition for all users: ' + str(all_user_results))
print('Average Likert scores per condition for individual users: ' + str(user_results))


def significant_difference(user_of_interest, condition):
    condition_full = 'cond_' + condition.lower()
    if abs(user_results[user_of_interest][condition_full] - all_user_results[condition_full]) > 2.5:
        print()
        print('User\'s response differs significantly from the average user response for condition ' + condition)
        print('User MD5 hash: ' + user)


for user in user_results.keys():
    # print('User result: ' + str(user_results[user]['cond_a']))
    # print('Everybody result: ' + str(all_user_results['cond_a']))
    significant_difference(user_of_interest=user, condition='A')
    significant_difference(user_of_interest=user, condition='B')
    significant_difference(user_of_interest=user, condition='C')
    significant_difference(user_of_interest=user, condition='D')
    significant_difference(user_of_interest=user, condition='E')
    significant_difference(user_of_interest=user, condition='F')
    significant_difference(user_of_interest=user, condition='G')
    significant_difference(user_of_interest=user, condition='H')
