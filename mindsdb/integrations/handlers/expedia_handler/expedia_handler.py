from mindsdb.utilities import log
from mindsdb.utilities.config import Config

from mindsdb_sql.parser import ast

from mindsdb.integrations.libs.api_handler import APIHandler, APITable, FuncParser
from mindsdb.integrations.utilities.sql_utils import extract_comparison_conditions
from mindsdb.integrations.utilities.date_utils import parse_utc_date

from mindsdb.integrations.libs.response import (
    HandlerStatusResponse as StatusResponse,
    HandlerResponse as Response,
    RESPONSE_TYPE
)
from mindsdb.utilities import log

class ExpediaTable(APITable):
    def select(self, query: ast.Select) -> Response:
        """Handle SELECT queries
        Args:
            query (ast.Select): select query
        Returns:
            Response
        """
        #conditions = extract_comparison_conditions(query.where)

        raise NotImplementedError
    
    def insert(self, query: ast.Insert) -> Response:
        """Handle INSERT queries
        Args:
            query (ast.Insert): insert query
        Returns:
            Response
        """
        raise NotImplementedError
    
    def get_columns(self):
        """Get columns of the table
        Returns:
            list
        """
        raise NotImplementedError

class ExpediaHandler(APIHandler):
    def __init__(self, name: str):
        super().__init__(name)
        """ constructor
        Args:
            name (str): the handler name
        """

        raise NotImplementedError


    def connect(self) -> HandlerStatusResponse:
        """ Set up any connections required by the handler
        Should return output of check_connection() method after attempting
        connection. Should switch self.is_connected.
        Returns:
            HandlerStatusResponse
        """
        raise NotImplementedError
    
    def check_connection(self) -> HandlerStatusResponse:
        """ Check connection to the handler
        Returns:
            HandlerStatusResponse
        """
        raise NotImplementedError
    
    def native_query(self, query: Any) -> HandlerResponse:
        """Receive raw query and act upon it somehow.
        Args:
            query (Any): query in native format (str for sql databases,
                dict for mongo, api's json etc)
        Returns:
            HandlerResponse
        """
        raise NotImplementedError

    def call_expedia_api(self, method_name:str = None, params:dict = None) -> DataFrame:
        """Receivery as AST (abstract syntax tree) and act upon it somehow.
        Args:
            query (ASTNode): sql query represented as AST. Can be any kind
                of query: SELECT, INSERT, DELETE, etc
        Returns:
            DataFrame
        """
        raise NotImplementedError

