#!/usr/bin/python3
def discovr():
    for name in dir(hidden_4):
        if not (name[0] == '_' and name[1] == '_'):
            print(name)


if __name__ == "__main__":
    import hidden_4
    discovr()
