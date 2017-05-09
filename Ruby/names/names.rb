a = {first_name: "Michael", last_name: "Choi"}
b = {first_name: "John", last_name: "Doe"}
c = {first_name: "Jane", last_name: "Doe"}
d = {first_name: "James", last_name: "Smith"}
e = {first_name: "Jennifer", last_name: "Smith"}
names = [a, b, c, d, e]

def name_stats names
    puts "There are #{names.length} first names here!"
    names.each {|name| puts "Your name is #{name[:first_name]} #{name[:last_name]}"}
end

name_stats(names)