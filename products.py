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

with open('products.csv', 'w') as f:
	f.write('product,price\n') #加入標題
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')