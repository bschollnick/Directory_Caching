"""
Unified Archive support for Python.

Adds:

* ZIP / CBZ
* RAR / CBR

Targeted intent is for Directory Caching, but usable in other venues.

The current model, is expanded from:

http://stackoverflow.com/questions/13044562/
    python-mechanism-to-identify-compressed-file-type-and-uncompress

Which gave me the spark on a sensible manner to deal with signature and managing via
the object model.

More File signatures are avialable here:

    http://www.garykessler.net/library/file_sigs.html

Mimetype Information from here:

    http://www.freeformatter.com/mime-types-list.html


Suggested workflow:

1) Initialize by using id_cfile_by_signature
    a) This will a populated class (with filename), archive listings will not be populated

2) Use the get_listings function to get the listings for the compressed file
3) Use extract_mem_file to pull out individual files, as needed.

Next steps:

Create a batch extractor?  To increase efficiency?

Zip, RAR are supported, what other formats might be useful?
    ?? PDF? - Technically not a archive, and will need to use Ghostscript to create
                extracted pages
"""

#		Gallery Comic Support
#
#
import exceptions
import os
import os.path

class NotInitializedYet(exceptions.Exception):
    """
    d
    """
    pass

class CompressedFile(object):
    """
d
    """
    file_type = None
    mime_type = None
    proper_extension = None
    filename = None
    listings = []
    handler = None
    magic = None

    def __init__(self, filename):
        """
d
        """
        # f is an open file or file like object, or filename
        self.filename = os.path.realpath(filename)
#        self.accessor = self.open()
        self.fhandle = None
        self.identified = None
        self.listings = []

    @classmethod
    def is_magic(cls, data):
        """
d
        """
        return data.startswith(cls.magic)

    def open(self):
        """
d
        """
# pylint: disable=E1102
        if self.handler == None:
            raise NotInitializedYet
        else:
            return self.handler(self.filename)
#    magic = None
# pylint: enable=E1102

    def get_listings(self):
        """
d
        """
        if self.handler == None:
            raise NotInitializedYet
        else:
            self.listings = []
# pylint: disable=E1102
            with self.handler(self.filename, 'r') as cfile:
# pylint: enable=E1102
                for afn in cfile.namelist():
                    if not (afn.startswith("__MACOSX") or os.path.split(afn)[1] == ""):
                        self.listings.append(afn)
                return True
            return False

    def extract_mem_file(self, filename):
        """
d
        """
# pylint: disable=E1102
        if self.handler == None:
            raise NotInitializedYet
        else:
            with self.handler(self.filename, 'r') as cfile:
                return cfile.read(filename)
# pylint: enable=E1102



class ZIPFile(CompressedFile):
    """
d
    """
    import zipfile
    magic = '\x50\x4b\x03\x04'
    file_type = ['zip', 'cbz']
    mime_type = 'compressed/zip'
    handler = zipfile.ZipFile



class RarFile(CompressedFile):
    """
d
    """
    import rarfile
    rarfile.PATH_SEP = '/'
    magic = '\x52\x61\x72\x21\x1a\x07'

    file_type = ['rar', 'cbr']
    mime_type = 'application/x-rar-compressed'
    handler = rarfile.RarFile


ARCHIVE_CLASSES = [ZIPFile, RarFile]  # BZ2File, GZFile,

# factory function to create a suitable instance for accessing files
def id_cfile_by_sig(filename):
    """
d
    """
    with file(filename, 'rb') as cfile:
        start_of_file = cfile.read(128)
        cfile.seek(0)
        for cls in ARCHIVE_CLASSES:
            if cls.is_magic(start_of_file):
                return cls(filename)
        return None


#filename='test.zip'
#cf = get_compressed_file(filename)
#if cf is not None:
#    print filename, 'is a', cf.mime_type, 'file'
#    print cf.accessor
