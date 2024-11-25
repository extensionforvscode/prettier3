# def is_safe(job, assigned_jobs):
#     return assigned_jobs[job] == -1

# def assign_jobs(current_worker, current_cost, min_cost, cost_matrix, assigned_jobs):
#     if current_worker == len(cost_matrix):
#         min_cost[0] = min(min_cost[0], current_cost)
#         return
    
#     for job in range(len(cost_matrix)):
#         if is_safe(job, assigned_jobs):
#             assigned_jobs[job] = current_worker
#             assign_jobs(current_worker+1, current_cost+cost_matrix[current_worker][job], min_cost, cost_matrix, assigned_jobs)
#             assigned_jobs[job] = -1

# def job_assignment(cost_matrix):
#     assigned_jobs = [-1]*len(cost_matrix)
#     min_cost = [1000]
#     assign_jobs(0, 0, min_cost, cost_matrix, assigned_jobs)
#     print(f"The min cost is :- {min_cost}")
#     # for i in range(len(cost_matrix)):
#     #     print(f"Job {i} - {assigned_jobs[i]}")

# if __name__ == "__main__":
#     cost_matrix = [
#         [9, 2, 7, 8],
#         [6, 4, 3, 7],
#         [5, 8, 1, 8],
#         [7, 6, 9, 4]
#     ]
#     job_assignment(cost_matrix)


def is_safe(job, assigned_jobs):
    return assigned_jobs[job] == -1

def job_assignment(current_worker, current_cost, min_cost, cost_matrix, assigned_jobs, final_assignment):
    if current_worker == len(cost_matrix):
        if current_cost < min_cost[0]:
            min_cost[0] = current_cost
            final_assignment[:] = assigned_jobs[:]
            return
        
    for job in range(len(cost_matrix)):
        if is_safe(job, assigned_jobs):
            if current_cost + cost_matrix[current_worker][job] < min_cost[0]:
                assigned_jobs[job] = current_worker
                job_assignment(current_worker+1, current_cost+cost_matrix[current_worker][job], min_cost, cost_matrix, assigned_jobs, final_assignment)
                assigned_jobs[job] = -1

def assign_jobs(cost_matrix):
    min_cost = [1000]
    assigned_jobs = [-1]*len(cost_matrix)
    final_assignment = [-1]*len(cost_matrix)
    job_assignment(0, 0, min_cost, cost_matrix, assigned_jobs, final_assignment)
    print(min_cost)
    for i in range(len(cost_matrix)):
        print(f"Job {i} - Worker {final_assignment[i]} with cost {cost_matrix[final_assignment[i]][i]}")

if __name__ == "__main__":
    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    assign_jobs(cost_matrix)