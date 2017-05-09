# Create an array with the following values: 3,5,1,2,7,9,8,13,25,32. Print the sum of all numbers in the array. Also have the function return an array that only include numbers that are greater than 10 (e.g. when you pass the array above, it should return an array with the values of 13,25,32 - hint: use reject or find_all method)
array = [3,5,1,2,7,9,8,13,25,32]
puts array.reduce(:+)
puts array.reject { |num| num <= 10 }

puts "***************************************************************"
# Create an array with the following values: John, KB, Oliver, Cory, Matthew, Christopher. Shuffle the array and print the name of each person. Have the program also return an array with names that are longer than 5 characters.
guysrray = ['John', 'KB', 'Oliver', 'Cory', 'Matthew', 'Christopher']
guysrray.shuffle!.each {|name| puts name}
puts guysrray.reject {|name| name.length < 5}

puts "***************************************************************"
# Create an array that contains all 26 letters in the alphabet (this array must have 26 values). Shuffle the array and display the last letter of the array. Have it also display the first letter of the array. If the first letter in the array is a vowel, have it display a message.
alphabet = ('a'..'z').to_a.shuffle!
puts alphabet
if alphabet[0] =~ /[aeiou]/ 
    puts "How lucky... A vowel."
else
    puts alphabet[0]
end
puts alphabet[-1]

puts "***************************************************************"
# Generate an array with 10 random numbers between 55-100.
array = []
5.times do |x|
array << rand(55..100)
end
puts array

puts "***************************************************************"
# Generate an array with 10 random numbers between 55-100 and have it be sorted (showing the smallest number in the beginning). Display all the numbers in the array. Next, display the minimum value in the array as well as the maximum value
array = []
10.times do |x|
array << rand(55..100)
end
puts array.sort!
puts array[0]
puts array[-1]

puts "***************************************************************"
# Create a random string that is 5 characters long (hint: (65+rand(26)).chr returns a random character)
string = ""
5.times do 
    string << (65+rand(26)).chr
end
puts string

puts "***************************************************************"
# Generate an array with 10 random strings that are each 5 characters long
array = []
10.times do 
    string = ""
    5.times do 
        string << (65+rand(26)).chr
    end
    array << string
end
puts array
