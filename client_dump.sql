-- MSSQL Database Backup

CREATE TABLE Clients (
  Id INT PRIMARY KEY,
  Name NVARCHAR(100),
  Email NVARCHAR(100),
  Password NVARCHAR(100)
);

INSERT INTO Clients (Id, Name, Email, Password) VALUES
(1, 'John Doe', 'john.doe@defensecorp.com', 'Summer2024!'),
(2, 'Alice Carter', 'alice.c@contractorhub.net', 'alice1234'),
(3, 'Bobby J.', 'b.johnson@securebuilds.org', 'MyDogSpot!');

-- Confidential Notes


-- FLAG{client_data_exfiltrated_from_sql_dump}
