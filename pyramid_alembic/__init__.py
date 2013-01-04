from pyramid.scaffolds import PyramidTemplate

class AlembicProjectTemplate(PyramidTemplate):
    _template_dir = 'alembic'
    summary = 'Pyramid Alembic/SQLAlchemy project using url dispatch and Mako templates'
