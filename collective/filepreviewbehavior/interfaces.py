from zope.interface import Interface

class IPreviewAware( Interface ):
    """ marker interface , Behavior for enabling Products.ARFilePreview support for dexterity
        content types
    """

class IPreviewable( Interface ):
    """
    support html preview for like file content types
    """
    
    def hasPreview( ):
        """
        Has the preview
        """
    
    def setPreview( preview):
        """
        Sets the preview
        """
    
    def getPreview( ):
        """
        Get the preview
        """
   




