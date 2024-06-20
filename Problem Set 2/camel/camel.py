

def main():
    varName = input("camelCase: ")
    print("snake_case:", snake_case(varName))

def snake_case(var):
    var_name = ""
    for i in var:
        if i.isupper():
            var_name += '_' + i.lower()
        else:
            var_name += i
    return var_name.lstrip('_')
main()

