import os
import matplotlib.pyplot as plt
from itertools import islice
from dotenv import load_dotenv

print("This script will chart the time taken for each participant and the average score of their acceptability "
      "measure for Condition D, then plot it on a scatter plot.")

# Assigning env variables based on ENV variables
load_dotenv(dotenv_path='.env')

# Load all .env variables
results_location = str(os.environ.get('RESULTS_LOCATION'))
results_location_italian = str(os.environ.get('RESULTS_LOCATION_ITALIAN'))

results = {}
user_md5_buffer = ''
judgements = 0
likert_score = 0
likert_avg = 0
counter = 0
total_time_exam = 0
value_line = ''

print('Condition D (English):')
with open(results_location) as f:
    for line in f:
        if 'https://ryanchausse.com/aubrie_masters/images/conversation_pics/' in line:
            timestamp_and_md5 = line[:43:1]
            user_md5 = timestamp_and_md5.split(',')[1]
            if not user_md5_buffer:
                user_md5_buffer = user_md5
            if user_md5 != user_md5_buffer:
                total_time_exam = 0
                counter = 0
                likert_score = 0
            value_line = ''.join(islice(f, 1))
            likert_score_location = int(value_line.find(',NULL,NULL,'))
            if 'cond=d' in line:
                if ',practice,' not in line:
                    # Find user's likert score, add to cond D likert judgements
                    if int(likert_score_location) != -1:
                        likert_point_location = 11 + likert_score_location
                    else:
                        likert_score_location = int(value_line.find(',NULL,'))
                        likert_point_location = 6 + likert_score_location
                    likert_score += int(value_line[likert_point_location])
                    counter += 1
                    if counter == 4:
                        likert_avg = likert_score / counter
                        total_time_exam += int(value_line.split(',')[-1])
                        results[user_md5_buffer] = {"likert_avg": float(likert_avg), "total_time": total_time_exam}
            user_md5_buffer = user_md5
            total_time_exam += int(value_line.split(',')[-1])
f.close()

print(results)

likert_scores = []
total_times = []
for score_time in results.values():
    likert_scores.append(score_time['likert_avg'])
    # Gives minutes to complete the test
    total_times.append(score_time['total_time']/1000/60)

# Plot on scatter plot
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain')
ax.set_ylabel('Time to complete test (mins)')
ax.set_xlabel('Average score')
ax.set_title('Total time to take exam vs. average Likert score per user for Condition D')
plt.scatter(likert_scores, total_times)
plt.savefig('./results/likert_vs_time_taken_cond_d.png')
