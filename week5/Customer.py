import Productcheck as pc

def buy(product, num, price):
    if pc.check(product, num) == True
        print ("YOu bought " + product + "and spent " + num*price)

    else:
        print ("Sorry! We are out of this product")


def main():
    
   buy(bread, 2, 500)
   

if __name__ == '__main__':
main()