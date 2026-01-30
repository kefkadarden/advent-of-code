local md5 = require('md5')

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
local content = file:read("l")
local i = 1
local message
local hash_string
while true do
  message = content .. i
  print(message)
  hash_string = md5.sumhexa(message)
  if string.sub(hash_string, 1, 6) == "000000" then
    break;
  end
  i = i + 1
end
print("Message: " .. message)
print("Md5 hash: " .. hash_string)
