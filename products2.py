#讀取檔案
products = []
with open('products2.csv', 'r', encoding= 'utf-8') as f:
    for line in f:
        if '商品,價格' in line: #不要有檔頭名稱
            continue  #略過這行，跳下一行直接做。 break 是直接跳出迴圈。 通常都在迴圈的高處
        name, price = line.strip().split(',') #切割完直接存入name,price。如果有三行，就需要輸入3個
        # name = s[0]   #切割完的結果直接成為清單
        # price = s[1]
        products.append([name, price])
print(products)
#請使用者輸入
while True: 
    name = input('請輸入商品名稱: ')
    if name == "q": #quit
        break
    price = input('請輸入商品價格: ') 
    products.append([name, price]) 
print(products)
#印出購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])
#寫入檔案
with open('products2.csv', 'w', encoding = 'utf-8') as f:      
    f.write('商品,價格\n') 
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') 
     