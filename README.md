tlr
===

WARNING: This project is DEPRECATED. Do not use it in any production
environment!

This script read temperature and CO2 gas measurements data
from `192.168.10.102` port `2009` and insert it
to `192.168.0.28` MySQL database.

### Cloning The Project

To clone the project, run the following command:

    $ git clone ssh://merapi@192.168.5.74:212/home/merapi/Repositories/tlr.git

### Install Dependencies

1. First, install pip and upgrade to the latest version:

        $ sudo apt-get install python-pip
        $ pip install --upgrade pip

2. Install python MySQLdb module and other development packages:

        $ sudo apt-get install python3-dev libmysqlclient-dev

3. Install other module requirements:

        $ pip install -r requirements.txt

### Install and Run the Script

1. Login to ssh server `192.168.0.28` port 212:

    $ ssh merapi@192.168.0.28 -p 212

2. Change directory to `/home/merapi/Projects/`:

    $ cd /home/merapi/Projects/

3. Clone the projects:

    $ git clone ssh://merapi@192.168.0.28:212/home/merapi/Repositories/tlr.git

4. Use `screen` to run program in the background:

    $ screen -S tlr

5. Run the program:

    $ /home/merapi/Projects/tlr/tlr_acq.sh

6. Press `Ctrl+A` then `Ctrl+D`. This will "detach" your screen session but leave your processes running.

7. Logout of the ssh remote.

8. If you want to resume the screen session, ssh login to `192.168.0.28` and then run `screen -r tlr`.
