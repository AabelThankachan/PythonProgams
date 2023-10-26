MyFamily=["Father","Mother","Brother","Sister","Jacky"]
print(MyFamily[2])
print(MyFamily[::-1])
if "Sister" in MyFamily:
    print("Sister is present in list")
else:
    print("Not present in list:")
MyFamily[-1]="Tiger"
print(MyFamily)
del MyFamily[-1]
print(MyFamily)
MyFamily.append("Tommy")
print(MyFamily)
