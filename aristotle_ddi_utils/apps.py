from aristotle_mdr.apps import AristotleExtensionBaseConfig

class AristotleDDIConfig(AristotleExtensionBaseConfig):
    name = 'aristotle_ddi_utils'
    verbose_name = "Aristotle DDI downloader"
    description = "Provides downloads for a number of different content types in the <a href='http://www.ddialliance.org'>DDI 3.2 XML format</a>."