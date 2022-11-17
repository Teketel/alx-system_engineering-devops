#!/usr/bin/env ruby
require 'set'

result = ARGV[0].scan(/(from:((?<from>\w+)|(?<from>\+1\d{10,10}))).+(\[to:((?<to>\w+)|(?<to>\+1\d{10,10}))).+(\[flags:(?<flags>\S+)\])/)
filtered = result[0].reject{|item| item.nil? || item == '' || item.to_s.empty?}
puts filtered.join(',')
