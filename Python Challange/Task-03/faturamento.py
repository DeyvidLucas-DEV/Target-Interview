import json

json_data = '''
{
  "daily_revenue": [
    {"day": 1, "amount": 500},
    {"day": 2, "amount": 700},
    {"day": 3, "amount": 0},
    {"day": 4, "amount": 800},
    {"day": 5, "amount": 600},
    {"day": 6, "amount": 0},
    {"day": 7, "amount": 700},
    {"day": 8, "amount": 0},
    {"day": 9, "amount": 0},
    {"day": 10, "amount": 900}
  ]
}
'''

data = json.loads(json_data)

amounts = [item['amount'] for item in data['daily_revenue'] if item['amount'] > 0]

min_amount = min(amounts)
max_amount = max(amounts)

monthly_average = sum(amounts) / len(amounts)

days_above_average = sum(1 for amount in amounts if amount > monthly_average)

print(f"Minimum revenue amount: R${min_amount:.2f}")
print(f"Maximum revenue amount: R${max_amount:.2f}")
print(f"Number of days with revenue above monthly average: {days_above_average}")
