orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]

special = []
for order in orders:
    if order not in special:
        special.append(order)

stats = [(product, orders.count(product)) for product in special]

best_product = ""
best_count = 0
for procut, count in stats:
    if count > best_count:
        best_product, best_count = best_product, count

last_three = orders [: -4 : -1]

print("უნიკალური:", special)
print("სიხშირე:", stats)
print(f"ყველაზე პოპულარული: {best_product} ({best_count}-ჯერ)")
print("ბოლო 3 შეკვეთა:", last_three)
