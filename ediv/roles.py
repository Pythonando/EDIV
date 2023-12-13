from rolepermissions.roles import AbstractUserRole

class Client(AbstractUserRole):
    available_permissions = {
        'submit_video_for_edit': True,
        'view_video_status': True
    }

class Editor(AbstractUserRole):
    available_permissions = {
        'edit_video': True,
        'view_video_for_editing': True,
        'make_budget': True
    }