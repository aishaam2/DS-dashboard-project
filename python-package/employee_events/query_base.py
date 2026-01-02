# Import any dependencies needed to execute sql queries
import pandas as pd
from .sql_execution import QueryMixin


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):
    # Create a class attribute called `name`
    # set the attribute to an empty string
    name=""
    primID = "" # so we can join the tables by using thier id
    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self,id):
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
       sqlquery = f'''SELECT event_date,
        SUM(positive_events) positive_events,
        SUM(negative_events) negative_events
        FROM employee_events 
        JOIN {self.name}  
        ON employee_events.{self.primID} = {self.name}.{self.primID}
        WHERE  employee_events.{self.primID} = {id}
        GROUP BY event_date 
        ORDER BY event_date'''
       return  self.pandas_query(sqlquery)

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self,id):
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        notequery=f'''SELECT note_date, note FROM notes 
        JOIN {self.name} ON notes.{self.primID}={self.name}.{self.primID}
        where notes.{self.primID}={id}'''
        return self.pandas_query(notequery)
