Rails.application.routes.draw do

  root "displayer#index"

  get "hello" => "displayer#hello"

  get "say/hello(/:name)" => "displayer#say"

  get "times" => "displayer#times"

  get "times/restart" => "displayer#restart"

end















# HTTP_VERB "<relative URL>" => "controller#method"