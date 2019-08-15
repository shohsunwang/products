products = []
while True: # while loop 常用在不知道要做幾次迴圈的時機
    name = input('請輸入商品名稱: ')
    if name == "q": #quit
        break
    price = input('請輸入商品價格: ') #為什麼輸入在這邊，因為當商品輸入q時，就不再在輸入價格
    # p = []    #小清單
    # p.append(name) #裝到小清單
    # p.append(price)#裝到小清單
    # p =[name, price] #直接寫，可簡化7~9行
    products.append([name, price]) #最簡潔的寫法，直接在這創作小清單 #小清單裝到大清單
print(products)

products[0][0] #第一個[大清單的第幾節，第二個[]是小清單的第幾節

for p in products:
    print(p[0], '的價格是', p[1])

#字串可以做加和乘，不能做減和除
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc' #幾乎沒有用到這個

with open('products.txt', 'w') as f:  
    for p in products
    f.write(p[0] + ',' + p[1] + "\n")