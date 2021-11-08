user_name=input("ENTER YOUR NAME:");
user_password=input("ENTER YOUR PASSWORD:");
password_length=len(user_password);
hidden_password='*' * password_length;
print(f"HI {user_name},Your password is {hidden_password}")
