if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

local passcount = {}
for line in io.lines(filename) do
  local i, prev, found
  passcount[line] = 0
  --check for 3 or more vowels
  local vowels = string.gsub(line, "[^aeiou]", "")
  print(vowels)
  local count = #vowels
  if (count >= 3) then
    passcount[line] = passcount[line] + 1
  else
    goto continue
  end
  --check for double letter
  i = 1
  prev = ""
  found = false
  while i <= #line do
    local c = string.sub(line, i, i)
    if prev == c then
      found = true
      break;
    end
    prev = c
    i = i + 1
  end

  if found == true then
    passcount[line] = passcount[line] + 1
  end
  --doesnt contain ab, cd, pq, xy
  if string.find(line, "ab") then
    goto continue
  elseif string.find(line, "cd") then
    goto continue
  elseif string.find(line, "pq") then
    goto continue
  elseif string.find(line, "xy") then
    goto continue
  else
    passcount[line] = passcount[line] + 1
  end
  ::continue::
  print(line .. " has " .. passcount[line])
end

local foundcount = 0
for _, count in pairs(passcount) do
  if count == 3 then
    foundcount = foundcount + 1
  end
end

print(foundcount)
