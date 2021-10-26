
from django.contrib import admin
from django.urls import path
from crud.views import index
from crud.views import SignupView, LoginView, product, productDelete, productUpdate, productInsert
from crud.views.email_verification import verifyCode , sendOtp
from crud.middlewares.can_not_access_after_login import cantAccessAfterLogin
from crud.views.reset_password import ResetPassword , PasswordResetVerification , verifyResetPasswordCode

urlpatterns = [
     path('', index.index , name='index'),

     path('login/', cantAccessAfterLogin(LoginView.as_view()) , name='login'),
     path('logout/', index.logout , name='logout'),

     path('send-otp', cantAccessAfterLogin(sendOtp) , name='sendotp'),
     path('verify', cantAccessAfterLogin(verifyCode) , name='verify'),
     path('signup/', cantAccessAfterLogin(SignupView.as_view()) , name='signup'),

     path('reset-password' , ResetPassword.as_view() , name = 'reset-password'),
     path('reset-password-verification' , PasswordResetVerification.as_view() , name = 'reset-password-verification'),
     path('verify-reset-password-code' , verifyResetPasswordCode , name='verify-reset-password-code'),

     path('view-product', product.ProductView.as_view() , name='product-view'),

     path('product-update/<int:product_id>' , productUpdate.ProductUpdateView.as_view() , name = 'product-update'),
     path('product-delete/<int:product_id>' , productDelete.ProductDeleteView.as_view() , name = 'product-delete'),

     path('product-insert' , productInsert.ProductInsertView.as_view() , name = 'product-insert'),
]
