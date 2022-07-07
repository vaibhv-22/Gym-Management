# Gym Management Database(CLI)


## Installation

- Setup and enable MySQL server

```
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation utility
sudo systemctl start mysql
```

- Login as root user using `sudo mysql -u root -p`, and make a new user connected to localhost

  ```sql
  CREATE USER 'enter_username_here'@'localhost' IDENTIFIED BY 'enter_password_here';
  GRANT ALL PRIVILEGES ON * . * TO 'enter_username_here'@'localhost';
  FLUSH PRIVILEGES;
  ```

  

- Run the python code

```
python3 Gym-Management/Phase\ 4/gym.py 
```

- Enter your login details. You are ready to go now!!

## Supported Functionalities:

- **Insertion:**
  - `insertMember()`
  - `insertTrainer()`
  - `insertStaff()`
  - `insertEquipment()`
- **Deletion:**
  - `deleteMember()`
  - `deleteTrainer()`
  - `deleteStaff()`
  - `deleteEquipment()`
- **Modification:**
  - `updateMember()`
  - `updateTrainer()`
  - `updateStaff()`
  - `updateEquipment()`
- **Report:**
  - `GenerateMemberReport()`
  - `GenerateBranchReport()`
  - `GenerateTrainerReport()`
  - `GenerateStaffReport()`
  - `GenerateEquipmentReport()`
- **Additional:**
  - `GetBmiReportByMemberName()`
  - `GetStaffBySalaryRange()`

<hr>

This is a part of Data and Applications project @IIITH

