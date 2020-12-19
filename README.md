# Flask Firebase Chat

## 1. Setup MySQL

We will be using MySQL as our backend. Hence, let us set it up for our app.

Requirements:

1. MySQL server
2. Credentials to access the MySQL server

### Option 1 (**Recommended**)

To save time and avoid setup errors, you can use this [pre-setup VM]()

* VM login: ``kali``
* VM password: ``kali``
* MySQL username: ``user``
* MySQL password: ``password``

### Option 2 (Manual setup)

Follow the below instructions on either your local or virtual machine. Choose the appropriate option depending on your OS.

* Windows: [Tutorial guide](https://www.liquidweb.com/kb/install-mysql-windows/)
* Linux: [Tutorial guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
* Mac: [Tutorial guide](https://www.positronx.io/how-to-install-mysql-on-mac-configure-mysql-in-terminal/)

<!-- TODO: Add the link to the pre-setup VM -->

Once you have a **running** MySQL server along with **valid credentials**, we can setup our messages table in the database.

Run the below commands to setup the table.

```
mysql -u user -p
<Enter your MySQL password>
```

```
create database flaskchat;

use flaskchat;

create table messages (
    ID int auto_increment,
    message varchar(200),
    sender varchar(50),
    primary key (ID)
);
```

## Flask version

###