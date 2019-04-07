class PostsController < ApplicationController
require "open3"
  def index
    @posts = Post.all.order(created_at: 'desc')
  end
  
  def show
    @post = Post.find(params[:id])
  end
  
  def new
  end
  
  def create
    #save
    @post = Post.new(post_params)
    label_predict
    @post.save!
    #redirect
    redirect_to action: 'show'
  end

  def destroy
     @post = Post.find(params[:id])
     @post.remove_image!
     @post.save!
     @post.destroy
     redirect_to posts_path
  end
  private
    def post_params
       params.require(:post).permit(:title,:image)
    end
    def label_predict #pythonによるラベル予測(適切なパスに変更)
       file = "/home/y-sugiyama/rails/dplearning/public"+@post.image.to_s
       o,e,s = Open3.capture3("python /home/y-sugiyama/rails/image_predict.py #{file}")
       @post.pred = o
    end
end
