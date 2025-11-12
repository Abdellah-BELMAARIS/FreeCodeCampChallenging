def validate(email):

    if email.count('@') != 1:
        return False

    parts = email.split('@')
    local_part = parts[0]
    domain_part = parts[1]

    if len(local_part) == 0:
        return False

    if local_part[0] == '.' or local_part[-1] == '.':
        return False

    for char in local_part:
        if not (char.isalpha() or char.isdigit() or char in '._-'):
            return False

    if '..' in local_part:
        return False

    if '.' not in domain_part:
        return False

    last_dot_index = domain_part.rfind('.')

    if len(domain_part) - last_dot_index < 3:
        return False

    extension = domain_part[last_dot_index + 1:]

    if not extension.isalpha():
        return False
    if '..' in domain_part:
        return False

    return True

print(validate("a@b.cd"))
print(validate("hell.-w.rld@example.com"))
print(validate(".b@sh.rc"))
print(validate("example@test.c0"))
print(validate("freecodecamp.org"))
print(validate("develop.ment_user@c0D!NG.R.CKS"))
print(validate("hello.@wo.rld"))
print(validate("hello@world..com"))
print(validate("git@commit@push.io"))
# print(validate("obaidbelmaaris@gmail.com"))