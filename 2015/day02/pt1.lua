if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

local sqft = 0
local separator = "x"

for line in io.lines(filename) do
  print(line)
  local result = {}
  for match in string.gmatch(line, "[^" .. separator .. "]+") do
    print(match)
    table.insert(result, match)
  end
  print(table.concat(result, ":"))
  if #result ~= 3 then
    print("Not 3 values for lxwxh")
    break
  end
  local l = result[1]
  local w = result[2]
  local h = result[3]

  local val = 2 * l * w + 2 * w * h + 2 * l * h
  local smallest = 9999999999
  if (l * w < smallest) then
    smallest = l * w
  end
  if w * h < smallest then
    smallest = w * h
  end
  if l * h < smallest then
    smallest = l * h
  end
  print(val + smallest)
  sqft = sqft + val + smallest
end

print("SQFT: " .. sqft)
