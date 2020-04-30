import re

class Algorithm:
    def test(self, path_to_comparable, path_to_compared, unknown_args):
        pass

    def parseSettings(self, **kwargs):
        dictionary = {}
        settings = kwargs.get('settings', None)
        regex = "(.*)=(.*)"
        if settings is not None:
            for setting in settings:
                match = re.match(regex, setting)
                dictionary[match.groups()[0]] = match.groups()[1]

        return dictionary
