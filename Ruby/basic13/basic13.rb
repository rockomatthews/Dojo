def countupto(num)
    for i in (1..num)
        puts i
    end
end

countupto(255)


def count_up_to_odd(num)
    for i in (1..num)
        if i % 2 != 0
        puts i
        end        
    end
end

count_up_to_odd(255)


def count_and_sum(num)
    sum = 0
    for i in (1..num)
        puts "the number is: #{i} and the sum is: #{sum += i}"
    end
end

count_and_sum(255)


def loop_thru_array(array)
    for i in array
        puts i
    end
end

loop_thru_array([1,3,5,7,9,13])


def max_in_array(array)
    puts array.max
end

max_in_array([1,4,2,3,8,-1])


def array_avg(array)
    sum = 0
    for i in array
        sum += i
    end
    puts sum / array.length
end

array_avg([20,40,60,10,50])

def array_with_odds(num)
    y = []
    for i in (1..num)
        if i % 2 != 0
            y << i
        end
    end
    print y
end

array_with_odds(255)


def larger_than_y(array, num)
    counter = 0
    for i in array
        if i > num
            counter += 1
        end
    end
    puts counter
end

larger_than_y([1,3,5,7,9,20], 6)


def square_values(array)
    new_array = []
    for i in array
        new_array << (i * i)
    end
    print new_array
end

square_values([3, 5, 6, 8])


def delete_negatives(array)
    new_array = array.map { |x| (x < 0 ? x = 0 : x) }
end

print delete_negatives([1,2,5,6,3,-4,8,-6])


def min_max_avg_hash(array)
    stat_hash = {
        'min': nil,
        'max': nil,
        'avg': nil
    }
    stat_hash[:min] = array.min
    stat_hash[:max] = array.max
    stat_hash[:avg] = array.reduce(:+) / array.length.to_f
    print stat_hash
end

min_max_avg_hash([1, 5, 10, -2])


def shift_left(array)
    array.shift
    array << 0
    print array
end

shift_left([1, 5, 10, 7, -2])


def negs_to_dojo(array)
    array.map! {|x| (x < 0 ? x = 'dojo' : x)}
end

print negs_to_dojo([-1, -3, 2])