def _key_value_parser(args):
        """Creates a dictionary from a list of input strings.
        usage is
        user=fuhad
        user.id = 89238
        so it will create a new user with name user = fuhad
        """
        new_dict = {}
        for arg in args:
            print(f'args: {arg}')
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')# work on fixing this code such that even if there is space in the title and description declaration, it wont split it
                else:
                     try:
                        value = int(value)
                     except:
                         try:
                             value = float(value)
                         except:
                             continue
            new_dict[key] = value
        return new_dict

sample = 'User name="fuhad" state="Kwara State" description="This is a sample to test certain things" another="A_sample_with_underscore"'
print(_key_value_parser(sample))
