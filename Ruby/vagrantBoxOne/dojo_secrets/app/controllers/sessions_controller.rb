class SessionsController < ApplicationController
  def new
    # render login page
  end

  def create
    # log user in
      # if authentification is true
        # save user id to sesssion
        # redirect to user profile page
      # if authenticate false
        # add an error message -> flash[:errors] = ["Invalid"]
        # redirect to login page
  end
  
  def destroy
    # Log User out
    # set session[:user_id] to null
    # redirect to login page
  end
  
end
