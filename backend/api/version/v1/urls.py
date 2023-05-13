from django.urls import path

from api.version.v1 import views as system_views

urlpatterns = [
    # system
    path("system/user-data/", system_views.UserDataApiView.as_view(), name="user_data"),
    path("system/user-list/", system_views.UserListApiView.as_view(), name="user_list"),
    path("system/create-account/", system_views.CreateAccountApiView.as_view(), name="create_account"),
    path("system/update-account/", system_views.UpdateAccountApiView.as_view(), name="update_account"),
    path(
        "system/set-account-password/",
        system_views.SetAccountPasswordApiView.as_view(),
        name="set_account_password",
    ),
    path("system/profile/", system_views.UserProfileApiView.as_view(), name="profile"),
    path("system/profile/avatar", system_views.ProfileAvatarApiView.as_view(), name="profile_avatar"),
    path(
        "system/get-history-log/",
        system_views.GetHistoryLogApiView.as_view(),
        name="get_history_log",
    ),
]
