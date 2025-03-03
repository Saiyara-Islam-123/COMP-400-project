plans= [([1,2], 4), ([3,2], 11)]
sorted_plans=sorted(plans,key=lambda plan:plan[1],reverse=True)


best_plan=sorted_plans[0]
best_action=best_plan[0][0]
print(best_action)