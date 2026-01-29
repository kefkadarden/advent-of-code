if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]
local file = io.open(filename, "r")

if not file then
  print('no file opened')
  return
end

local houses = 1
local grid = {}
local x = 1
local y = 1
grid[x] = {}
grid[x][y] = 1

while true do
  local c = file:read(1)

  if c == nil then
    break
  end

  if c == "^" then
    y = y - 1
  elseif c == "<" then
    x = x - 1
  elseif c == ">" then
    x = x + 1
  elseif c == "v" then
    y = y + 1
  elseif c == "\n" then
  else
    print(string.format("bad character %s", c))
    return
  end

  if not grid[x] then
    houses = houses + 1
    grid[x] = {}
    grid[x][y] = 1
  end
  if not grid[x][y] then
    grid[x][y] = 1
    houses = houses + 1
  end
end

print("houses: " .. houses)
