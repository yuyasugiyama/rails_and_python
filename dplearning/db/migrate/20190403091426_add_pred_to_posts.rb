class AddPredToPosts < ActiveRecord::Migration[5.2]
  def change
    add_column :posts, :pred, :string
  end
end
