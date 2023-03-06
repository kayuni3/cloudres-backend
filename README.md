# Back-end Development 

After I created and deployed my website and mapped it to my custom domain name, I needed to create a visitor counter to be displayed on my site.


# Azure Cosmos DB for Table API 

The data for the visits to my site will be stored in a table in my Cosmos DB. I created the database in the Azure portal. I created a Table Client for my database so that I can managed entities within my Cosmos DB table.

# Azure Functions

I created function with a HTTP trigger and an input and output to my Cosmos DB table. This was the hardest part as the Python documentation for Azure Functions is very limited so it was a lot of playing around with different methods. I finally found the azure.data.tables SDK and was able to take code that was written in c# and basically translate it in Python. 

Azure SDKs for Python can be found here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables

# DotEnv: keeping my secrets secret

In order to keep my Azure resource credentials safe, I opted to use Dotenv in order to not have my credentials stored in my actual code. All of my credentials are stored in a .env file as a name/value pair and which is then imported into my Python file. 




