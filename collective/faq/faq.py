from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getMultiAdapter

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from collective.faq import MessageFactory as _


# Interface class; used to define content-type schema.

class IFAQ(form.Schema, IImageScaleTraversable):
    """
    A Frequently asked question
    """

    answer = RichText(
            title=_(u"Answer"),
            description=_(u"The answer"),
            required=False,
            )

    source = schema.TextLine(
            title=_(u"Source"),
            description=_(u"Source of the question. Can be a hyperlink or just 'twitter' etc."),
            required=False,
            )

    questioner = schema.TextLine(
            title=_(u"Questioner"),
            description=_(u"Name, age, area"),
            required=False,
            )

    email = schema.TextLine(
            title=_(u"Questioner email"),
            description=_(u"Questioner email, to notify the questioner when the question is answered."),
            required=False,
            )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class FAQ(Item):
    grok.implements(IFAQ)

    # Add your class methods and properties here
    pass


class View(grok.View):
    """ sample view class """

    grok.context(IFAQ)
    grok.require('zope2.View')

    def answered(self):
        plone = getMultiAdapter((self.context, self.request), name="plone")
        effective = self.context.effective_date
        if effective:
            return plone.toLocalizedTime(self.context.effective_date)
        else:
            return u''

    def answerer(self):
        creators = self.context.creators
        if creators:
            return creators[0]
        return u''

    def asked(self):
        plone = getMultiAdapter((self.context, self.request), name="plone")
        return plone.toLocalizedTime(self.context.created())
