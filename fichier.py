class fichier(object):

    def __init__(self):
        self.html=""

    def ecrire(self, html):
        self.html += html + "\n"

    def reset(self):
        self.html=""

    def ret_html(self):
        print(self.html)
        return self.html