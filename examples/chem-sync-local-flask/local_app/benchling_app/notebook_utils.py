from benchling_sdk.apps.framework import App
from pathlib import Path
from benchling_sdk.models import CustomEntity
#from benchling_sdk.services.v2.stable.custom_entity_service import CustomEntityService
from benchling_sdk.services.v2.stable.entry_service import EntryService



def process_notebook(app: App, notebook_name: str)-> None: # , destination_path: Path) -> None:
    """
    Generates a client from an existing App object, and uses this to connect to benchling.
    With the name of a notebook finds its id and maybe goes though it?
    """
    #Create a new custom entity service
    
    entry_cust_serv = EntryService(client=app.benchling._client)
    #Get the entity proper through the custom entity service
    notebook_ent = entry_cust_serv.list_entries(name = notebook_name)
    
    #get the noebook ID
    
    notebook_id = notebook_ent.id

    # Do stuff with notebook
