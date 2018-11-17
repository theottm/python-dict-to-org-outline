with open("result.org", "w") as f:
    f.write("")

def append_heading(h, l):
    with open("result.org", "a") as f:
        f.write(l*"*" + " " + h)
        f.write("\n")

def append_content(c):
    print("appening content")    
    with open("result.org", "a") as f:
        f.write(c)
        f.write("\n")

def dict_to_org(d, l):
    print(l)
    print(type(d))
    if isinstance(d, list):
        for v in d:
            append_heading(str(d.index(v)), l)
            dict_to_org(v, l + 1)
    if isinstance(d, dict):
        for k, v in d.items():
            print("Appening heading")
            print(k)
            append_heading(k, l)
            dict_to_org(v, l + 1)
    if isinstance(d, str):
        print("appening content")
        print(d)
        append_content(d)
