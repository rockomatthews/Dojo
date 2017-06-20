class Tip < ActiveRecord::Base
    has_many :secrets
    has_many :users, through: :owners
    
    validates :title, :description, presence: true
end
