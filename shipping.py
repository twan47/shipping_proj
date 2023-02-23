weight = 24

#ground shipping
if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00
print(cost_ground)

#ground shipping premium
cost_ground_premium = 125
print(cost_ground_premium)

#drone shipping
if weight <= 2:
    drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
    drone_shipping = weight * 9.00
elif weight > 6 and weight <= 10:
    drone_shipping = weight * 12.00
else:
    drone_shipping = weight * 14.25
print(drone_shipping)