def calc(op: str, val1, val2=None):
    if not isinstance(val1, (int, float)):
        raise ValueError(f'Invalid operator "{val1}"')
    if val2 is not None and not isinstance(val2, (int, float)):
        raise ValueError(f'Invalid operator "{val2}"')
    if op not in ["+", "-", "*", "/", "%", "^", "add", "sub", "mul", "div", "mod", "pow"]:
        raise ValueError(f'Invalid operator "{op}"')

    if op in ("+", "add"):
        if val2 is None:
            return val1
        return val1 + val2
    elif op in ("-", "sub"):
        if val2 is None:
            return -val1
        return val1 - val2
    elif op in ("*", "mul"):
        return val1 * val2
    elif op in ("/", "div"):
        try:
            return val1 / val2
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")
    elif op in ("%", "mod"):
        try:
            return val1 % val2
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")
    elif op in ("^", "pow"):
        return val1 ** val2

def eval(lst: list):
    if not isinstance(lst, list) or len(lst) > 3 or len(lst) <= 1:
        return f'Failed to evaluate "{lst}"'

    elif len(lst) < 3:
        if lst[0] in ("+", "sum"):
            return lst[1]
        elif lst[0] in ("-", "sub"):
            if isinstance(lst[1], list):
                return -eval(lst[1])
            return (-lst[1])

    elif isinstance(lst[1], list):
        lst[1] = eval(lst[1])
        return eval(lst)
    elif isinstance(lst[2], list):
        lst[2] = eval(lst[2])
        return eval(lst)

    else:
        return calc(lst[0], lst[1], lst[2])

def struct(raw_lst: list):
    error_msg = "Failed to structure"
    if not isinstance(raw_lst, list) or len(raw_lst) == 1:
        return f'{error_msg} "{raw_lst}"' 

    elif len(raw_lst) == 2:
        if isinstance(raw_lst[0], (int, float)):
            raw_lst[0], raw_lst[1] = raw_lst[1], raw_lst[0]
            return raw_lst
        else:
            return raw_lst

    elif len(raw_lst) == 3 and isinstance(raw_lst[-2], str):
        raw_lst[0], raw_lst[1] = raw_lst[1], raw_lst[0]
        return raw_lst
    
    elif any(op in ["^", "pow"] for op in raw_lst):
        for i in range(len(raw_lst)):
            if raw_lst[i] in ["^", "pow"]:
                sublst = raw_lst[i-1:i+2]
                sublst[0], sublst[1] = sublst[1], sublst[0]
                raw_lst[i-1:i+2] = [sublst]
                break
        return struct(raw_lst)

    elif any(op in ["*", "/", "%", "mul", "div", "mod"] for op in raw_lst):
        for i in range(len(raw_lst)):
            if raw_lst[i] in ["*", "/", "%", "mul", "div", "mod"]:
                sublst = raw_lst[i-1:i+2]
                sublst[0], sublst[1] = sublst[1], sublst[0]
                raw_lst[i-1:i+2] = [sublst]
                break
        return struct(raw_lst)

    elif any(op in ["+", "-", "add", "sub"] for op in raw_lst):
        if isinstance(raw_lst[-1], str):
            return f'{error_msg} "{raw_lst}"'
        else:
            for i in range(len(raw_lst)):
                if raw_lst[i] in ["+", "-", "add", "sub"]:
                    sublst = raw_lst[i-1:i+2]
                    sublst[0], sublst[1] = sublst[1], sublst[0]
                    raw_lst[i-1:i+2] = [sublst]
                    break
            return struct(raw_lst)
    
    else:
        for i in range(len(raw_lst)):
            if isinstance(raw_lst[i], str):
                sublst = raw_lst[i-1:i+2]
                sublst[0], sublst[1] = sublst[1], sublst[0]
                raw_lst[i-1:i+2] = [sublst]
                break
        return struct(raw_lst)

def get_next(line: str, start: int):
    if line == "" or start >= len(line):
        return "End of string"
        
    output = ""
    if line[start].isdigit():
        for i in line[start:]:
            if not i.isdigit() and i != ".":
                break
            else:
                output += i

        if any(char == "." for char in output):
            return float(output)
        else:
            return int(output)
    
    elif line[start].isalpha():
        for i in line[start:]:
            if not i.isalpha():
                break
            else:
                output += i
        return output

    else:
        output = line[start]
        return output

def parse(raw_str: str):
    raw_str = raw_str.replace(" ", "")
    parsed_lst = []
    start = 0

    while start < len(raw_str):
        parenth = []
        item = get_next(raw_str, start)
        start += len(str(item))
        if item == "(":
            subitem = ""
            while subitem != ")":
                subitem = get_next(raw_str, start)
                start += len(str(subitem))
                parenth.append(subitem)
            
            if "(" in parenth:
                st_idx = parenth.index("(")
                nd_idx = parenth.index(")")
                inside_par = parenth[st_idx + 1:nd_idx]
                subpar = " ".join(map(str, inside_par))
                subpar = parse(subpar)
                parenth[st_idx:nd_idx+1] = [subpar]
            if parenth[-1] == ")":
                parenth.pop()
            
            item = struct(parenth)

        elif item == ")":
            break

        parsed_lst.append(item)
        
    return struct(parsed_lst)

def pre_parse(pre_string: str):
    opening_par = 0
    closing_par = 0
    for i in pre_string:
        if i == "(":
            opening_par += 1
        elif i == ")":
            closing_par += 1

    if opening_par != closing_par:
        raise Exception("Not matching parenthesis")

def coordinate(original: str):
    try:
        pre_parse(original)
        original = parse(original)
        original = eval(original)
        return original

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to the advanced calculator")
    print("You can press 'q' or type 'quit' to exit")
    while True:
        original = input("Enter your calculation: ")
        if original.lower() in ["q", "quit"]:
            break
        result = coordinate(original)
        print("Result:",result)
