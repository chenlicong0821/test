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

test2={code = 200, msg = 'no data', data = {}}
for k,v in pairs(test2) do
print(k,v)
end

local a1 = 0
local a2 = nil
local a3 = {}
local a4=''

if a1 then
    print('a')
else
    print('not a')
end
if a2 then
    print('a')
else
    print('not a')
end
if a3 then
    print('a')
else
    print('not a')
end
if a4 then
    print('a')
else
    print('not a')
end
