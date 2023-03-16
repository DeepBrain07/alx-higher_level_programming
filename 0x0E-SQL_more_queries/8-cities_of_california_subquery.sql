--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name FROM hbtn_0d_usa.cities WHERE hbtn_0d_usa.cities.state_id = hbtn_0d_usa.cities.id ORDER BY hbtn_0d_usa.cities.id ASC;
