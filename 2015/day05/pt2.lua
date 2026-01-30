if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

local passcount = {}
for line in io.lines(filename) do
  local i
  local lettercount = {}
  passcount[line] = 0
  i = 1
  while i <= #line do
    local char = string.sub(line, i, i + 2)
    local char2 = string.sub(char, 1, 2)

    if string.sub(char, 1, 1) == string.sub(char, 2, 2) and string.sub(char, 1, 1) == string.sub(char, 3, 3) then
      break;
    end
    if not lettercount[char2] then
      lettercount[char2] = 0
    end
    lettercount[char2] = lettercount[char2] + 1
    if (lettercount[char2] == 2) then
      passcount[line] = passcount[line] + 1
      break
    end
    i = i + 1
  end

  i = 1
  while i <= #line do
    local char = string.sub(line, i, i + 2)

    if string.sub(char, 1, 1) == string.sub(char, 3, 3) and string.sub(char, 2, 2) ~= string.sub(char, 1, 1) then
      passcount[line] = passcount[line] + 1
      break
    end
    i = i + 1
  end
  print(line .. " has " .. passcount[line])
end

local foundcount = 0
for _, count in pairs(passcount) do
  if count == 2 then
    foundcount = foundcount + 1
  end
end

print(foundcount)
