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
XS = 1
YS = 1
XR = 1
YR = 1
local turn = "S"
grid[1] = {}
grid[1][1] = 1

local function takeTurn(driver, direction)
  local x, y
  if (driver == "S") then
    x = XS
    y = YS
  elseif driver == "R" then
    x = XR
    y = YR
  end
  --print(string.format("Driver: %s, Direction: %s, x=%i, y=%i", driver, direction, x, y))
  if direction == "^" then
    y = y - 1
  elseif direction == "<" then
    x = x - 1
  elseif direction == ">" then
    x = x + 1
  elseif direction == "v" then
    y = y + 1
  else
    print('bad character ' .. direction)
    return nil
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

  if driver == "S" then
    XS = x
    YS = y
    driver = "R"
  elseif driver == "R" then
    XR = x
    YR = y
    driver = "S"
  end

  return driver
end

while true do
  local c = file:read(1)

  if c == nil or c == "\n" then
    break
  end

  if c == "^" or c == "v" or c == "<" or c == ">" then
    turn = takeTurn(turn, c)
  else
    print(string.format("bad character %s", c))
    return
  end
end

print("houses: " .. houses)
