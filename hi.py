def hello(part):
    if part[len(part)-1] == "s":
        print(f"my {part} hurt")
    else:
        print(f"my {part} hurts")

hello(str(input("enter a body part: ")))