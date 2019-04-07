class RenameColumn < ActiveRecord::Migration[5.2]
  def change
    rename_column :posts ,:body,:image
  end
end
