if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

local instructions = {}
local wires = {}

local function operator_find(line)
  local operators = { "AND", "OR", "NOT", "LSHIFT", "RSHIFT" }
  for _, op in ipairs(operators) do
    if line:find(op) then
      return op
    end
  end

  return nil
end

local function print_wires()
  table.sort(wires)
  for key, val in pairs(wires) do
    print("Wire[" .. key .. "] = " .. val)
  end
end

local function trim(s)
  if (s == nil) then return nil end
  return string.gsub(s, "^%s*(.-)%s*$", "%1")
end

local function bitwise_not(n)
  return (~n) & 0xFFFF
end

local function save_instruction(operand1, operand2, operator, endwire)
  table.insert(instructions,
    { complete = false, operand_1 = operand1, operand_2 = operand2, operator = operator, end_wire = endwire })
end

local function perform_calc(instruction)
  local operator = instruction["operator"]
  local w1 = instruction["operand_1"]
  local w2 = instruction["operand_2"]
  local endWire = instruction["end_wire"]

  if (operator == nil) then
    wires[endWire] = w1
  elseif (operator == "AND") then
    wires[endWire] = tonumber(v1) & tonumber(v2)
  elseif (operator == "OR") then
    wires[endWire] = tonumber(v1) | tonumber(v2)
  elseif (operator == "NOT") then
    wires[endWire] = bitwise_not(tonumber(v1))
  elseif (operator == "LSHIFT") then
    wires[endWire] = tonumber(v1) << tonumber(v2)
  elseif (operator == "RSHIFT") then
    wires[endWire] = tonumber(v1) >> tonumber(v2)
  end
end

for line in io.lines(filename) do
  local w1, w2
  local v1, v2
  --Get available operators
  local operands = line:gmatch("([^AND|OR|LSHIFT|RSHIFT|NOT]+)")
  w1 = trim(operands(1))
  w2 = trim(operands(2))

  local startIndex, endIndex
  if w1 ~= nil then
    startIndex, endIndex = w1:find(" -> ", 1, true)
  end

  print(tostring(w1) .. "    " .. tostring(w2) .. " : " .. tostring(startIndex) .. "," .. tostring(endIndex))
  local endWire
  if startIndex ~= nil and endIndex ~= nil then
    endWire = trim(w1:sub(endIndex + 1))
    w1 = trim(w1:sub(1, startIndex))
    if tonumber(w1) then v1 = w1 else v1 = wires[w1] end
  else
    startIndex, endIndex = w2:find(" -> ", 1, true)
    endWire = trim(w2:sub(endIndex + 1))
    w2 = trim(w2:sub(1, startIndex))
    v1 = wires[w1]
    if tonumber(w2) then v2 = w2 else v2 = wires[w2] end
    print(v2)
  end

  print("end wire: \"" .. tostring(endWire) .. "\"")
  print("w1: " .. tostring(w1) .. " - " .. tostring(v1))
  print("w2: " .. tostring(w2) .. " - " .. tostring(v2))

  local operator = operator_find(line)
  print("Operator: " .. tostring(operator))
  save_instruction(w1, w2, operator, endWire)


  if (operator == nil) then
    wires[endWire] = w1
  elseif (operator == "AND") then
    wires[endWire] = tonumber(v1) & tonumber(v2)
  elseif (operator == "OR") then
    wires[endWire] = tonumber(v1) | tonumber(v2)
  elseif (operator == "NOT") then
    wires[endWire] = bitwise_not(tonumber(v1))
  elseif (operator == "LSHIFT") then
    wires[endWire] = tonumber(v1) << tonumber(v2)
  elseif (operator == "RSHIFT") then
    wires[endWire] = tonumber(v1) >> tonumber(v2)
  end
end

while true do
  for _, instruction in ipairs(instructions) do
    if (perform_calc(instruction)) then
      instruction["complete"] = true
    end
  end
end

print_wires()
