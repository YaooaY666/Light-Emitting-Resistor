import datetime 
import math

def f(D):
    output = []
    sorted_data = sorted(data, key = lambda x: x['Running_time'])
    fastest_time = sorted_data[0]['Running_time']
    slowest_time = sorted_data[-1]['Running_time']
    max_diff = slowest_time - fastest_time
    for team in data:
        acc_score = math.ceil(team['Accuracy'] / 10)
        run_percentage = math.floor(((team['Running_time']-fastest_time)/max_diff)*100)
        run_score = round((100-run_percentage)/10) if (run_percentage >= 0 and run_percentage <= 10) else (math.floor((99-run_percentage)/10) if
                                                                                                          run_percentage >= 11 and run_percentage <= 79 else 1)
        score = run_score + acc_score
        time = team['Submission_time'].strftime("%Y-%m-%d %H:%M:%S")
        dt = datetime.datetime(2024, 4, 23, 10, 15)
        output.append({
            'Team_name': team['Team_name'],
            'Score': score,
            'Submission time': time
        })

    output = sorted(output, key = lambda x: (-x['Score'], x['Submission time'])) # sort in decreasing order by score, but break ties with submission time
    return output
