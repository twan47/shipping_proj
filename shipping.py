weight = 24

#ground shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20.00
elif weight > 10:
    cost_ground = weight * 4.75 + 20.00