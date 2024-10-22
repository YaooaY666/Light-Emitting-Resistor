For a problem solving task, this task was quite fun, and more so the challenge to make it as short as possible in terms of file size. The solution is as follows. 

Solution.
Sorting the team in running time, we take the longest and slowest running time, then subtract the slowest from the longest to obtain the max difference. We then enter a for loop for each team in the dictionary. To avoid writing out a bunch of if statements, we derived a formula to compute points awarded by accuracy, and a formula to compute points awarded by running time. 

For accuracy, we use ceil(Accuracy/10) to award the score obtained by it. To obtain the running time percentage with relation to the max difference, we use floor((running_time - fastest_time/max_diff)*100). If 0 <= percentage <= 10, we use round((100 - percentage)/10) to get the score, else if 11 <= percentage <= 79, we use floor((99 - percentage)/10) to get the score. If 80 <= percentage <= 100, the score is 1.

To obtain the total score, we add the score obtained from accuracy and score obtained from running time. We then append each team, total score, and submission time (in the given format) into the output list, then sort them by the score, breaking ties using the submission time, before returning it.
