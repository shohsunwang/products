import os # operating system

#全部先寫成fuction
#決定這些fuction 需不需要參數(投幣孔)和reture (回傳)
#function的中心思想，只做一件事
#讀取檔案做了兩件事，先檢查檔案，在讀取檔案，不夠好需要修改。
#主要執行的程式在最下面，其他都是function，通常會把主要程式定義main ()


#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding= 'utf-8') as f:
        for line in f:
            if '商品,價格' in line: 
                continue  
            name, price = line.strip().split(',') 
            products.append([name, price])
    return products


#請使用者輸入
def user_input(products):
    while True: 
        name = input('請輸入商品名稱: ')
        if name == "q": #quit
            break
        price = input('請輸入商品價格: ') 
        products.append([name, price]) 
    print(products)
    return products   #products原本是空清單，後來加東西有改變，所以要回傳

#印出購買紀錄
def print_product(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def wirte_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:      
        f.write('商品,價格\n') 
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') 
         

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yash! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_product(products)
    wirte_file('products.csv', products)

main()