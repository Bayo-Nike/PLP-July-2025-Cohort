admins = {"Alice", "Bob"}
editors = {"Bob", "Charlie"}

# Combine both groups
all_users = admins.union(editors)
print("All users:", all_users)  # {'Alice', 'Bob', 'Charlie'}

# Who is both admin and editor?
both_roles = admins.intersection(editors)
print("Users with both roles:", both_roles)  # {'Bob'}

# Who is only admin?
admin_only = admins.difference(editors)
print("Admins only:", admin_only)  # {'Alice'}

# Who is only editor?
editor_only = editors.difference(admins)
print("Editors only:", editor_only)  # {'Charlie'}