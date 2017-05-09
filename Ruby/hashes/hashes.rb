# .delete(key) => deletes and returns a value associated with the key

# e.g.  ruby h = {:first_name => "Coding", :last_name => "Dojo"}

# h.delete(:last_name) print h # => {:first_name => "Coding"}

# .empty? => returns true if hash contains no key-value pairs .has_key?(key) => true or false

# .has_value?(value) => true or false

hashy = { "first_name" => "coding", "last_name" => "dojo"}

# hashy.delete("first_name")

# puts hashy.empty?

puts hashy.has_key?("first_name")

puts hashy.has_value?("fart")