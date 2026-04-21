import pandas as pd
import numpy as np
import os

def create_master_data():
    base_dir = r"d:\Project\Datathon\Datathon---AllForMoney-main"
    data_dir = os.path.join(base_dir, "data", "raw")
    output_dir = os.path.join(base_dir, "data")

    print("1. Đọc dữ liệu...")
    customers = pd.read_csv(os.path.join(data_dir, "customers.csv"))
    geography = pd.read_csv(os.path.join(data_dir, "geography.csv"))
    products = pd.read_csv(os.path.join(data_dir, "products.csv"))
    promotions = pd.read_csv(os.path.join(data_dir, "promotions.csv"))
    
    orders = pd.read_csv(os.path.join(data_dir, "orders.csv"))
    order_items = pd.read_csv(os.path.join(data_dir, "order_items.csv"))
    payments = pd.read_csv(os.path.join(data_dir, "payments.csv"))
    shipments = pd.read_csv(os.path.join(data_dir, "shipments.csv"))
    returns = pd.read_csv(os.path.join(data_dir, "returns.csv"))
    reviews = pd.read_csv(os.path.join(data_dir, "reviews.csv"))
    
    print("2. Xử lý dữ liệu ảo (Data Cleaning)...")
    
    # 2.1 Missing Values
    # Customers: nullable gender, age_group, acquisition_channel -> fill with 'Unknown'
    customers['gender'] = customers['gender'].fillna('Unknown')
    customers['age_group'] = customers['age_group'].fillna('Unknown')
    customers['acquisition_channel'] = customers['acquisition_channel'].fillna('Unknown')
    
    # Promotions: applicable_category -> 'All', promo_channel -> 'Unknown'
    promotions['applicable_category'] = promotions['applicable_category'].fillna('All')
    promotions['promo_channel'] = promotions['promo_channel'].fillna('Unknown')
    
    # Order items: promo_id nullable, filled with 'None' string representation
    order_items['promo_id'] = order_items['promo_id'].fillna('No Promo')
    order_items['promo_id_2'] = order_items['promo_id_2'].fillna('No Promo')
    
    # Constraints check:
    # products: cogs < price
    invalid_cogs = products[products['cogs'] >= products['price']]
    if not invalid_cogs.empty:
        print(f"Warning: Found {len(invalid_cogs)} products where cogs >= price. Adjusting cogs to be 90% of price.")
        products.loc[products['cogs'] >= products['price'], 'cogs'] = products['price'] * 0.9

    # 3. Kết nối dữ liệu (Data Joining)
    print("3. Bắt đầu ghép nối (Join) các bảng...")

    # Join Order Items (Transaction details) with Orders
    master = pd.merge(order_items, orders, on="order_id", how="left")
    
    # Join with Customers
    master = pd.merge(master, customers, on="customer_id", how="left", suffixes=('_order', '_customer'))
    
    # Join with Geography (Delivery to order.zip)
    # the column "zip" exists in orders and customers. Pandas merge with suffixes handled 'zip_order' and 'zip_customer'
    master = pd.merge(master, geography, left_on="zip_order", right_on="zip", how="left")
    master.drop(columns=['zip'], inplace=True)
    master.rename(columns={'city': 'delivery_city', 'region': 'delivery_region', 'district': 'delivery_district'}, inplace=True)

    # Join with Geography for Customer
    master = pd.merge(master, geography, left_on="zip_customer", right_on="zip", how="left")
    master.drop(columns=['zip'], inplace=True)
    master.rename(columns={'city': 'customer_city', 'region': 'customer_region', 'district': 'customer_district'}, inplace=True)
    
    # Join with Products
    master = pd.merge(master, products, on="product_id", how="left")
    
    # Join with Payments (Aggregated or directly if 1 to 1) 
    # payments represents order level information. If we join on order_items level, payment values will be duplicated per item.
    # To keep table flattened, we just merge. 
    # But wait, payments is 1:1 to orders. So it's safe to merge.
    master = pd.merge(master, payments, on="order_id", how="left")
    
    # Join with Shipments (1:0/1 to orders)
    master = pd.merge(master, shipments, on="order_id", how="left")
    
    # Join with Returns (item_level?) 
    # returns applies to product_id inside an order_id.
    # So we join on both order_id and product_id!
    master = pd.merge(master, returns, on=["order_id", "product_id"], how="left")
    
    # Join with Reviews (product_id, order_id, customer_id)
    master = pd.merge(master, reviews, on=["order_id", "product_id"], how="left", suffixes=("", "_review"))
    # The review also has customer_id, so we joined on order_id and product_id which is enough because an item in an order is unique.
    if 'customer_id_review' in master.columns:
         master.drop(columns=['customer_id_review'], inplace=True)
    
    print(f"Hoàn thành nối bảng. Master DataFrame shape: {master.shape}")
    
    output_file = os.path.join(output_dir, "master_data.csv")
    print(f"4. Xuất file: {output_file}")
    master.to_csv(output_file, index=False)
    print("Xong!")

if __name__ == '__main__':
    create_master_data()
