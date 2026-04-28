if #arg == 0 then
  print('filename not passed as argument')
  return
end

local filename = arg[1]

local function trim(s)
  if (s == nil) then return nil end
  return string.gsub(s, "^%s*(.-)%s*$", "%1")
end

local stotal = 0
local mtotal = 0
for line in io.lines(filename) do
  local scnt = 0
  local mcnt = 0

  scnt = #line

  local newline
  line = trim(line)

  newline = string.gsub(line, "^\"(.-)\"$", "%1")
  newline = string.gsub(newline, "\\\\", "\\")
  newline = string.gsub(newline, "\\x[0123456789abcdef][0123456789abcdef]", "A") --Just some random letter to count
  newline = string.gsub(newline, "\\\"", "\"")
  mcnt = #newline

  stotal = stotal + scnt
  mtotal = mtotal + mcnt
  print("line: " .. line .. " newline: " .. newline .. " scnt: " .. scnt .. " mcnt: " .. mcnt)
end

print(stotal - mtotal)
