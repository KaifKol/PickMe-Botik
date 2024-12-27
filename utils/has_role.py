def has_role_by_id(interaction, role_id):
    return any(role.id == role_id for role in interaction.author.roles)
