
file=open("/home/divyakshi/PycharmProjects/Decorators/scratch.txt",'w')
content1="Hello World"
l=["Python"]*2
file.write(content1)
file.writelines(l)
file.close()
f=open("/home/divyakshi/PycharmProjects/Decorators/scratch.txt",'r')
f.read()
f.close()
f=open("/home/divyakshi/PycharmProjects/Decorators/scratch.txt",'r')
l=f.readlines()
print(l)
f.close()
with open("/home/divyakshi/PycharmProjects/Decorators/scratch.txt","r") as f:
    print(f.readlines())
    print(f.closed)
    f.close()