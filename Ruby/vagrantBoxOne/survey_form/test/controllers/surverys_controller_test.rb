require 'test_helper'

class SurverysControllerTest < ActionController::TestCase
  test "should get name:string" do
    get :name:string
    assert_response :success
  end

  test "should get location:string" do
    get :location:string
    assert_response :success
  end

  test "should get favorite_language:string" do
    get :favorite_language:string
    assert_response :success
  end

  test "should get comment:string" do
    get :comment:string
    assert_response :success
  end

end
