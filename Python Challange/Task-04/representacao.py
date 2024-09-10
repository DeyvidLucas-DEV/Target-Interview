import json

json_data = '''
{
  "states": {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53
  }
}
'''

state_revenues = json.loads(json_data)["states"]

total_revenue = sum(state_revenues.values())

percentages = {state: (revenue / total_revenue) * 100 for state, revenue in state_revenues.items()}

print(f"Total: R${total_revenue:.2f}")
for state, percentage in percentages.items():
    print(f"Porcentagem de representacao do {state}: {percentage:.2f}%")
