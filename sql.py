import sqlite3
import numpy as np
import pandas as pd

connection = sqlite3.connect("rewardola1.db")
cursor = connection.cursor()



df = pd.read_csv("freq.csv")
table_info="""
CREATE TABLE IF NOT EXISTS freq(user_id int,user_name varchar(200),first_activity varchar(200),last_activity datetime,
offers_redeemed int,account_created datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('freq', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_coupon_history.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_coupon_history (coupon_id int,user_id int,store_id int,pointe int,created_at datetime,
updated_at datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_coupon_history', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_reward_history.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_reward_history (store_id int,store_admin int,reward_id int,user_id int,pointe int,
type varchar(200),added_or_removed int,created_at datetime,updated_at datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_reward_history', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_store_address.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_store_address(store_id int,is_available int,address varchar(200),mobile varchar(200),map_link varchar(200),
street_address varchar(200),unit_no varchar(200),province varchar(200),postal_code varchar(200),city varchar(200),created_at datetime,
updated_at datetime,is_active int,store_lat varchar(200),store_long varchar(200))
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_store_address', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_store_category.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_store_category(category_name varchar(200),is_active int,category_image varchar(200),
created_at datetime,updated_at datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_store_category', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_store_rewards_programe.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_store_rewards_programe(user_id int,store_id int,created_at datetime,updated_at datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_store_rewards_programe', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_stores.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_stores(store_name varchar(200),store_slogun varchar(200),category_id int,community_category int,
owner_id varchar(200),logo varchar(200),default_point int,header_image varchar(200),address varchar(200),mobile varchar(200),
map_link varchar(200),ios_link varchar(200),android_link varchar(200),working_hours varchar(200),priority varchar(200),created_at datetime,
updated_at datetime,is_deleted int,is_active int,instagram_link,facebook_link varchar(200),twitter_link varchar(200),linked_in varchar(200),
website_link varchar(200),youtube_link varchar(200),snapchat_link varchar(200),pinterest_link varchar(200),tiktok_link varchar(200),
google_reviews varchar(200),rewards_status int,coupons_status int,info_status int,contacts_status int,appointment_status int,order_status int,
store_owner_name varchar(200),store_owner_contact_no varchar(200),store_owner_email varchar(200),store_owner_display_name varchar(200),
store_owner_alternate_contact varchar(200),store_owner_alternate_name varchar(200),store_owner_alternate_email varchar(200),store_display_on_web varchar(200),
store_contact_email varchar(200),search_keys varchar(200),list_created varchar(200),brevo_list_id int ,domains_name varchar(200),
dns_name varchar(200),unable_rewardprogram varchar(200))
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_stores', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("tbl_user_store_visits.csv")
table_info="""
CREATE TABLE IF NOT EXISTS tbl_user_store_visits(user_id int,store_id int,created_at datetime)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('tbl_user_store_visits', connection, if_exists='replace', index = False)
connection.commit()



df = pd.read_csv("users.csv")
table_info="""
CREATE TABLE IF NOT EXISTS users (user_id int,notification_on int,user_name varchar(200),mobile varchar(200),
email varchar(200),user_type int,is_deleted int,created_at datetime,updated_at datetime,is_active int,via_social int,
is_admin int,default_store int,special_offer varchar(200),plat_form varchar(200),latitude varchar(200),
longitude varchar(200),location_city varchar(200),intro_video_status int,added_by int,review_count int,
review_date datetime,review_status varchar(200),update_app_count int)
"""
cursor.execute(table_info)
connection.commit()
df.to_sql('users', connection, if_exists='replace', index = False)
connection.commit()



connection.close()