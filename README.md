# invinsense-backend
## Technologies used

* **[Python3](https://www.python.org/downloads/)** 
* **[Flask](flask.pocoo.org/)** 
* **[MariaDB](https://mariadb.org/download/)** 
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Installation / Usage

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).

    ```bash
    git clone https://github.com/Infopercept/invinsense-backend
    ```

* ### Dependencies

    1. Cd into your the cloned repo:

        ```bash
        cd flask-rest-api
        ```

    2. Create and get into your virtual environment:

        ```bash
        virtualenv -p python3 venv
        source venv/bin/activate
        ```


* ### Install your requirements
  
    ```bash
    $ pip install -r requirements.txt
    ```

* ### Database 

    Make sure your mariadb server is running. create your database from scripts\init.sql file
    Change database configuration from models\database.py edit host, port, user, password and database name as per the system configuration



* ### Running the Server

    On your terminal, run the server using this one simple command:

    ```bash
    $ python app.py
    ```

    You can now access the app on your local browser by using

    ```bash
    http://127.0.0.1:5000
    ```

    Or test creating bucketlists using Postman
    
    
    
    # query for creating table for visits_log (user tracking)
    CREATE TABLE `visits_log` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `no_of_visits` int NULL,
  `ip_address` varchar(255) NULL,
  `requested_url` varchar(255) NULL,
  `referer_page` varchar(255) NULL,
  `page_name` varchar(255) NULL,
  `query_string` varchar(255) NULL,
  `user_agent` varchar(255) NULL,
  `access_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `method` varchar(255) NULL,
  `username` varchar(255) NULL,
  `tool_name` varchar(255) NULL
);


    
