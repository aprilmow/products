products = []
#先讀取原有檔案
with open('products.csv', 'r') as f:
	for line in f:
		if 'product,price' in line: #拿掉標題
			continue #不進行後續動作，跳到下一迴
		name, price = line.strip().split(',') 
		products.append([name, price])
print(products)

#再讓使用者輸入
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

#with open('products.csv', 'w', encoding = 'utf-8') as f:
#若標題為中文會產生亂碼，使用編碼encoding來解決
with open('products.csv', 'w') as f:
	f.write('product,price\n') #加入標題
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
