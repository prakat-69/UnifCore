from .models import User

# Core authentication services for user registration
def register_user(username, email, password):
    if User.objects.filter(username=username).exists():
        return None, "Username already exists"

    user = User.objects.create(
        username=username,
        email=email,
        password=password  # later replace with hashing
    )

    return user, None

# Core authentication services for user login
def login_user(username, password):
    try:
        user = User.objects.get(username=username)
        if user.password == password: #todo : replace with hashing
            return user, None
        else:
            return None, "Invalid password"
    except User.DoesNotExist:
        return None, "User not found"

# Core authentication services for user logout
def logout_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        # Implement logout logic
        return True, None
    except User.DoesNotExist:
        return False, "User not found"
    

# Core authentication services for user profile retrieval
def get_user_profile(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user, None
    except User.DoesNotExist:
        return None, "User not found"
    

# Core authentication services for user profile Update
def update_user_profile(user_id, username=None, email=None, password=None):
    try:
        user = User.objects.get(id=user_id)
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = password # later replace with hashing
        user.save() 
        return user, None
    
    except User.DoesNotExist:
        return None, "User not found"
   
      

# Core authentication services for user deletion
def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return True, None
    
    except User.DoesNotExist:
        return False, "User not found"
      