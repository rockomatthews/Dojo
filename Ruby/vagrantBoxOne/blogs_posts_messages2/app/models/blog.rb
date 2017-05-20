class Blog < ActiveRecord::Base
    has_many :posts
    has_many :owners
    has_many :user_posts, through: :posts, source: :user

end
