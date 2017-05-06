# .at or .fetch

# .delete

# .reverse

# .length

# .sort

# .slice

# .shuffle

# .join


# .insert

# values_at() -> returns an array with values specified in the param

# e.g. a = %w{cat dog bear}; puts a.values_at(1,2).join(' and ') #=> "dog and bear"

magnificent = ["great", "impressive", "grand", "worthy", "magnificent", "spectacular", "extraordinary", "perfect"]
funny = [69, "lol", "baha", "BAHAHAHAHA", "ha", "clowns", 169, "Tosh.0"]
numbers = [10, 20, 30, 40, 50, 60, 69, 80, 90, 100]

puts magnificent.at(4)
puts magnificent.fetch(7)

funny.delete(169)
puts funny[0]

puts funny.reverse

puts funny[4].reverse

numbers.length

puts magnificent.sort

magnificent.slice(4)

puts magnificent

numbers.shuffle

funny.insert(69)

puts magnificent.values_at(1, 2).join(' and ')

print funny
print magnificent
print numbers

