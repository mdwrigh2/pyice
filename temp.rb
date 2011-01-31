#!/usr/bin/env ruby
file = File.new("p1/ice9.y")
arr = []

file.each do |line|
  input = line.split(" ")
  if input[0] == "%token"
    if input[1].start_with? "TK"
      arr << "    '"+input[1].split("_")[1]+"'"
    else
      arr << "    '"+input[2].split("_")[1]+"'"
    end
  end
end
puts arr.join(",\n")
