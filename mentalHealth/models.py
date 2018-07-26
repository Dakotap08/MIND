from google.appengine.ext import ndb

class Meme(ndb.Model):
    first_line = ndb.StringProperty(required=True)
    second_line = ndb.StringProperty(required=False)
    pic_type =  ndb.StringProperty(required=True)

    #other functions should go above handler so the handler can make a reference to this code
    def get_meme_url(self):
        if meme_type == 'Baby Cardi':
            url = 'http://ugc.vivalastatic.com/gen/constrain/600/600/80/2018/01/09/13/8i/hx/phx023zxoo2qbwe.jpg'
        elif meme_type == 'Spongebob':
            url = 'https://amp.thisisinsider.com/images/5abb9eb43216742a008b45cc-1334-667.jpg'
        elif meme_type == 'Beyonce':
            url = 'https://www.alux.com/wp-content/uploads/2015/06/0f787710-e311-45da-8fd0-4042963b0858.jpg'
        elif meme_type == 'Gavin':
            url = 'https://i.kym-cdn.com/entries/icons/original/000/020/941/gavin_mastodon.jpg'
        return url
