a="KiShoRe"
var=a.lower()
print(var, a.lower())
print(a.upper())
if a.startswith("k"):
    print("input starts with pattern K")
else:
    print("input does not starts with pattern K")

if a.lower().startswith("k"):
     print("input starts with pattern K")
else:
    print("input does not starts with pattern K")

if a.lower().endswith("e"):
     print("input ends with pattern e")
else:
    print("input does not ends with pattern e")

var1="aa:a1:1.2"
out=var1.split(":")
print(out, out[0])


out1, out2, out3=var1.split(":")
print(out1, out2, out3)

out1, out2=var1.split(':',1)
print(out1, out2)


out1, out2=var1.rsplit(':',1)
print(out1, out2)


out=var1.replace(":", "/")
print(out)

