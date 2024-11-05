#!/usr/bin/env ruby
# Join the ARGV array into a single string, removing surrounding quotes if present
input_string = ARGV.join(' ').gsub(/^'|'$/, '')

# Regular expressions to extract from the input string
from_regex = /\[from:(.*?)\]/
to_regex = /\[to:(.*?)\]/
flags_regex = /\[flags:(.*?)\]/

# Extract the values using regex
sender = input_string.match(from_regex)[1]
receiver = input_string.match(to_regex)[1]
flags = input_string.match(flags_regex)[1]

# Output the formatted result
puts "#{sender},#{receiver},#{flags}"
