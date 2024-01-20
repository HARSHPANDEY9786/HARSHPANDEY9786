def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

# Example usage
candidates_list = [2, 3, 6, 7]
target_sum = 7
result_combinations = combination_sum(candidates_list, target_sum)
print(result_combinations)
