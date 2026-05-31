def get_initials(name):
    split_name = name.split(' ')
#   1. Variante
#   result = ''
#   for name in split_name:
#     result += name[0] + '.'
#   return result
    # 2. Short Variante
    return ''.join( name[0] + '.' for name in split_name)


'''
Name Initials
Given a full name as a string, return their initials.

Names to initialize are separated by a space.
Initials should be made uppercase.
Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.".

Tests:
Passed:1. get_initials("Tommy Millwood") should return "T.M.".
Passed:2. get_initials("Savanna Puddlesplash") should return "S.P.".
Passed:3. get_initials("Frances Cowell Conrad") should return "F.C.C.".
Passed:4. get_initials("Dragon") should return "D.".
Passed:5. get_initials("Dorothy Vera Clump Haverstock Norris") should return "D.V.C.H.N.".
'''
