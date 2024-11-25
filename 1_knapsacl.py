import numpy as np

def calculate_profit(weights, profits, item_index, current_capacity, profit_matrix):
    if item_index == 0 or current_capacity <= 0:
        return 0
    
    current_item = item_index - 1
    current_weight = weights[current_item]

    if current_weight > current_capacity:
        return profit_matrix[item_index - 1][current_capacity]
    
    profit_without_item = profit_matrix[current_item-1][current_capacity]
    profit_with_item = profit_matrix[current_item-1][current_capacity-current_weight] + profits[current_item]

    return max(profit_with_item, profit_without_item)

def solve_knapsack(weights, profits, capacity):
    n_items = len(weights)
    profit_matrix = np.zeros((n_items+1, capacity+1))

    for i in range(1, n_items+1):
        for j in range(capacity+1):
            profit_matrix[i][j] = calculate_profit(weights, profits, i, j, profit_matrix)
        print(profit_matrix[i])
    
    return profit_matrix, profit_matrix[n_items][capacity]

def find_items(profit_matrix, weights):
    n_items = len(weights)
    capacity = profit_matrix.shape[1] - 1
    selected_items = []
    current_capacity = capacity

    for i in range(n_items, 0, -1):
        if profit_matrix[i][current_capacity] != profit_matrix[i-1][current_capacity]:
            selected_items.append(i-1)
            current_capacity -= weights[i-1]

    return selected_items

if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [1, 2, 5, 6]
    capacity = 8

    profit_matrix, max_profit = solve_knapsack(weights, profits, capacity)

    selected_items = find_items(profit_matrix, weights)

    print(f"Maximum Profit :- {max_profit}")
    print(f"Selected items :- {selected_items}")