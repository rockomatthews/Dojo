class CreateSecrets < ActiveRecord::Migration
  def change
    create_table :secrets do |t|
      t.string :author
      t.string :content
      t.references :tip, index: true, foreign_key: true
      t.references :user, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
