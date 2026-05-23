# Final Project-Functional Calculator

# print("test running") 

def get_nums():
    #gets numbers from user

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y

def do_math(ops_dict, hist_list, my_set):
    #show operations

    print("Available operators: + - * / ^")
    op = input("Choose an operator: ")

    if op in ops_dict:
        n1, n2 = get_nums()

        #calc using lambda from the dict
        ans = ops_dict[op](n1, n2)

        # s = str(n1) + " " + op + " " + str(n2) + " = " + str(ans)
        
        # new way
        s = f"{n1} {op} {n2} = {ans}"
        print("Result:", s)

        hist_list.append(s)
        
        #just make sure it's a number before adding to the set so it doesn't crash
        if type(ans) is float or type(ans) is int:
            my_set.add(ans)
    else:
        print("wrong input!")

def add_two_lists(ops_dict):
    print("\n----Batch Addition----")
    l1 = [10, 20, 30]
    l2 = [1, 2, 3]
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")

    # Zip lists and Add them
    # ans_list = []
    # for x,y in zip(l1,l2):
    #     ans_list.append(ops_dict['+'](x,y))
    
    #Shorter Way:
    ans_list = [ops_dict['+'](x, y) for x, y in zip(l1, l2)]
    print(f"Result: {ans_list}")

def double_stuff(ops_dict):
    print("\n----Double a List----")
    user_str = input("Enter numbers with spaces: ")
    
    # map to float
    my_list = list(map(float, user_str.split()))
    
    # double using lambda and map
    res = list(map(lambda x: ops_dict['*'](x, 2), my_list))
    
    print(f"Original: {my_list}")
    print(f"Doubled: {res}")

def show_history(hist_list, my_set):
    print("\n----Calculation History----")
    
    if len(hist_list) == 0:
        print("empty.")
    else:
        # using enumerate
        for i, item in enumerate(hist_list, start=1):
            print(f"[{i}] -> {item}")
        
        print("\n----Unique Results----")
        print(my_set)
        
        print("\n----Positive Results Only----")
        # use filter to get numbers > 0
        pos_nums = list(filter(lambda num: num > 0, my_set))
        print(pos_nums)

def main():
    # dict for math using lambda
    # division has if else to avoid error
    ops_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error!! dont divide by 0",
        '^': lambda x, y: x ** y
    }

    hist_list = []          
    my_set = set() 

    print("----Functional Calculator----")

    while True: # Main loop
        print("\nMenu:")
        print("1.Standard Calc")
        print("2.Batch Addition (zip)")
        print("3.Double List (map)")
        print("4.History & filter positives (enumerate, filter)")
        print("5.Exit")
        
        c = input("\nchoice: ")

        if c == '1':
            do_math(ops_dict, hist_list, my_set)
        elif c == '2':
            add_two_lists(ops_dict)
        elif c == '3':
            double_stuff(ops_dict)
        elif c == '4':
            show_history(hist_list, my_set)
        elif c == '5':
            print("Done!")
            break
        else:
            print("Try Again")

# run the code
if __name__ == "__main__":
    main()