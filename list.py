#list are collection based data structure which is used to store multiple items in a single variable
# list properties :
#ordered
#indexed
#mutable
#duplicate allowed
a=[1,2,2.5,"karthik"]
print(type(a))
print(a)
"indexing also posible"
print(a[0])
print(a[-1])
"slicing also posible"
print(a[0:3])
print(a[ :3])     
print(a[0:])
# you can change the list
a[0]="karthik"
print(a)
a[0:2]=["karthik","python"]
print(a)    #duplicate allowed
# inserting 
print("inserting")
print(a.insert(2,"reddy"))  #insert at index 2
print(a.append("reddy"))  #insert at end


#to concat the list 
b=[4,5,6]
print(a.extend(b))  #extend the list a with b
