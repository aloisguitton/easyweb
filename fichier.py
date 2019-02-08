class fichier(object):

    def __init__(self):
        self.html=""

    def ecrire(self, html):
        self.html += html + "\n"

    def remplacer(self, html):
        self.html = html

    def reset(self):
        self.html=""

    def ret_html(self):
        return self.html