class DisplayerController < ApplicationController

    def index
        render text: "What do you want me to say?"
    end
    
    def hello
        render text: "Hello Coding Dojo"
    end

    def say
        unless params[:name]
            render text: "Saying hello"
        else
            if params[:name] == "Michael"
                redirect_to "/say/hello/joe"
            else
                render text: "Hello #{params[:name]}"
            end
        end
    end
    
    def times
        session[:count] ||= 0
        render text: "You have visited this page #{session[:count] += 1} times"
    end
    
    def restart
        reset_session
        render text: "Destroyed Session"
    end
    

end
