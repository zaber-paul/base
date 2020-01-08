from __future__ import print_function

from builtins import object
from cloudmesh_base.tables import dict_printer
from cloudmesh_base.tables import print_format_dict
from cloudmesh_base.tables import array_dict_table_printer
from cloudmesh_base.tables import column_table
from cloudmesh_base.tables import row_table
from cloudmesh_base.util  import HEADING

class TestDatabase(object):
 
    data = {
        "x": {"a": 1, "b": "2"},
        "y": {"a": 3, "b": "4"},
        }
                       
    def setup(self):
        # HEADING()
        pass
        
    def teardown(self):
        # HEADING()
        pass


    def test_json(self):
        HEADING()
        print(print_format_dict(self.data, kind="json"))
        assert True
    """
    def test_yaml(self):
        HEADING()
        print(print_format_dict(self.data, kind="yaml"))
        assert True

    def test_table(self):
        HEADING()
        print(column_table(self.data))
        assert True

    def test_table1(self):
        HEADING()
        print(array_dict_table_printer(self.data))
        assert True

    def test_table2(self):
        HEADING()
        print(row_table(self.data))
        assert True
    """
    
    def test_table3(self):
        HEADING()
        print(dict_printer(self.data))
        assert True

