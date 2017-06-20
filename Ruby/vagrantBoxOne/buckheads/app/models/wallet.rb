class Wallet < ActiveRecord::Base
  belongs_to :user


composed_of :price,
              :class_name => 'Money',
              :mapping => %w(price cents),
              :converter => Proc.new { |value| Money.new(value) }


end
