import datetime 
import math

def f(D):
    output = []
    sorted_data = sorted(D, key = lambda x: x['Running_time'])
    fastest_time = sorted_data[0]['Running_time']
    slowest_time = sorted_data[-1]['Running_time']
    max_diff = slowest_time - fastest_time
    for team in D:
        acc_score = math.ceil(team['Accuracy'] / 10)
        run_percentage = math.floor(((team['Running_time']-fastest_time)/max_diff)*100)
        run_score = round((100-run_percentage)/10) if (run_percentage >= 0 and run_percentage <= 10) else (math.floor((99-run_percentage)/10) if
                                                                                                          run_percentage >= 11 and run_percentage <= 79 else 1)
        output.append({
            'Team_name': team['Team_name'],
            'Score': run_score + acc_score,
            'Submission_time': team['Submission_time'].strftime("%d-%m-%y %H:%M:%S")
        })

    return sorted(output, key = lambda x: (-x['Score'], x['Submission_time']))
