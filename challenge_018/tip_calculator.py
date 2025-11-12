def calculate_tips(meal_price, custom_tip):
    price_str = meal_price.replace('$', '').replace(' ', '')
    price = float(price_str)

    custom_percent_str = custom_tip.replace('%', '')
    custom_percent = float(custom_percent_str) / 100

    tip_15 = price * 0.15
    tip_20 = price * 0.20
    tip_custom = price * custom_percent

    result_15 = f"${tip_15:.2f}"
    result_20 = f"${tip_20:.2f}"
    result_custom = f"${tip_custom:.2f}"

    return [result_15, result_20, result_custom]


print(calculate_tips("$10.00", "25%"))
print(calculate_tips("$89.67", "26%"))
print(calculate_tips("$19.85", "9%"))