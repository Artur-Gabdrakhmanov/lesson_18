from voluptuous import Schema, PREVENT_EXTRA

register_single_user = Schema(
    {
        'id': int,
        'token': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

create_single_user = Schema(
    {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_single_user = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str,
    },
    extra=PREVENT_EXTRA,
    required=True
)
