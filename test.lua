local test1 = {[1] = 1 , [2] = 2 , [3] = 3 , [4] = 4 ,[5] = 5}
print(#test1)

for i,v in ipairs(test1) do
print(i,v)
end
print("hello")
--ipairs遍历table所有元素
for k,v in pairs(test1) do
print(k,v)
end

print("world")
local test1 = {[1] = 1 , [3] = 3 , [4] = 4 , [6] = 6 ,[2] = 2}
print(#test1)
for i,v in ipairs(test1) do
print(i,v)
end
print("hello")
--ipairs遍历table所有元素
for k,v in pairs(test1) do
print(k,v)
end
