from allauth.account.forms import SetPasswordForm, SignupForm
from base.models import Profile
from base.roles import Operator, Saas
from rolepermissions.permissions import grant_permission
from rolepermissions.roles import assign_role


class CustomSignupForm(SignupForm):
    def save(self, request):
        # request data must have
        # username # password # password1 # first_name # last_name # email # permissions

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # set user data
        user.first_name = request.data.get("first_name", "")
        user.last_name = request.data.get("last_name", "")
        user.email = request.data.get("email", None)
        user.save()

        # save profile
        profile = Profile(user=user)
        profile.save()

        # Add your own processing here.
        assign_role(user, Operator)
        assign_role(user, Saas)
        for perm in request.data.get("permissions", []):
            grant_permission(user, perm)

        # You must return the original result.
        return user


class CustomSetPasswordForm(SetPasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(CustomSetPasswordForm, self).save()

        # Add your own processing here.
