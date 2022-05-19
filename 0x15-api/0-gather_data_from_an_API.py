#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request as request

    with request.urlopen("https://intranet.hbtn.io/status") as response:
        readcontent = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(readcontent)))
        print("\t- content: {}".format(readcontent))
        print("\t- utf8 content: {}".format(readcontent.decode('utf8')))
