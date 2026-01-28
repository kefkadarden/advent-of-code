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

Position = 0
FloorNum = 0
for i = 1, #Content do
  local c = Content:sub(i, i)
  if c == "(" then
    FloorNum = FloorNum + 1
  end

  if c == ")" then
    FloorNum = FloorNum - 1
  end

  print(i .. " : " .. c .. " : " .. FloorNum)
  if FloorNum == -1 then
    print("Floor " .. i)
    return
  end
end
