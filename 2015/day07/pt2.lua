if #arg == 0 then
  print('filename not passed as argument')
  return
end
local filename = arg[1]

--IDEA
-- read file for all instructions and put in var:instructions
-- while reading also put all variables in var:variables
-- what if the "instruction" is a key/value pair where the key is the "endwire"
-- and the value is the text instruction
--
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

local function pairsByKeys(t, f)
  local a = {}
  for n in pairs(t) do table.insert(a, n) end
  table.sort(a, f)
  local i = 0             -- iterator variable
  local iter = function() -- iterator function
    i = i + 1
    if a[i] == nil then
      return nil
    else
      return a[i], t[a[i]]
    end
  end
  return iter
end

local function print_wires()
  for key, val in pairsByKeys(wires) do
    print("Wire[" .. key .. "] = " .. val)
  end
end

local function print_instructions()
  for i, instr in ipairs(instructions) do
    print(string.format(
      "Instruction %d: complete=%s, operand_1=%s, operand_2=%s, operator=%s, end_wire=%s",
      i, tostring(instr.complete), tostring(instr.operand_1),
      tostring(instr.operand_2), tostring(instr.operator), tostring(instr.end_wire)))
  end
end

local function trim(s)
  if (s == nil) then return nil end
  return string.gsub(s, "^%s*(.-)%s*$", "%1")
end

local function bitwise_not(n)
  if (n == nil) then
    return n
  end
  return (~n) & 0xFFFF
end

local function save_instruction(operand1, operand2, operator, endwire)
  table.insert(instructions,
    { complete = false, operand_1 = operand1, operand_2 = operand2, operator = operator, end_wire = endwire })
end

local function check_instructions_complete()
  for _, record in pairs(instructions) do
    if record.complete == false then
      return true
    end
  end

  return false
end

local function perform_calc(instruction)
  local operator = instruction["operator"]
  local w1 = instruction["operand_1"]
  local w2 = instruction["operand_2"]
  local endWire = instruction["end_wire"]
  local v1, v2

  if (tonumber(w1)) then
    v1 = w1
  else
    v1 = wires[w1]
  end
  if (tonumber(w2)) then
    v2 = w2
  else
    v2 = wires[w2]
  end

  --If v1 doesn't have value then skip because it always needs a value to calc expression
  if (v1 == nil) then
    return
  end

  --If instruction requires both wires and one doesn't have value then skip
  if (operator ~= nil and (operator == "AND" or
        operator == "OR" or
        operator == "LSHIFT" or
        operator == "RSHIFT")) then
    if (v1 == nil and v2 == nil) then
      return
    end
  end

  if (operator == nil) then
    wires[endWire] = v1
  elseif operator == "AND" and tonumber(v1) ~= nil and tonumber(v2) ~= nil then
    wires[endWire] = tonumber(v1) & tonumber(v2)
  elseif operator == "OR" and tonumber(v1) ~= nil and tonumber(v2) ~= nil then
    wires[endWire] = tonumber(v1) | tonumber(v2)
  elseif operator == "NOT" and tonumber(v1) ~= nil then
    wires[endWire] = bitwise_not(tonumber(v1))
  elseif operator == "LSHIFT" and tonumber(v1) ~= nil and tonumber(v2) ~= nil then
    wires[endWire] = tonumber(v1) << tonumber(v2)
  elseif operator == "RSHIFT" and tonumber(v1) ~= nil and tonumber(v2) ~= nil then
    wires[endWire] = tonumber(v1) >> tonumber(v2)
  else
    return
  end

  instruction["complete"] = true
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

  --print(tostring(w1) .. "    " .. tostring(w2) .. " : " .. tostring(startIndex) .. "," .. tostring(endIndex))
  if startIndex ~= nil and endIndex ~= nil then
    endWire = trim(w1:sub(endIndex + 1))
    w1 = trim(w1:sub(1, startIndex))
    if (tonumber(w1)) then
      wires[endWire] = w1
    else
      wires[endWire] = nil
    end
  else
    startIndex, endIndex = w2:find(" -> ", 1, true)
    endWire = trim(w2:sub(endIndex + 1))
    w2 = trim(w2:sub(1, startIndex))
    if (tonumber(w2)) then
    else
      wires[endWire] = nil
    end
  end

  if (endWire == "b") then
    w1 = 3176
    wires[endWire] = 3176
  end
  --print("end wire: \"" .. tostring(endWire) .. "\"")
  --print("w1: " .. tostring(w1) .. " - " .. tostring(v1))
  --print("w2: " .. tostring(w2) .. " - " .. tostring(v2))

  local operator = operator_find(line)
  --print("Operator: " .. tostring(operator))
  save_instruction(w1, w2, operator, endWire)
end

while check_instructions_complete() do
  for _, instruction in ipairs(instructions) do
    if (not instruction["complete"]) then
      perform_calc(instruction)
    end
  end
end


-- print_wires()
print("A: " .. wires["a"])
-- print_instructions()
