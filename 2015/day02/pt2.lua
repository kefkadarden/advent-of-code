if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

local total = 0
local separator = "x"

for line in io.lines(filename) do
  local result = {}
  for match in string.gmatch(line, "[^" .. separator .. "]+") do
    table.insert(result, tonumber(match))
  end
  if #result ~= 3 then
    print("Not 3 values for lxwxh")
    break
  end

  --find 2 smallest sides
  table.sort(result)
  local s1 = result[1]
  local s2 = result[2]
  local s3 = result[3]
  local ribbon = s1 + s1 + s2 + s2
  local bow = s1 * s2 * s3
  local val = bow + ribbon
  total = total + val
end

print("Total: " .. total)
