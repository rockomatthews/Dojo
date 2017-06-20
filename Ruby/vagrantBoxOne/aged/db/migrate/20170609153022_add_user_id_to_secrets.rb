class AddUserIdToSecrets < ActiveRecord::Migration
  def change
    add_column :secrets, :user_id, :int
  end
end
