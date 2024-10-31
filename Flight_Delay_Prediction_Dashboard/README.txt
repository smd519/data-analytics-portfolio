SE6242team114 - On-Time Aviation

'On-Time Aviation' is a machine learning based flight delay prediction dashboard," an innovative project that aims to develop an interactive dashboard to accurately predict flight delays for common routes.

A. How It Works
Users will be able to select the origin, destination airport, targeted airlines, and date. The UI will pass the parameters into our model to get predicted values for each airline. The results will be displayed to the users and sorted from less risk to high risk of arrival delay. The dashboard use machine learning (ML) algorithms, which will analyze features such as departure time, route, and airline, to predict the likelihood of a delay. The machine learning algorithm is a XG Boost model which is trained trained using flight information from 2018 to 2022.

B. How It has been implemented
The implementation is based on flaskapp containing following componenets:

The UI imeplemetation (index.html)
The trained model (.sav files)
Communication endpoint between UI and trained model (Routes.py)


C. How to configure the PC

C-1. Setup the envirnment

First you need to create a conda envirnment based on the requirements presented listed in requirements.txt. you can use the follwoing command:

conda create --name <env_name> --file requirements.txt

C-2. Activate the conda envirnment

You need to make sure you are in the right envirnment before launching the applicaion. You can use the follwoing command:

conda activate <env_name>


C-3. Install additional libraries

there are additional libraries which must be installed after creating and activating the envirnment. You can use the follwoing command:

pip install -r requirements_pip.txt

D. How to launch the application

D-1. Activate the conda envirnment

You need to make sure you are in the right envirnment before launching the applicaion. You can use the follwoing command:

 conda activate <env_name>


D-2. Run the python server

You need to setup and run a python http server. You can use the follwoing command:

 python run.py

D-3. Launch the web application

You need to launch a web browser, and launch python server. You can use the following URL in navigate bar:

localhost:3001

E. How to use the application
You must select the origin, destination airport, targeted airlines, and date. The application pass the parameters to our machine learing model to get the predicted likelihood of delay base on your selections. The results will be displayed to the users and sorted from less risk to high risk of arrival delay.