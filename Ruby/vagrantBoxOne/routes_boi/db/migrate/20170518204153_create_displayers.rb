class CreateDisplayers < ActiveRecord::Migration
  def change
    create_table :displayers do |t|

      t.timestamps null: false
    end
  end
end
