import os #載入作業系統模組operating system

def read_file(filename):
	products = [] #不管有沒有舊檔案都要先開空清單
	#先讀取原有檔案
	with open(filename, 'r') as f:
		for line in f:
			if 'product,price' in line: #拿掉標題
				continue #不進行後續動作，跳到下一迴
			name, price = line.strip().split(',') 
			products.append([name, price])
	return products #回傳資料到products清單


#再讓使用者輸入更多
def user_input(products): #讓function知道products是什麼
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
	return products #再傳出來一次 

#印出所有購買紀錄
def print_products(products): #讓function知道products是什麼
	for p in products:
		print(p[0], 'price is', p[1])

#寫入檔案
#with open('products.csv', 'w', encoding = 'utf-8') as f:
#若標題為中文會產生亂碼，使用編碼encoding來解決
def write_file(filename, products): #兩個參數
	with open(filename, 'w') as f:
		f.write('product,price\n') #加入標題
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查此檔案存不存在，只用一次不需要寫成function
		print('there is an old file')
		products = read_file(filename) #如果檔案在就把csv檔傳到filename
	else:
		print('no old file')

	products = user_input(products) #把products傳進去function，再把結果存進去products
	print_products(products)
	write_file('products.csv', products)

main()
