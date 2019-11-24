import pretty_print


def  calculate_cube (x):
	return (x*x*x)
def  calculate_square (x):
	return (x*x)


def main():
    
    result_square = calculate_square (2)
    simple_print (result_square)  
    
    result_cube = calculate_cube(4)
    pro_print (result_cube)


if __name__ == '__main__':
    main()