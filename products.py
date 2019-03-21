products = []
while True:
	name = input('please enter product name:')
	if name == 'q':
		break
	price = input('please enter product price:')
	p = []
	p.append(name)
	p.append(price)
	#p = [name, price]
	products.append(p)
	#products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is', p[1])