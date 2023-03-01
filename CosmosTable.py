pip install azure-data-tables

from azure.data.tables import TableClient



# create client from connection string 
#bash script az storage account show-connection-string -g MyResourceGroup -n MyStorageAccount 
#create resourcegroup and storage account from Azure 

from azure.data.tables import TableServiceClient
connection_string = "DefaultEndpointsProtocol=https;AccountName=<my_account_name>;AccountKey=<my_account_key>;EndpointSuffix=core.windows.net"
service = TableServiceClient.from_connection_string(conn_str=connection_string)

from azure.data.tables import TableServiceClient
table_service_client = TableServiceClient.from_connection_string(conn_str="<connection_string>")
table_name = "myTable"
table_client = table_service_client.create_table(table_name=table_name)

PRODUCT_ID = u'001234'
PRODUCT_NAME = u'RedMarker'

my_entity = {
    u'PartitionKey': PRODUCT_NAME,
    u'RowKey': PRODUCT_ID,
    u'Stock': 15,
    u'Price': 9.99,
    u'Comments': u"great product",
    u'OnSale': True,
    u'ReducedPrice': 7.99,
    u'PurchaseDate': datetime(1973, 10, 4),
    u'BinaryRepresentation': b'product_name'
}

table_service_client = TableServiceClient.from_connection_string(conn_str="<connection_string>")
table_client = table_service_client.get_table_client(table_name="myTable")

entity = table_client.create_entity(entity=my_entity)
