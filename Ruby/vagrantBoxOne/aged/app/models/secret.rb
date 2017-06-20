class Secret < ActiveRecord::Base
  belongs_to :tip
  belongs_to :user

  validates :author, :content, presence: true
end
