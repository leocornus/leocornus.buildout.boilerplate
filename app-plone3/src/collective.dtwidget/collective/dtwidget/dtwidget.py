from zope.app.form.browser.textwidgets import DatetimeWidget
from zope.app.pagetemplate import ViewPageTemplateFile
from DateTime import DateTime
from zope.app.datetimeutils import parseDatetimetz
from zope.app.form.interfaces import WidgetInputError

class dtwidget(DatetimeWidget):
    
    __call__ = ViewPageTemplateFile('dtwidget.pt')
    
    tag = u'input'
    cssClass = u''
    extra = u''
    _missing = u''

    def evil(self):
        """Allows us to break back into the normal structure so the templates stolen from skin layers still work.  Very evil."""
        from zope.app.component.hooks import getSite; return getSite()  
    
    def getDT(self):
        from Products.ATContentTypes.utils import dt2DT
        try:
            return dt2DT(self._getFormValue())
        except AttributeError:
            return self._missing
    
    def _toFieldValue(self, input):
            if input == self._missing:
                return self.context.missing_value
            else:
                try:
                    DT = DateTime(input)
                except:
                    raise WidgetInputError("Invalid date",input)
                from Products.ATContentTypes.utils import DT2dt
                return DT2dt(DT)
        