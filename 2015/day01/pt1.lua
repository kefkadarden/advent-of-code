if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]
local file = io.open(filename, "r")

if file then
  Content = file:read("*all")
  file:close()
end

TotalFloors = 0
for i = 1, #Content do
  local c = Content:sub(i, i)
  if c == "(" then
    TotalFloors = TotalFloors + 1
  end

  if c == ")" then
    TotalFloors = TotalFloors - 1
  end

  print(c .. ": " .. TotalFloors)
end

print("Total Floors: " .. tostring(TotalFloors))
