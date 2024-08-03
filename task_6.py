def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, info in items_sorted:
        if info['cost'] <= budget:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    
    return selected_items, total_calories

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)

def dynamic_programming(items, budget):
    # Ініціалізація таблиці динамічного програмування
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [item]
    
    return selected_items[budget], dp[budget]

# Приклад використання
budget = 100
selected_items, total_calories = dynamic_programming(items, budget)
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)
