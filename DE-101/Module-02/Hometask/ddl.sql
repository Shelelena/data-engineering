CREATE TABLE "orders"
(
 "row_id"        bigserial NOT NULL,
 "order_id"      varchar(30) NOT NULL,
 "order_date"    date NOT NULL,
 "ship_date"     date NOT NULL,
 "ship_mode"     varchar(30) NOT NULL,
 "customer_id"   varchar(30) NOT NULL,
 "customer_name" varchar(30) NOT NULL,
 "segment"       varchar(30) NOT NULL,
 "country"       varchar(30) NOT NULL,
 "city"          varchar(30) NOT NULL,
 "state"         varchar(30) NOT NULL,
 "postal_code"   int NULL,
 "region"        varchar(30) NOT NULL,
 "product_id"    varchar(30) NOT NULL,
 "category"      varchar(30) NOT NULL,
 "sub_category"  varchar(30) NOT NULL,
 "product_name"  varchar(200) NOT NULL,
 "sales"         numeric(10, 3) NOT NULL,
 "quantity"      int NOT NULL,
 "discount"      numeric(4, 3) NOT NULL,
 "profit"        numeric(10, 4) NOT NULL,
 PRIMARY KEY ( "row_id" )
);






