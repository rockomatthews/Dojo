class CreatePms < ActiveRecord::Migration
  def change
    create_table :pms do |t|
      t.text :remark
      t.references :user, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
