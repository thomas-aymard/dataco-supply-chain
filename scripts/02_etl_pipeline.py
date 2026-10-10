import pandas as pd
import sqlite3

print("1. Chargement des données brutes...")
# L'encodage latin1 est requis pour ce dataset spécifique
df_raw = pd.read_csv('data/raw/DataCoSupplyChainDataset.csv', encoding='latin1')

print("2. Nettoyage et sélection des colonnes...")
df_raw.rename(columns={
    'Customer Id': 'Customer_Id',
    'Customer City': 'Customer_City',
    'Customer Country': 'Customer_Country',
    'Customer Segment': 'Customer_Segment',
    'Order Id': 'Order_Id',
    'order date (DateOrders)': 'Order_Date',
    'shipping date (DateOrders)': 'Shipping_Date',
    'Shipping Mode': 'Shipping_Mode',
    'Order Status': 'Order_Status',
    'Late_delivery_risk': 'Late_Delivery_Risk'
}, inplace=True)

# Création des tables normalisées (en supprimant les doublons)
customers = df_raw[['Customer_Id', 'Customer_City', 'Customer_Country', 'Customer_Segment']].drop_duplicates()
orders = df_raw[['Order_Id', 'Customer_Id', 'Order_Date', 'Shipping_Date', 'Shipping_Mode', 'Order_Status', 'Late_Delivery_Risk']].drop_duplicates()

print("3. Connexion à la base SQLite et injection...")
# SQLite va créer le fichier supply_chain.db tout seul
conn = sqlite3.connect('data/processed/supply_chain.db')

customers.to_sql('Customers', conn, if_exists='replace', index=False)
orders.to_sql('Orders', conn, if_exists='replace', index=False)

conn.close()
print("Succès ! L'ETL est terminé et la base de données est prête.")