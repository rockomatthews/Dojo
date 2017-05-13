class AddEmailColumnToUsers < ActiveRecord::Migration
  def change
    add_column :users, :email, :stringCopy
  end
end
