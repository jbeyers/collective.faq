from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

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


# View class
# The view will automatically use a similarly named template in
# faq_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IFAQ)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
