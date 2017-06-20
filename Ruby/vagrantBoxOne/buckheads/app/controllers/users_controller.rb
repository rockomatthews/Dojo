class UsersController < ApplicationController
  skip_before_action :require_login, only: [:new, :create]
  before_action :require_correct_user, only: [:edit, :show, :update, :destroy]
    
  def new
    redirect_to "/sessions/new"
  end

  def show
    @user = User.includes(:wallet).find_by_id(params[:id])
  end

  def edit
  end

  def create
  @user = User.new user_params
    if @user.save
      session[:user_id] = @user.id
      redirect_to "/users/#{@user.id}"
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to "/sessions/new"
    end
  end

  private
    def require_correct_user
      if current_user != User.find(params[:id])
        redirect_to "/users/#{session[:user_id]}"
      end
    end

    def user_params
      params.require(:user).permit(:email, :motto, :bio, :first_name, :last_name, :password, :password_confirmation)
    end

end
