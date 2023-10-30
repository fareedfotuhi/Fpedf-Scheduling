# Fpedf-Scheduling
The EDF (Earliest Deadline First) algorithm is employed to globally schedule 'm' jobs at any given time, selecting jobs with the closest deadlines.
If there are fewer than 'm' jobs in the system, some cores will remain idle.
The fpEDF algorithm aims to improve the schedulability of tasks by prioritizing jobs with higher utilization.
Unlike EDF, where jobs with closer deadlines are chosen, fpEDF selects jobs with smaller normalized deadlines (normalized to their utilization).
