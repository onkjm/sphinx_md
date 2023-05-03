import os

def create_index_rst(depth=3):
    
    content = ''
    content += '\n' + 'Welcome to md_docs\'s documentation!'
    content += '\n' + '==================================='
    content += '\n' + ''
    content += '\n' + '.. toctree::'
    content += '\n' + '   :maxdepth: ' + str(depth)
    content += '\n' + ''
    
    items = sorted( os.listdir() )
    for item in items:
        if item.startswith('_') or item.startswith('.'):
            pass
        elif os.path.isdir(item):
            # item is dir and does not start with '_' nor '.'
            content += create_rst_dir(item)
            create_rst_base(parent='', dirname=item, depth=depth)
            
    content += '\n' + ''
    content += '\n' + 'Indices and tables'
    content += '\n' + '=================='
    content += '\n' + ''
    content += '\n' + '* :ref:`genindex`'
    content += '\n' + '* :ref:`modindex`'
    content += '\n' + '* :ref:`search`'
    
    f = open('index.rst', 'w')
    f.write(content)
    f.close()

def create_rst_base(parent, dirname, depth=3):
    
    content = dirname
    content += '\n' + '==========================='
    content += '\n' + ''
    content += '\n' + '.. toctree::'
    content += '\n' + '   :maxdepth: ' + str(depth)
    content += '\n' + '   :glob:'
    content += '\n' + ''
    content += '\n' + '   ' + parent + dirname + '/*'
    
    items = sorted( os.listdir(parent + dirname) )
    for item in items:
        # print(dirname, '/', item)
        if item.startswith('_') or item.startswith('.'):
            pass
        elif os.path.isdir(dirname +'/'+ item):
            # print(item, 'is dir.')
            # print('found dir:', item, ' under ', parent + dirname)
            content += create_rst_dir(item)
            create_rst_base(parent=parent+dirname+'/',
                            dirname=item,
                            depth=depth)
        elif os.path.isfile(dirname +'/'+ item):
            # print(item, 'is file.')
            pass
            
    f = open(dirname+'.rst', 'w')
    f.write(content)
    f.close()

def create_rst_dir(dirname):
    return '\n' + '   ' + dirname + ' <' + dirname + '>'