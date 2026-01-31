if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]
local grid = {}
local rows = 999
local cols = 999

local function build_grid()
  grid = {}
  for x = 0, rows do
    grid[x] = {}
    for y = 0, cols do
      grid[x][y] = 0
    end
  end
end

local function count_lit()
  local count = 0
  for x = 0, rows do
    for y = 0, cols do
      if grid[x][y] then
        count = count + grid[x][y]
      end
    end
  end

  return count
end

build_grid()

for line in io.lines(filename) do
  local cmd = ""

  if line:match("^turn on") then
    cmd = "turn on"
    line = line:gsub("turn on ", "")
  elseif line:match("^turn off") then
    cmd = "turn off"
    line = line:gsub("turn off ", "")
  elseif line:match("^toggle") then
    cmd = "toggle"
    line = line:gsub("toggle ", "")
  else
    print("invalid command")
    break
  end
  local coords = {}
  local i = 1
  for coord in line:gmatch("([^through ]+)") do
    coords[i] = coord
    i = i + 1
  end

  local x1, y1, x2, y2
  local firstsvals = coords[1]:gmatch("([^,]+)")
  local secondvals = coords[2]:gmatch("([^,]+)")
  x1 = firstsvals(1)
  y1 = firstsvals(2)
  x2 = secondvals(1)
  y2 = secondvals(2)

  print(cmd)
  print(x1 .. "," .. y1)
  print(x2 .. "," .. y2)
  for x = x1, x2 do
    for y = y1, y2 do
      if cmd == "turn on" then
        grid[x][y] = grid[x][y] + 1
      elseif cmd == "turn off" then
        if (grid[x][y] - 1 >= 0) then
          grid[x][y] = grid[x][y] - 1
        end
      elseif cmd == "toggle" then
        grid[x][y] = grid[x][y] + 2
      end
    end
  end
end
print(count_lit())
