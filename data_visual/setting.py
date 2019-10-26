# _*_ coding: utf-8 _*_

class Setting(object):
    """Object that holds configuration settings"""
    def __init__(self, source):
        object.__init__(self)
        if isinstance(source, dict):
            self.load_from_dict(source)
        elif isinstance(source, Setting):
            self.load_from_setting(source)
        else:
            raise RuntimeError(
                    "Cannot initialize Setting from %s" % (source))

    def override(self, other):
        for key, value in other._dict.items():
            if isinstance(value, Setting) and key in self._dict:
                self._dict[key].override(value) 
            else:
                self._dict[key] = other._dict[key]
        return self

    def load_from_setting(self, source):
        self.load_from_dict(source._dict)

    def load_from_dict(self, source):
        self._dict = {}
        for key in source:
            if isinstance(source[key], dict):
                self._dict[key] = Setting(source[key])
            else:
                self._dict[key] = source[key]
    
    def __getitem__(self, key):
        try:
            return self._dict[key]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __len__(self):
        return len(self._dict) 
