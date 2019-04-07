Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts
  root 'posts#index'
  get '/posts',to: 'posts#show'
  post '/posts/create', to: 'posts#create'
  post "posts/:id/update", to: "posts#update", as: 'update'
end
