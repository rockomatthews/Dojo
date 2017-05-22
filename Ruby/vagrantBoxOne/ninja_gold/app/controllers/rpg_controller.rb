class RpgController < ApplicationController

    def index
        session[:gold] ||= 0
        session[:activities] ||= []

        @gold = session[:gold]
        @activities = session[:activities]
    end
    
    def new
        if params[:building] == 'Farm'
            gold = rand(10..20)
        elsif params[:building] == 'Cave'
            gold = rand(5..10)
        elsif params[:building] == 'House'
            gold = rand(2..5)
        elsif params[:building] == 'Casino'
            gold = rand(-50..50)
        end
    
        current_time = Time.now

        if gold > 0
            session[:activities] << "You collected #{gold} and from the #{params[:building]}! at #{current_time.strftime('%Y/%m/%d %l:%M %P')}"
        else
            session[:activities] << "You entered the casino and lost #{gold} at the casino you sucker! at #{current_time.strftime('%Y/%m/%d %l:%M %P')}"
        end
    
        session[:gold] += gold
        redirect_to :root
    end
end
