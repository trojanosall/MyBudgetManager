REQUIREMENTS:

Open an admin command prompt and enter:

pip --proxy http://localhost:3128 install autopep8
pip --proxy http://localhost:3128 install msgpack
pip --proxy http://localhost:3128 install zeep
pip --proxy http://localhost:3128 install zeep[async]
pip --proxy http://localhost:3128 install zeep[tornado]
pip --proxy http://localhost:3128 install pyserial
pip --proxy http://localhost:3128 install django-chartjs
pip --proxy http://localhost:3128 install sqlparse
pip --proxy http://localhost:3128 install django-fontawesome-5

Open Anaconda prompt as admin and enter:

conda update --all    <-- This command shoud be run periodically for updating python libraries.
conda install sqlalchemy
conda install sqlalchemy-utils
conda install mysql-connector-c
conda install mysql-connector-python
conda install mysqlclient
conda install django