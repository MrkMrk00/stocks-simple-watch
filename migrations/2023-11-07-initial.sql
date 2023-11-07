CREATE TABLE `migrations` (
	name 		VARCHAR(511) NOT NULL PRIMARY KEY,
	migrated 	DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `transactions` (
	id 		SERIAL 		PRIMARY KEY,
	stock 		VARCHAR(15)	NOT NULL,
	stock_amount	DECIMAL(15, 4)	NOT NULL,
	stock_price	DECIMAL(15, 4) 	NOT NULL,
	when 		DATETIME	NOT NULL
);

CREATE INDEX `transactions_stock_name` ON `transactions` (stock);

INSERT INTO `migrations` (name) VALUES ('2023-11-07-initial.sql');
