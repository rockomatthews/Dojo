class BankAccount
attr_accessor :account_number, :checking_balance, :savings_balance, :deposit_money
attr_reader :bank_account
@@bank_accounts = 0

    def initialize(account_number, checking_balance, savings_balance)
        @account_number = account_number
        @checking_balance = checking_balance
        @savings_balance = savings_balance
        @@bank_accounts += 1
        @interest_rate = 0.01
    end
    
    def return_number
        puts "here's your account number: #{@account_number}"
    end
    
    def return_checking
        puts "available: #{@checking_balance}"
    end
    
    def return_savings
        puts "available: #{@savings_balance}"
    end

    def deposit(account_type, amount)
        if account_type == "checking"
            @checking_balance += amount
        else
            @savings_balance += amount
        end 
    end
    
    def total
        puts "your total is #{@checking_balance + @savings_balance}"    
    end
    
    def number_of_bank_accounts
        @@bank_accounts
    end
    
    def account_information
        puts "account number: #{@account_number}\nChecking: #{@checking_balance}\nSavings: #{@savings_balance}\nInterest Rate: #{@interest_rate}\nTotal: #{self.total}"
    end
    
end

the_account = BankAccount.new(10.times.map { rand(1..9) }.join.to_i, 1000, 40000)

puts the_account.return_number
puts the_account.return_checking
puts the_account.return_savings
the_account.deposit("checking", 300)
the_account.deposit("savings", 10000)
puts the_account.return_checking
puts the_account.return_savings
puts the_account.total
puts the_account.number_of_bank_accounts
puts the_account.account_information