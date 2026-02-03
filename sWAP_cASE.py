def swap_case(s):
    result = ""
    for st in s:
        if st == st.lower():
            result += st.upper()
        else:
            result += st.lower()
        
    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)