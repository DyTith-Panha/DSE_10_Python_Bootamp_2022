def multiply_values(x,y,z):
    Inter = int(x)
    String = str(y)
    Inter = int(z)
    print(f'make_list({x},"{y}",{z})')
    return x,y,z
make_list = (multiply_values(21,'hello',45))
print(list(make_list))